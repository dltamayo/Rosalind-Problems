#!/usr/bin/python
import sys
inFile = sys.argv[1]
outFile = sys.argv[2]

def sequence_count(sequence):
    '''
    input: string, a DNA sequence
    output: a string containing four integers (separated by spaces) 
    counting the respective number of times that 'A', 'C', 'G', and 'T' occur in sequence
    '''
    output = ('%d %d %d %d' 
              % (sequence.count('A'), sequence.count('C'), 
                 sequence.count('G'), sequence.count('T')))
    return output

if __name__ == '__main__':
    with open(inFile, 'r') as input_file, open(outFile, 'w') as output_file:
        sequence = input_file.read()
        output_file.writelines(sequence_count(sequence))