<h1>Migrate data form IBM Gitlab to Azure Devops Git</h1>
<h2>Requeriments</h2>
* Git
* Python 3
<h2>How it works</h2>
<p align="justify">Controller class manage the interaction between both git repositories. <strong>IBMGitlab</strong> calls to IBM Gitlab API and <strong>AzureDevops</strong> calls to Azure Devops API. If you want to develop new features you will need to edit the two previous classes. <strong>main</strong> class invoke the controller and contains all the necessary data to realize the connection, as tokens, user, passwords, etc. If you need connect to another git, as GitHub, you only have to crete a new class named, for example, GitHub. This class will call to the API and controller will manage interaction with another git repositories.</p>
<h2>How to use</h2>
<p align="justify">Execute the class main:</p>

python3 main.py

