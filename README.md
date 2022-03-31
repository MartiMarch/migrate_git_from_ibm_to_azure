<h1>Migrate data form IBM Gitlab to Azure Devops Git</h1>
<h2>Requeriments</h2>
<p> - Git</p>
<p> - Python 3</p>
<h2>How to use</h2>
<p align="justify">Controller class manage the interaction between both git repositories. IBMGitlab calls to IBM Gitlab API and AzureDevops calls to Azure Devops API. If you want to develop new features you will need to edit the two previous classes. main class invoke the controller and contains all the necessary data to realize the connection, as tokens, user, passwords, etc. If you need connect to another git, as GitHub, you only have to crete a new class named, for example, GitHub. This class will call to the API and controller will manage interaction with another git repositories.</p>
