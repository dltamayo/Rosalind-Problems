#!/usr/bin/python
import sys
inFile = sys.argv[1]
outFile = sys.argv[2]

def hamming_dist(sequence_s, sequence_t):
    """Compare two input sequences and calculate the number of point
    mutations.
    """
    seq_comparison = zip(sequence_s, sequence_t)
    hamm_distance = 0

    # Compare each character between the two sequences.
    # If they differ, increase Hamming distance by 1.
    for i,j in seq_comparison:
        if i != j:
            hamm_distance += 1
    
    return hamm_distance

if __name__ == '__main__':
    with open(inFile, 'r') as input_file, open(outFile, 'w') as output_file:
        input = input_file.read()
        
        input_list = [sequence for sequence in input.split('\n')]
        s,t = input_list[0],input_list[1]

        output_file.writelines(str(hamming_dist(s,t)))