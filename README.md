<style type="text/css">
.table{
  background: #ffffff
}
</style>

<h1>Migrate data form IBM Gitlab to Azure Devops Git</h1>
<h2>Requeriments</h2>
<p> - Git</p>
<p> - Python 3</p>
<h2>How it works</h2>
<p align="justify">Controller class manage the interaction between both git repositories. <strong>IBMGitlab</strong> calls to IBM Gitlab API and <strong>AzureDevops</strong> calls to Azure Devops API. If you want to develop new features you will need to edit the two previous classes. <strong>main</strong> class invoke the controller and contains all the necessary data to realize the connection, as tokens, user, passwords, etc. If you need connect to another git, as GitHub, you only have to crete a new class named, for example, GitHub. This class will call to the API and controller will manage interaction with another git repositories.</p>
<h2>How to use</h2>
<p align="justify">Execute the class main:</p>
<p><strong>&ensp;&ensp;&ensp;&ensp;python3 main.py</strong></p>
<p>You will need to fill the next values before execute the script:</p>
<table>
  <tr>
    <th>
      IBM Gitlab variables
    </th>
  </tr>
  <tr>
    <td>
      GL_USER
    </td>
    <td>
      IBM user
    </td>
  </tr>
  <tr>
    <td>
      GL_PASS      
    </td>
    <td>
      IBM password
    </td>
  </tr>
  <tr>
    <td>
      GL_URL
    </td>
    <td>
      Part of API url
    </td>
  </tr>
  <tr>
    <td>
      GL_TYOKEN
    </td>
    <td>
      IBM Gitlab token
    </td>
  </tr>
  <tr>
    <td>
      GL_GIT_USER
    </td>
    <td>
      IBM Gitlab user
    </td>
  </tr>
  <tr>
    <td>
      GL_GIT_PASS
    </td>
    <td>
      IBM Gitlab password
    </td>
  </tr>
</table>
<br>
<table>
  <tr>
    <th>
      Azure Devops Git
    </th>
  </tr>
  <tr>
    <td>
      AZ_TOKEN
    </td>
    <td>
      Git token
    </td>
  </tr>
  <tr>
    <td>
      AZ_USER
    </td>
    <td>
      Git user
    </td>
  </tr>
  <tr>
    <td>
      AZ_URL
    </td>
    <td>
      Defualt Git URL 
    </td>
  </tr>
  <tr>
    <td>
      AZ_ORG
    </td>
    <td>
      Git organitzation name
    </td>
  </tr>
</table>
