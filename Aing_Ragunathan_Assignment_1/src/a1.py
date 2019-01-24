#!/usr/bin/python

import sys, getopt
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
import csv

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
    distribution_counter = Counter()
    total = sum(counter.values())
    total_distribution = 0;

    for char in sorted(counter):
        print (char, ': ', counter[char], '\tdistribution: ', counter[char]/total)
        total_distribution += counter[char]/total
        distribution_counter[char] += counter[char]/total

    print ('total = ', total)
    print('total distribution = ', total_distribution)

    return distribution_counter

def create_graph(counter):
    # make graph
    labels, values = zip(*sorted(counter.items()))
    indexes = np.arange(len(labels))
    width = 0.5

    plt.bar(indexes, values, width)
    plt.xticks(indexes + width * 0.5, labels)

def create_csv(plain_counter, cipher_counter, output_file):
    with open(output_file, 'w') as results:
        fieldnames = ['character', 'frequency']
        writer = csv.writer(results)
        writer.writerow(fieldnames)

        writer.writerow("Plaintext")
        for key, value in sorted(plain_counter.items()):
            writer.writerow(list(key) + [value])

        writer.writerow('Ciphertext')
        for key, value in sorted(cipher_counter.items()):
            writer.writerow(list(key) + [value])

def calc_prob(counter, char):
    total = sum(counter.values())
    return (counter[char]/total)/26

def usage():
    print ('a1.py -i <inputfile>')


def main(argv):
    plain_file = ''
    cipher_file = ''
    message = False         # mode for analyzing plaintext messages
    ciphertext = False      # mode for comparing plaintext and ciphertext

    #get input/output file names
    try:
        opts, args = getopt.getopt(argv, "hm:c:o:",["message=", "ciphertext="])
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
        elif opt in ("-o", "--output"):
            output_file = arg
        else:
            print (usage())

    # run modes accordingly
    if message == True:
        plain_counter = Counter()                 # counter to hold all dictionary data
        plain_counter = get_frequency(plain_file)  # calculate the frequencies of each character
        distribution_array = verify_distribution(plain_counter)        # verify that the distribution is 1.0

        if ciphertext == True:
            cipher_counter = Counter()
            cipher_counter = get_frequency(cipher_file)  # calculate the frequencies of each character
            verify_distribution(cipher_counter)        # verify that the distribution is 1.0
            create_csv(plain_counter, cipher_counter, output_file)           # compute the conditional probabilities of each character

    print('\nConditional Probabilities')
    print('e:', calc_prob(plain_counter, 'e'))
    print('t:', calc_prob(plain_counter, 't'))
    print('a:', calc_prob(plain_counter, 'a'))
    print('i:', calc_prob(plain_counter, 'i'))
    print('o:', calc_prob(plain_counter, 'o'))
    print('u:', calc_prob(plain_counter, 'u'))


    plt.figure(1)
    create_graph(plain_counter)               # plot data on a graph
    plt.figure(2)
    create_graph(cipher_counter)               # plot data on a graph

    plt.show()

if __name__ == "__main__":
    main(sys.argv[1:])
