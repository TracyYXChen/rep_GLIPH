'''
simply count how many groups have been converged
'''
import argparse, sys

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-nf', '--num_file', type=str)
    parser.add_argument('-mf','--multi_file', type=str)
    return parser

#load file a list
def load_f_a_list(f):
    results = [] 
    for line in f: 
        results.extend(line.strip().split('\n'))
    return results

#load file as a list of lists
def load_f_lists(f):
    tmp = [x.strip().split('\t') for x in f.read().splitlines()]
    return tmp

def count_num(args):
    with open(args.num_file) as in_f:
        single_list = load_f_a_list(in_f)   
    total = 0
    group_3 = 0
    peptide_3 = 0
    group_less = 0
    peptide_less = 0
    for items in single_list:
        total += int(items)
        if int(items) < 3: 
            group_less += 1
            peptide_less += int(items)
        else:
            group_3 += 1
            peptide_3 += int(items)
    ratio_less = peptide_less*100/total
    ratio_3 =peptide_3*100/total
    print("the total size of sequence is %d \nthere are %d groups clustered less than 3,\
    i.e. %.2f%%(%d) sequences,\nthere are %d groups clustered equal or larger\
    than 3, i.e. %.2f%%(%d) sequences"
    %(total,group_less,ratio_less,peptide_less,group_3,ratio_3,peptide_3)) 

def get_set(args):
    '''append peptides of each cluster and return a set of peptides(remove
    duplicates)'''
    with open(args.multi_file) as in_f:
        multi_lists = load_f_lists(in_f)
    all_peptide=[]
    for items in multi_lists:
        all_peptide.append(items[2:])
    #flat list of lists
    flat_list = [item for sublist in all_peptide for item in sublist]
    set_peptide = set(flat_list)
    print("The num of peptides in all clustering(after removing duplicates) are\
    %d"%(len(set_peptide)))
        
def run(args):
    count_num(args)
    #get_set(args)

if __name__ == '__main__':
    run(get_parser().parse_args(sys.argv[1:]))
