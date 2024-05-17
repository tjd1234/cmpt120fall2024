# import_sort.py

#
# Reads a file of Python import statements, and prints them out in sorted order.
# Any duplicate imports are removed.
#

def solution1():
    """Sample solution using a list to keep track of the modules.
    """
    print('# solution 1')
    module_list = []
    file = open('sample_imports.py')
    for line in file:
        line = line.strip()
        if line not in module_list:
            module_list.append(line)

    module_list.sort()
    for mod in module_list:
        print(f'{mod}')

solution1()

def solution2():
    """Sample solution using a dictionary to keep track of the modules.
    """
    print('# solution 2')
    module_dict = {}
    file = open('sample_imports.py')
    for line in file:
        line = line.strip()
        module_dict[line] = 1

    all_modules = list(module_dict.keys())
    all_modules.sort()
    for mod in all_modules:
        print(f'{mod}')

solution2()
