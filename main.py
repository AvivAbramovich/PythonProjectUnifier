from sys import argv, exit
from os.path import isdir, join
from os import walk

__author__ = 'AvivAbramovich'
__version__ = '0.0.1'

def path_to_dirs_list(orig_path, current_path):
    relative_path = current_path[len(orig_path)+1:]
    return relative_path.split('/') # for unix based

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
    return modules_structure

def append_module(output_file_handler, depth, module_path, module_name):
    ident = ''
    for i in xrange(0, depth):
        ident += '\t'
    output_file_handler.write(ident + 'class ' + module_name[:-3] + ':\r\n') # -3 remove the .py
    num_lines = 0
    with open(module_path, 'r') as in_fh:
        for line in in_fh:
            num_lines += 1
            output_file_handler.write(ident + '\t' + line + '\r\n')
    if num_lines == 0:  # empty file
        output_file_handler.write(ident + '\tpass\r\n')


def enumerate_modules_structure(modules_structure, output_file_handler, depth=0):
    for key in modules_structure.keys():
        if type(modules_structure[key]) is dict:
            if modules_structure[key]['type'] == 'module':
                append_module(output_file_handler, depth, modules_structure[key]['path'], modules_structure[key]['name'])
            else:
                enumerate_modules_structure(modules_structure[key], output_file_handler, depth+1)

if __name__ == '__main__':
    if len(argv) != 3:
        print 'Usage: unifier.py <containing directory path> <output file path>'
        exit(1)

    base_path = argv[1]
    output_path = argv[2]
    if not isdir(base_path):
        print '\'{}\' does not exists'.format(base_path)
        exit(1)

    modules_structure = parse_project_structure(base_path)
    with open(output_path, 'w') as o_fh:
        o_fh.write('Unified by Python-Projects-Unifier by {}, version {}\r\n'.format(__author__, __version__))
        enumerate_modules_structure(modules_structure, o_fh)
