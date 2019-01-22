#!/usr/bin/python

import sys, getopt
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

def get_frequency(inputfile):
    # get character frequency from inputfile
    with open(inputfile) as f:
        counter = Counter()

        with open(inputfile) as f:
            for line in f:
                for char in line:
                    if char.isalpha() == True:
                        counter += Counter(char.strip().lower())
    return counter

def verify_distribution(counter):
    # verify distribution == 1
    total = sum(counter.values())
    total_distribution = 0;

    for char in sorted(counter):
        print (char, ': ', counter[char], '\tdistribution: ', counter[char]/total)
        total_distribution += counter[char]/total

    print ('total = ', total)
    print('total distribution = ', total_distribution)

def create_graph(counter):
    # make graph
    labels, values = zip(*sorted(counter.items()))
    indexes = np.arange(len(labels))
    width = 0.5

    plt.bar(indexes, values, width)
    plt.xticks(indexes + width * 0.5, labels)
    plt.show()

def compute_probability(plain_counter, cipher_counter):
    matrix = np.matrix()

    # key == number of shifts in the caeser cipher
    for key in range(0,26):
        for char in sorted(cipher_counter):
            matrix[key, char] = 1
            # find P(C=x), the probability of a ciphertext == x
            cipher_probability = plain_counter[char] * key

    print (matrix)
    return

def usage():
    print ('a1.py -i <inputfile>')


def main(argv):
    plain_file = ''
    cipher_file = ''
    message = False         # mode for analyzing plaintext messages
    ciphertext = False      # mode for comparing plaintext and ciphertext

    #get input/output file names
    try:
        opts, args = getopt.getopt(argv, "hm:c:",["message=", "ciphertext="])
    except getopt.GetoptError:
        print (usage())
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print (usage())
        elif opt in ("-m", "--message"):
            message = True
            plain_file = arg                     # user specified file for input
        elif opt in ("-c", "--ciphertext"):
            ciphertext = True
            cipher_file = arg                     # user specified file for input
        else:
            print (usage())

    # run modes accordingly
    if message == True:
        plain_counter = Counter()                 # counter to hold all dictionary data
        plain_counter = get_frequency(plain_file)  # calculate the frequencies of each character
        verify_distribution(plain_counter)        # verify that the distribution is 1.0

        if ciphertext == True:
            cipher_counter = Counter()
            cipher_counter = get_frequency(cipher_file)  # calculate the frequencies of each character
            verify_distribution(cipher_counter)        # verify that the distribution is 1.0
            compute_probability(plain_counter, cipher_counter)           # compute the conditional probabilities of each character

        #create_graph(counter)               # plot data on a graph


if __name__ == "__main__":
    main(sys.argv[1:])
