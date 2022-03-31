import os
import subprocess
import json
import time

class Project:
    NAME = ""
    ID = ""

    def __init__(self, NAME, ID):
        self.NAME = NAME
        self.ID = ID

    def getName(self):
        return self.NAME

    def getId(self):
        return self.ID

    def printProject(self):
        print("Name project: \'" + self.NAME + "\', ID project: " + self.ID)

class AzureDevops:
    TOKEN = ""
    USER = ""
    URL = ""
    ORG = ""
    JSON_HEAD = "--header \"Content-Type: application/json\""
    GIT_USER = ""
    GIT_TOKEN = ""
    GIT_PATH = "/home/temporalRepo"
    DELAY = 5

    def __init__(self, token, user, url, org, git_user, git_token):
        self.TOKEN = token
        self.USER = user
        self.URL = url
        self.ORG = org
        self.GIT_USER = git_user
        self.GIT_TOKEN = git_token

    def getProjects(self):
        command = "curl -u " + self.USER + ":" + self.TOKEN + " -s -X GET " + self.URL + self.ORG + "/_apis/projects?api-version=6.0"
        out = self.MyShell(command)
        json_projects = json.loads(out)
        projectArray = json_projects['value']
        projects = []
        for project in projectArray:
            name = project['name']
            id = project['id']
            projects.append(Project(name, id))
        return projects

    def printProjects(self, projects):
        n = 1
        for project in projects:
            print("Project[" + str(n) + "] \'" + project.getName() + "\'")
            n = n + 1

    def getIDbyName(self, name):
        projects = self.getProjects()
        for project in projects:
            prj_name = project.getName()
            if prj_name == name:
                return project.getId()

    def createProject(self, name, description):
        json = "\'"
        json += "{"
        json +=   "\"name\": \"" + name + "\","
        json +=   "\"description\": \"" + description + "\","
        json +=   "\"visibility\": \"private\","
        json +=   "\"capabilities\": {"
        json +=     "\"versioncontrol\": {"
        json +=       "\"sourceControlType\": \"Git\""
        json +=     "},"
        json +=     "\"processTemplate\": {"
        json +=       "\"templateTypeId\": \"6b724908-ef14-45cf-84f8-768b5384da45\""
        json +=     "}"
        json +=   "}"
        json += "}"
        json += "\'"
        command = "curl -u " + self.USER + ":" + self.TOKEN + " -s -X POST " + self.URL + self.ORG + "/_apis/projects?api-version=6.0 " + self.JSON_HEAD + " --data " + json
        out = self.MyShell(command)
        print("Project \'" + name + "\' created...")
        time.sleep(self.DELAY)
        return out

    def importRepo(self, url, id, name, projectName):
        http_projectName = projectName.replace(' ', "%20")
        http_json = "\'"
        http_json += "{"
        http_json +=   "\"name\": \"" + name + "\","
        http_json +=   "\"project\": {"
        http_json +=     "\"id\": \"" + str(id) + "\""
        http_json +=   "}"
        http_json += "}"
        http_json += "\'"
        command = "curl -u " + self.USER + ":" + self.TOKEN + " -s -X POST " + self.URL + self.ORG + "/_apis/git/repositories/repositories?api-version=6.0 " + self.JSON_HEAD + " --data " + http_json
        self.MyShell(command)
        print("++ Repo \'" + name + "\' created...")
        command = "mkdir -p " + self.GIT_PATH
        self.MyShell(command)
        url_1 = "https://" + self.GIT_USER + ":" + self.GIT_TOKEN + "@"
        url_2 = url[8:]
        url = url_1 + url_2
        print("++ Moving \'" + name + "\'")
        print("-> Cloning repo from IBM...")
        command = "git clone " + url + " " + self.GIT_PATH
        print("Done!")
        self.MyShell(command)
        command = "curl -u " + self.USER + ":" + self.TOKEN + " -s -X GET " + self.URL + self.ORG + "/" + http_projectName + "/_apis/git/repositories?api-version=6.0"
        out = self.MyShell(command)
        json_out = json.loads(out)
        json_repos = json_out['value']
        repoID = ""
        name = name.strip()
        for object in json_repos:
            if object['name'] == name:
                repoURL = object['remoteUrl']
                repoName = object['name']
        print("-> Starting git repo locally...")
        command = "git --git-dir=" + self.GIT_PATH + "/.git --work-tree=" + self.GIT_PATH + " init"
        self.MyShell(command)
        print("Done!")
        command = "git --git-dir=" + self.GIT_PATH + "/.git --work-tree=" + self.GIT_PATH + " remote -v"
        out = self.MyShell(command)
        if "fatal" in out.decode():
            print("-> Adding remote url...")
            command = "git --git-dir=" + self.GIT_PATH + "/.git --work-tree=" + self.GIT_PATH + " remote add origin " + repoURL
            self.MyShell(command)
            print("Done!")
        else:
            print("-> Adding remote url...")
            command = "git --git-dir=" + self.GIT_PATH + "/.git --work-tree=" + self.GIT_PATH + " remote set-url origin " + repoURL
            self.MyShell(command)
            print("Done!")
        print("-> Adding local files...")
        command = "git --git-dir=" + self.GIT_PATH + "/.git --work-tree=" + self.GIT_PATH + " add --all"
        print("Done!")
        self.MyShell(command)
        print("-> Creating first commit...")
        command = "git --git-dir=" + self.GIT_PATH + "/.git --work-tree=" + self.GIT_PATH + " commit -m \'First commit\'"
        try:
            self.MyShell(command)
        except Exception:
            pass
        print("-> Pushing repo")
        url1 = "https://" + self.USER.replace('@', "%40") + ":" + self.TOKEN
        url2 = "@dev.azure.com/" + repoURL[len("https://") + len(self.USER.replace('@', "%40")):]
        url = url1 + url2
        command = "git --git-dir=" + self.GIT_PATH + "/.git --work-tree=" + self.GIT_PATH + " push " + url + " --all"
        self.MyShell(command)
        print("Done!")
        command = "rm -rf " + self.GIT_PATH + "/.git"
        self.MyShell(command)
        command = "rm -rf " + self.GIT_PATH
        self.MyShell(command)

    def MyShell(self, command):
        return subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
