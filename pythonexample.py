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
