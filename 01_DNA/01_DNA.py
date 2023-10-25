#!/usr/bin/python
import sys
inFile = sys.argv[1]
outFile = sys.argv[2]

def sequence_count(sequence):
    """Count the number of occurrences of A, C, G, T in the input sequence.
    
    input: string, a DNA sequence
    """
    A,C,G,T = sequence.count('A'), sequence.count('C'), sequence.count('G'), sequence.count('T')
    return f'{A} {C} {G} {T}'

if __name__ == '__main__':
    with open(inFile, 'r') as input_file, open(outFile, 'w') as output_file:
        sequence = input_file.read()
        output = sequence_count(sequence)
        output_file.writelines(output)