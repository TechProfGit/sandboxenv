import json

# Open the JSON file
with open("data.json", "r") as file:
    data = json.load(file)

# Define the properties you want to retrieve
desired_properties = ["name", "age"]

# Iterate through each object in the list
for item in data:
    # Create a new dictionary containing only the desired properties
    selected_properties = {prop: item[prop] for prop in desired_properties}
    print(selected_properties)
