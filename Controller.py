from AzureDevops import *
from IBMGitlab import *

class Controller:

    # IBM -> Gitlab
    GL_USER = ""
    GL_PASS = ""
    GL_URL = ""
    GL_TOKEN = ""
    GL_GIT_USER = ""
    GL_GIT_PASS = ""

    # Azure Devops Git
    AZ_TOKEN = ""
    AZ_USER = ""
    AZ_URL = ""
    AZ_ORG = ""

    def setGL_USER(self, GL_USER):
        self.GL_USER = GL_USER

    def getGL_USER(self, GL_USER):
        return self.GL_USER

    def setGL_PASS(self, GL_PASS):
        self.GL_PASS = GL_PASS

    def getGL_PASS(self, GL_PASS):
        return self.GL_PASS

    def setGL_URL(self, GL_URL):
        self.GL_URL = GL_URL

    def getGL_URL(self):
        return self.GL_URL

    def setGL_TOKEN(self, GL_TOKEN):
        self.GL_TOKEN = GL_TOKEN

    def getGL_TOKEN(self):
        return self.GL_TOKEN

    def setGL_GIT_USER(self, GL_GIT_USER):
        self.GL_GIT_USER = GL_GIT_USER

    def getGL_GIT_USER(self):
        return self.GL_GIT_USER

    def setGL_GIT_PASS(self, GL_GIT_PASS):
        self.GL_GIT_PASS = GL_GIT_PASS

    def getGL_GIT_PASS(self):
        return self.GL_GIT_PASS

    def setAZ_TOKEN(self, AZ_TOKEN):
        self.AZ_TOKEN = AZ_TOKEN

    def getAZ_TOKEN(self):
        return self.AZ_TOKEN

    def setAZ_USER(self, AZ_USER):
        self.AZ_USER = AZ_USER

    def setAZ_URL(self, AZ_URL):
        self.AZ_URL = AZ_URL

    def getAZ_URL(self):
        return self.AZ_URL

    def setAZ_ORG(self, AZ_ORG):
        self.AZ_ORG = AZ_ORG

    def getAZ_ORG(self):
        return self.AZ_ORG

    def check_IBM_Vlues(self):
        empty = False
        if self.GL_USER == "":
            empty = True
        if self.GL_PASS == "":
            empty = True
        if self.GL_URL == "":
            empty = True
        if self.GL_TOKEN == "":
            empty = True
        if self.GL_GIT_USER == "":
            empty = True
        if self.GL_GIT_PASS == "":
            empty = True
        return empty

    def check_Azure_Values(self):
        empty = False
        if self.AZ_TOKEN == "":
            empty = True
        if self.AZ_USER == "":
            empty = True
        if self.AZ_URL == "":
            empty = True
        if self.AZ_ORG == "":
            empty = True
        return empty

    def migration_IBM_Azure(self):
        if self.check_IBM_Vlues():
            raise Exception("One ore more IBM values are empty")
        if self.check_Azure_Values():
            raise Exception("One ore more Azure values are empty")
        gl = IBMGitlab(self.GL_USER, self.GL_PASS, self.GL_URL, self.GL_TOKEN)
        az = AzureDevops(self.AZ_TOKEN, self.AZ_USER, self.AZ_URL, self.AZ_ORG, self.GL_GIT_USER, self.GL_GIT_PASS)
        grps = gl.getGroups()
        for grp in grps:
            print("#############################################")
            grp.printGroup()
            name = grp.getName()
            desc = grp.getDesc()
            az.createProject(name, desc)
            glProjects = gl.getProjects(grp)
            for prj in  glProjects:
                id = az.getIDbyName(grp.getName())
                url = prj.getUrl()
                name = prj.getName()
                projectName = grp.getName()
                az.importRepo(url, id, name, projectName)
        print("#############################################")
        print(" All Git has been migrated!!!")
        print("#############################################")
