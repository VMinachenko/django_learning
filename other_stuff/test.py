import os
import json

path = r"c:\Users\vmina\OneDrive\Desktop\Odcore\django_project_explorer\django-projects-explorer\Parsers"

def get_files_with_path_v1(directory):
    files_dict = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            files_dict[file] = file_path
    return {directory: files_dict}


result = get_files_with_path_v1(path)
output_file = "result_v1.json"
with open(output_file, "w") as file:
    json.dump(result, file, indent=4)



def get_files_with_path_v2(directory):
    files_dict = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            parent_directory = os.path.relpath(root, directory)
            if parent_directory not in files_dict:
                files_dict[parent_directory] = []
            files_dict[parent_directory].append({file: file_path})
    return {directory: files_dict}

result = get_files_with_path_v2(path)
output_file = "result_v2.json"
with open(output_file, "w") as file:
    json.dump(result, file, indent=4)