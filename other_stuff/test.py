import os
import json
import uuid

# Structure
# C:\Users\vmina\OneDrive\Desktop\Odcore\other_stuff\I Love Python 12!#
# C:\Users\vmina\OneDrive\Desktop\Odcore\other_stuff\I Love Python 12!#\Kek &2!
# C:\Users\vmina\OneDrive\Desktop\Odcore\other_stuff\I Love Python 12!#\Kek &2!\SJSJSJ.txt
# C:\Users\vmina\OneDrive\Desktop\Odcore\other_stuff\I Love Python 12!#\Kek &2!\EIEEIEIE
# C:\Users\vmina\OneDrive\Desktop\Odcore\other_stuff\I Love Python 12!#\Kek &2!\EIEEIEIE\SPSPSPS!.txt
# C:\Users\vmina\OneDrive\Desktop\Odcore\other_stuff\I Love Python 12!#\Lol
# C:\Users\vmina\OneDrive\Desktop\Odcore\other_stuff\I Love Python 12!#\Lol\SSKSKKSS.txt
# C:\Users\vmina\OneDrive\Desktop\Odcore\other_stuff\I Love Python 12!#\WELCOME.txt


# Creating uuid for each file
# def retrieve_file_structure(path):
#     structure = {}

#     def clean_name(name):
#         # Removes special characters, converts to lowercase,
#         # and replaces spaces with underscores
#         return ''.join(char.lower() if char.isalnum() else '_' for char in name)

#     def traverse_directory(directory, parent_structure):
#         files = os.listdir(directory)
#         for file in files:
#             file_path = os.path.join(directory, file)
#             file_name = os.path.basename(file_path)
#             cleaned_file_name = clean_name(file_name)
#             if os.path.isdir(file_path):
#                 sub_structure = {
#                     'id': str(uuid.uuid4()),
#                     'original_folder_name': file_name,
#                     'path': file_path
#                 }
#                 parent_structure[cleaned_file_name] = sub_structure
#                 traverse_directory(file_path, sub_structure)
#             else:
#                 parent_structure[cleaned_file_name] = {
#                     'id': str(uuid.uuid4()),
#                     'original_file_name': file_name,
#                     'path': file_path
#                 }

#     structure['id'] = str(uuid.uuid4())
#     traverse_directory(path, structure)
#     return {structure['id']: structure}


def retrieve_file_structure(path):
    structure = {}

    def clean_name(name):
        # Removes special characters, converts to lowercase, and replaces spaces with underscores
        return ''.join(char.lower() if char.isalnum() else '_' for char in name)

    def traverse_directory(directory, parent_structure):
        files = os.listdir(directory)
        for file in files:
            file_path = os.path.join(directory, file)
            file_name = os.path.basename(file_path)
            cleaned_file_name = clean_name(file_name)
            if os.path.isdir(file_path):
                sub_structure = {
                    'original_folder_name': file_name,
                    'path': file_path
                }
                parent_structure[cleaned_file_name] = sub_structure
                traverse_directory(file_path, sub_structure)
            else:
                parent_structure[cleaned_file_name] = {
                    'original_file_name': file_name,
                    'path': file_path
                }
    main_id = str(uuid.uuid4())
    structure['id'] = main_id
    structure['path'] = path
    traverse_directory(path, structure)
    return {main_id: structure}


# path = r'C:\Users\vmina\OneDrive\Desktop\Odcore\other_stuff\I Love Python 12!#'
# result = retrieve_file_structure(path)
# output_file = "result_v4.json"
# with open(output_file, "w") as file:
#     json.dump(result, file, indent=4)
