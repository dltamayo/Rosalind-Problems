#!/usr/bin/python
import sys
inFile = sys.argv[1]
outFile = sys.argv[2]

def dominant_probability(k,m,n):
    """From population containing k homozygous dominant, m heterozygous, and
    n homozygous recessive genotypes, calculate probability that two randomly
    selected mating organisms will produce an individual with a dominant allele.
    """
    pop = k + m + n
    total_recessive = (.25 * (m**2 - m) + n * m + (n**2 - n))/(pop*(pop-1))

    return 1 - (total_recessive)

if __name__ == '__main__':
    with open(inFile, 'r') as input_file, open(outFile, 'w') as output_file:
        # input = input_file.read()
        
        input_list = [int(x) for x in input_file.read().split(' ')]
        k,m,n = input_list[0],input_list[1],input_list[2]

        output_file.writelines(str(dominant_probability(k,m,n)))