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