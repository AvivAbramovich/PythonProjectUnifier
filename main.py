from sys import argv, exit
from os.path import isdir
from parse_project_structure import parse_project_structure
from append_module import enumerate_modules_structure

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
        enumerate_modules_structure(modules_structure, o_fh)
