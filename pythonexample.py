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

#---------------
import re

def replace_url_in_file(input_file, output_file, search_pattern, replace_string):
    with open(input_file, 'r') as f:
        content = f.read()

    modified_content = re.sub(search_pattern, replace_string, content)

    with open(output_file, 'w') as f:
        f.write(modified_content)

input_file_path = 'input.txt'
output_file_path = 'output.txt'
search_pattern = r'https://mywebsite\.com/.+?\.jpeg'
replace_string = r'https://images.com\g<0>'

replace_url_in_file(input_file_path, output_file_path, search_pattern, replace_string)

print("URLs replaced successfully.")
