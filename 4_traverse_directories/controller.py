import ntpath
import os


# ss = [os.getcwd()]
# while ss:
#     current_dir = ss.pop()
#     print(current_dir)
#     if os.path.isfile(current_dir):
#         continue
#
#     for file_path in os.listdir(current_dir):
#         absolute_path = os.path.join(current_dir, file_path)
#         ss.append(absolute_path)
#

# file_list = []
# current_dir = os.getcwd()
# files = os.listdir()
#
# files_dict = {}
# for el in files:
#     extension = f".{el.split('.')[1]}"
#     if extension not in files_dict:
#         files_dict[extension] = []
#     files_dict[extension].append(el)
#
# for key, value in sorted(files_dict.items()):
#     print(key)
#     for el in value.sort():
#         print(f'- - - {el}')

current_dir = os.getcwd()
dict_files = {}


def traverse_directories(starting_directory, files_dict):

    for x in os.listdir(starting_directory):
        current_path = os.path.join(starting_directory, x)
        if os.path.isfile(current_path):
            extension = f".{x.split('.')[-1]}"
            if extension not in files_dict:
                files_dict[extension] = []
            files_dict[extension].append(x)
        elif os.path.isdir(current_path):
            traverse_directories(current_path, files_dict)
    return files_dict


print(traverse_directories(current_dir, dict_files))



