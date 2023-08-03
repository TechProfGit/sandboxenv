import requests

# Set up authentication and API endpoint
databricks_host = "https://<databricks-instance>"
databricks_token = "<your-databricks-token>"
headers = {
    "Authorization": "Bearer " + databricks_token,
    "Content-Type": "application/json"
}
url = f"{databricks_host}/api/2.0/clusters/list"

# Make API request to get clusters
response = requests.get(url, headers=headers)
response.raise_for_status()
clusters = response.json()["clusters"]

# Retrieve Cluster ID for a specific notebook
notebook_path = "/Workspace/path/to/notebook"
cluster_id = None
for cluster in clusters:
    if cluster["state"] == "RUNNING" and cluster["notebook_task"]["notebook_path"] == notebook_path:
        cluster_id = cluster["cluster_id"]
        break

# Print the Cluster ID
print("Cluster ID:", cluster_id)

Go to the Databricks workspace.
Click on the "User Settings" icon (usually a user profile picture) in the top-right corner.
Click on "User Settings" in the dropdown menu.
In the "Access Tokens" tab, click "Generate New Token."
Enter a name for the token and set the expiration if needed.
Click "Generate."

my_variable=$(databricks notebooks run --notebook-path "<notebook-path>" --json "{\"run_my_code\": true}" | jq -r '.metadata.userExtraPythonResults.my_variable')
echo $my_variable




# Replace the placeholders with your actual values
storage_account_name="<storage_account_name>"
storage_account_key="<storage_account_key>"
container_name="<container_name>"
folder_name="<folder_name>"

az storage blob list --account-name $storage_account_name --account-key $storage_account_key --container-name $container_name --prefix $folder_name/ --output tsv --query '[].{Name:name}' |
while read -r blob_name
do
    destination_path="${blob_name//$folder_name\//}" # Remove folder prefix from the blob name to get the destination path
    echo "Downloading: $blob_name to $destination_path"
    az storage blob download --account-name $storage_account_name --account-key $storage_account_key --container-name $container_name --name "$blob_name" --file "$destination_path"
done

