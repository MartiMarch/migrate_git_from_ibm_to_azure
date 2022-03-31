from Controller import *

# IBM -> Gitlab
GL_USER=""
GL_PASS=""
GL_URL="us-south.git.cloud.ibm.com/api/v4"
GL_TOKEN=""
GL_GIT_USER=""
GL_GIT_PASS=""

# Azure Devops Git
AZ_TOKEN = ""
AZ_USER = ""
AZ_URL = "https://dev.azure.com/"
AZ_ORG = ""

c = Controller()
c.setGL_USER(GL_USER)
c.setGL_PASS(GL_PASS)
c.setGL_URL(GL_URL)
c.setGL_TOKEN(GL_TOKEN)
c.setGL_GIT_USER(GL_GIT_USER)
c.setGL_GIT_PASS(GL_GIT_PASS)
c.setAZ_TOKEN(AZ_TOKEN)
c.setAZ_USER(AZ_USER)
c.setAZ_URL(AZ_URL)
c.setAZ_ORG(AZ_ORG)
c.migration_IBM_Azure()
