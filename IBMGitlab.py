import subprocess
import re
import json

class Group:
    ID = ""
    NAME = ""
    DESC = ""

    def __init__(self, ID, NAME, DESC):
        self.ID = ID
        self.NAME = NAME
        self.DESC = DESC

    def printGroup(self):
        print("Group name: \'" + self.NAME + "\', ID: \'" + self.ID + "\'")

    def getName(self):
        return self.NAME

    def getId(self):
        return self.ID

    def getDesc(self):
        return self.DESC

class Project:
        ID = ""
        NAME = ""
        DESC = ""
        URL = ""

        def __init__(self, ID, NAME, DESC, URL):
                self.ID = ID
                self.NAME = NAME
                self.DESC = DESC
                self.URL = URL

        def printProject(self):
                print("Project name: \'" + self.NAME + " \', url: \'" + self.URL + "\'")

        def getId(self):
                return self.ID

        def getName(self):
                return self.NAME

        def getDescription(self):
                return self.DESC

        def getUrl(self):
                return self.URL

class IBMGitlab:
    USER = ""
    PASS = ""
    URL = ""
    TOKEN = ""
    API_URL = ""

    def __init__(self, USER, PASS, URL, TOKEN):
        self.USER = USER
        self.PASS = PASS
        self.URL = URL
        self.TOKEN = TOKEN
        self.API_URL = "curl --header \'PRIVATE-TOKEN: " + self.TOKEN + "\' -s -XGET https://" + self.USER + ":" + self.PASS + "@" + self.URL

    def getGroups(self):
        grps = []
        command = self.API_URL + "/groups"
        out = self.MyShell(command)
        json_groups = json.loads(out)
        for object in json_groups:
            id = str(object['id'])
            name = object['name']
            desc = object['description']
            grp = Group(id, name, desc)
            grps.append(grp)
        return grps

    def getProjects(self, grp):
        prjs = []
        command = self.API_URL + "/groups/" + grp.getId() + "/projects"
        out = self.MyShell(command)
        json_projects = json.loads(out)
        for object in json_projects:
            id = str(object['id'])
            name = object['name']
            desc = object['description']
            url = object['http_url_to_repo']
            prj = Project(id, name, desc, url)
            prjs.append(prj)
        return prjs

    def MyShell(self, command):
        return subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
