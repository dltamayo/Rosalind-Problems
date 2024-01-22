#!/usr/bin/python
import sys
inFile = sys.argv[1]
outFile = sys.argv[2]

import regex as re

def find_motif(sequence, motif):
    """Return locations of motif as a substring of input sequence.
    """
    result = re.finditer(motif,sequence, overlapped=True)
    matches = []

    for match in result:
        start = match.span()[0]
        matches.append(str(start + 1))
    
    return ' '.join(matches)

if __name__ == '__main__':
    with open(inFile, 'r') as input_file, open(outFile, 'w') as output_file:
        input = input_file.read()
        
        input_list = [x for x in input.split('\n')]
        sequence,motif = input_list[0],input_list[1]

        output_file.writelines(find_motif(sequence, motif))