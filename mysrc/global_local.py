'''Thsi program is to extract values of different columns under 
different names.'''

import argparse, sys

def get_parser():
    parser = argparse.ArgumentParser()
    #two arguments passed from terminal
    parser.add_argument("-mf","--multi_f",type=str, help = "the file has multiple columns.")
    return parser

#load file into a list of list
def load_f_lists(in_f):
    tmp = [x.strip().split('\t') for x in in_f.read().splitlines()]
    return tmp

def run(args):
    with open(args.multi_f) as my_f:
        list_many = load_f_lists(my_f)
#new lists to store values from different types
    list_global = []
    list_local = []
    list_single= []
    for single_list in list_many:
        if single_list[2] == "global":
#append its values
            list_global.append(single_list[0])
            list_global.append(single_list[1])
        elif single_list[2] == "local":
            list_local.append(single_list[0])
            list_local.append(single_list[1])
        elif single_list[2] == "singleton":
            list_single.append(single_list[0])
            list_single.append(single_list[1])
    #do the set operation
    set_global = set(list_global)
    set_local = set(list_local)
    set_single = set(list_single)
    #print(len(set_global.intersection(set_local)))
    union_glocal = set_global | set_local
    inter_glocal = set_global.intersection(set_local)
    print("the union size of local and global are %d, the intersection size of\
    local and global are %d, and the global-unique size is %d, and the\
    local-unique size is %d"%(len(union_glocal), len(inter_glocal),
    len(set_global)-len(inter_glocal), len(set_local) - len(inter_glocal)))

    total = len(set(set_global | set_local | set_single))
    g_percent = round(len(set_global)*100/total,2)
    l_percent = round(len(set_local)*100/total,2)
    s_percent = round(len(set_single)*100/total,2)

    print("there are %d total peptides\nthere are %d global clustering,\
    i.e. %.2f%%,\nthere are %d local clustering, i.e. %.2f%%,\nthere are %d \
    singleton, i.e. %.2f%%."%(total,
    len(set_global),g_percent,len(set_local),l_percent, len(set_single),s_percent))
    
    '''

    #do without set
    total=len(list_global) + len(list_local) + len(list_single)
    g_percent = round(len(list_global)*100/total,2)
    l_percent = round(len(list_local)*100/total,2)
    s_percent = round(len(list_single)*100/total,2)
    print("there are %d total peptides\nthere are %d global clustering,\
    i.e. %.2f%%,\nthere are %d local clustering, i.e. %.2f%%,\nthere are %d \
    singleton, i.e. %.2f%%."%(total,
    len(list_global),g_percent,len(list_local),l_percent, len(list_single),s_percent))
    '''


if __name__ == '__main__':
    run(get_parser().parse_args(sys.argv[1:]))        
