'''This program read a file into a list, and return the set of it'''
import argparse, sys

def get_parser():
    parser = argparse.ArgumentParser()
    #two arguments passed from terminal
    parser.add_argument("-if","--input_file",type=str, help = "the file has multiple columns.")
    parser.add_argument("-of","--output_file",type=str, help = "save set to another file")
    return parser

#load file into a list
 
def load_f_a_list(in_f):
    results = [] 
    for line in in_f: 
        results.extend(line.strip().split('\n'))
    return results
 

def run(args):
    my_list = []
    my_set = ()
    set_list = []
    with open(args.input_file) as file_1:
        my_list = load_f_a_list(file_1)    
    my_set = set(my_list)
    for items in my_set:
        set_list.append(items)

    #write the result into a new file.
    with open(args.output_file,'w') as out_f:
        for rows in set_list:
            out_f.write(rows + '\n')

if __name__ == '__main__':
    run(get_parser().parse_args(sys.argv[1:]))

