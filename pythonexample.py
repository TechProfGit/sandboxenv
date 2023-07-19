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
