#!/usr/bin/python

import sys, getopt
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

def get_frequency(inputfile):
    #get character frequency from inputfile
    with open(inputfile) as f:
        counter = Counter()

        with open(inputfile) as f:
            for line in f:
                for char in line:
                    if char.isalpha() == True:
                        counter += Counter(char.strip().lower())
    return counter

def verify_distribution(counter):
    #verify distribution == 1
    total = sum(counter.values())
    total_distribution = 0;

    for char in sorted(counter):
        print (char, ': ', counter[char], '\tdistribution: ', counter[char]/total)
        total_distribution += counter[char]/total

    print ('total = ', total)
    print('total distribution = ', total_distribution)

def create_graph(counter):
    #make graph
    labels, values = zip(*sorted(counter.items()))
    indexes = np.arange(len(labels))
    width = 0.5

    plt.bar(indexes, values, width)
    plt.xticks(indexes + width * 0.5, labels)
    plt.show()


def main(argv):
    inputfile = ''

    #get input/output file names
    try:
        opts, args = getopt.getopt(argv, "hi:",["ifile="])
    except getopt.GetoptError:
        print ('a1.py -i <inputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('a1.py -i <inputfile>')
        elif opt in ("-i", "--ifile"):
            inputfile = arg

    counter = get_frequency(inputfile)
    verify_distribution(counter)
    create_graph(counter)

if __name__ == "__main__":
    main(sys.argv[1:])
