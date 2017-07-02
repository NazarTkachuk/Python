#!/usr/bin/env python
"""module docstring"""
# imports standard
# import third party libraries
# local packages/modules imports
import os
import sys

def print_dict(dict_to_print):
    for item in dict_to_print:
        print(item, dict_to_print[item])
        print('\n')

def write_files_with_packeges(dict_to_parse):
    for item in dict_to_parse:
        open(item.txt, 'w')
        item.write(dict_to_parse[item])

def create_packages(list_to_parse):
    dict_of_packages = {'Ivasyk':[], 'Dmytryk':[], 'Ostap':[], 'Lesya':[]}
    for string in list_to_parse:
        if string=="\n":
            continue;
        if string.endswith(' end\n'):
            dict_of_packages['Lesya'].append(string)
        elif (len(string)-1)%2==0:
            dict_of_packages['Ivasyk'].append(string)
        elif string[0].isupper():
            dict_of_packages['Dmytryk'].append(string)
        else:
            dict_of_packages['Ostap'].append(string)
    return dict_of_packages


def create_lines_list(path_to_file):
    text = open(path_to_file)
    file_list = text.readlines()
    text.close()
    return file_list

def main():
    fn = sys.argv[1]
    if os.path.exists(fn):
        #print os.path.basename(fn)
	lines_list = create_lines_list(fn)
    diction = create_packages(lines_list)
    print_dict(diction)



if __name__ == '__main__':
    main()
