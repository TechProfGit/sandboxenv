import re

def replace_url_in_file(input_file, output_file, search_pattern, replace_string):
    with open(input_file, 'r') as f:
        content = f.read()

    modified_content = re.sub(search_pattern, replace_string, content)

    with open(output_file, 'w') as f:
        f.write(modified_content)

input_file_path = 'input.txt'
output_file_path = 'output.txt'
search_pattern = r'https://www\.mywebsite\.com/.+?/\w+\.(jpg|jpeg|png)'
replace_string = r'https://www.abcd.com/img/\w+\g<1>'

replace_url_in_file(input_file_path, output_file_path, search_pattern, replace_string)

print("URLs replaced successfully.")


#======================
import os

def get_file_list(directory):
    file_list = []
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_list.append(filename)
    return file_list

directory_path = '/path/to/your/directory'
file_list = get_file_list(directory_path)

print("List of files in the directory:")
for filename in file_list:
    print(filename)

#======================================
import os

def rename_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"File '{old_name}' renamed to '{new_name}' successfully.")
    except OSError as e:
        print(f"Error renaming the file: {e}")

old_file_name = 'old_file.txt'
new_file_name = 'new_file.txt'

rename_file(old_file_name, new_file_name)
