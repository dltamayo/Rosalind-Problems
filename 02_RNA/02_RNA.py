#!/usr/bin/python
import sys
inFile = sys.argv[1]
outFile = sys.argv[2]

def transcribe_dna(sequence):
    """Translate T characters in input sequence into U.
    """
    output = sequence.translate(str.maketrans('T', 'U'))
    return output

if __name__ == '__main__':
    with open(inFile, 'r') as input_file, open(outFile, 'w') as output_file:
        sequence = input_file.read()
        output = transcribe_dna(sequence)
        output_file.writelines(output)