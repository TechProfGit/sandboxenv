# List the contents of a DBFS directory
directory_path = "/dbfs/mnt/my-mount-point"

contents = dbutils.fs.ls(directory_path)

# Find the first folder
first_folder_path = None
for item in contents:
    if item.isDir():
        first_folder_path = item.path
        break

if first_folder_path:
    print("First folder path:", first_folder_path)
else:
    print("No folders found in the directory.")
