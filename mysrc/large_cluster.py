'''
This program is to store large clusters whose size >= 3
'''
import argparse, sys

def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-if', '--input_file', type=str)
    parser.add_argument('-of','--output_file', type=str)
    return parser

#load file a list
def load_f_lists(f):
    tmp = [x.strip().split('\t') for x in f.read().splitlines()]
    return tmp

def store_large(in_list):
    cluster_name = []
    for items in in_list:
        #print("itmes",items)
        if int(items[0]) >= 3:
            cluster_name.append(items[1])
    return cluster_name

def run(args):
    with open(args.input_file) as in_f:
        cluster_lists = load_f_lists(in_f)
    namelist = store_large(cluster_lists)

    with open(args.output_file,'w') as out_f:
        for names in namelist:
            out_f.write("%s\n" % names)

if __name__ == '__main__':
    run(get_parser().parse_args(sys.argv[1:]))
