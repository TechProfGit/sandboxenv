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
