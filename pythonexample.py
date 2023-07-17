dbutils.secrets.set("github-sp", "<client-id>")
dbutils.secrets.set("github-sp-secret", "<client-secret>")
dbutils.secrets.set("github-sp-tenant", "<tenant-id>")

import com.databricks.labs.spark.github._
import org.eclipse.jgit.api._

val clientId = dbutils.secrets.get("github-sp", "<client-id>")
val clientSecret = dbutils.secrets.get("github-sp-secret", "<client-secret>")
val tenantId = dbutils.secrets.get("github-sp-tenant", "<tenant-id>")

val token = GitHubUtilities.generateTokenFromSP(clientId, clientSecret, tenantId)

// Clone the repository
val gitUrl = "https://<github-username>:<generated-token>@github.com/<your-username>/<repository>.git"
val destinationPath = "/mnt/<mount-point>"
Git.cloneRepository.setURI(gitUrl).setDirectory(destinationPath).call()

// Download a specific file from the repository
val fileToDownload = "path/to/file"
val filePath = "/mnt/<mount-point>/<file-name>"
Git.cloneRepository.setURI(gitUrl).call().getRepository.copyTo(filePath, fileToDownload)
// ===========================================


import requests
import zipfile


repo_owner = "<github-owner>"
repo_name = "<github-repo>"
branch_name = "<github-branch>"
client_id = "<aad-client-id>"
client_secret = "<aad-client-secret>"
tenant_id = "<aad-tenant-id>"


token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token"
headers = {"Content-Type": "application/x-www-form-urlencoded"}
data = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret,
    "scope": "https://graph.microsoft.com/.default"
}
response = requests.post(token_url, headers=headers, data=data)
access_token = response.json()["access_token"]


zip_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/zipball/{branch_name}"
headers = {"Authorization": f"Bearer {access_token}"}
response = requests.get(zip_url, headers=headers)


with open("/dbfs/tmp/github_repo.zip", "wb") as zip_file:
    zip_file.write(response.content)



// ============================================
