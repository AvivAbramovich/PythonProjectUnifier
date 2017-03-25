from os import walk
from os.path import join

def path_to_dirs_list(orig_path, current_path):
    relative_path = current_path[len(orig_path)+1:]
    return relative_path.split('/') # for unix based


# def add_depth(dictionary, current_depth=0):
#     if 'depth' not in dictionary:
#         dictionary['depth'] = current_depth
#     for key in dictionary.keys():
#         if type(dictionary[key]) == dict:
#             add_depth(dictionary[key], current_depth+1)


def parse_project_structure(base_path):
    modules_structure = {}
    for current_path, sub_dirs, files in walk(base_path):
        dirs_list = path_to_dirs_list(base_path, current_path)
        pointer = modules_structure
        for dir in dirs_list:
            if len(dir) > 0:
                if dir not in pointer:
                    pointer[dir] = {'type': 'directory'}
                pointer = pointer[dir]
        for file in files:
            if file.endswith('.py'):
                pointer[file] = {'type': 'module', 'path': join(current_path, file), 'name' : file}

    # add_depth(modules_structure)
    return modules_structure
