'''Besides returning the intersection of 2 single columns, this program is to compare file A and file B, file A may contain many columns,
demilimted by tab. And file B only contains one column. And this column has some 
intersection with a column of A. This program will return part of A that has intersection
with B. 

e.g 
File A: 
Alice Bob 3
Bob Terry 4
Candy Tom 5

File B:
Alice
Bob

Output:
Alice Bob 3
'''

#   read file A into list of list, 
#   read file B into a total list
#   check every item in A, if it is in B, append the list.
#   save the list to file "intersect_output.txt"

import argparse, sys

def get_parser():
    parser = argparse.ArgumentParser()
    #two arguments passed from terminal
    parser.add_argument("-mf1","--multi_f",type=str, help = "the file has multiple columns.")
    parser.add_argument("-sf1","--single_f1",type=str, help = "the file has only 1 column.")
    parser.add_argument("-sf2","--single_f2",type=str, help ="the file has only 1 column")
    parser.add_argument("-of","--outfile",type=str, help = "the name of output file")
    parser.add_argument("-num","--common_number",type=int, default=1,help="number of common columns")
    return parser

#load file into a list of list
def load_f_lists(in_f):
    tmp = [x.strip().split('\t') for x in in_f.read().splitlines()]
    return tmp
 
def load_f_a_list(in_f):
    results = [] 
    for line in in_f: 
        results.extend(line.strip().split('\n'))
    return results
 
def single_single(args):
    with open(args.single_f1) as file_1:
        list_1 = load_f_a_list(file_1)
    with open(args.single_f2) as file_2:
        list_2 = load_f_a_list(file_2)
    return set(list_1).intersection(list_2)

def many_single(args):
    with open(args.multi_f) as mfile:
        list_many = load_f_lists(mfile)
    #read whole file as a single list
    with open(args.single_f1) as sfile:
        list_single = load_f_a_list(sfile)
        
    inter = []
    for items in list_many:
        if len(set(items).intersection(set(single))) == args.common_number:
            inter.append(items)
    return inter

def run(args):
#if it's single-single situation
    if type(args.multi_f) == type(None):
        inter_set = single_single(args)
        with open(args.outfile,'w') as out_f:
            for item in inter_set:
                out_f.write("%s\n" % item)
#if it's single-many situation
    else:
        inter_set = many_single(args)
        with open(args.outfile,'w') as out_f:
            for rows in inter_set:
                line = '\t'.join(map(str,rows))
                out_f.write(line + '\n')

if __name__ == '__main__':
    run(get_parser().parse_args(sys.argv[1:]))


