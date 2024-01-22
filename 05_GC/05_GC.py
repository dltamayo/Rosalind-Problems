#!/usr/bin/python
import sys
inFile = sys.argv[1]
outFile = sys.argv[2]

import pyfastx

def gc_count(fasta_file):
    """Calculate GC-content of file; return the ID of highest GC-content
    sequence and its GC-content.
    """
    fa = pyfastx.Fasta(fasta_file)
    
    # Add every sequence and its GC content to a dictionary.
    gc_dict = {}
    for seq in fa:
        gc_dict[seq.name] = seq.gc_content

    highest_gc_id = max(gc_dict, key=gc_dict.get)
    highest_gc_content = gc_dict[highest_gc_id]

    return highest_gc_id, highest_gc_content

if __name__ == '__main__':
    with open(outFile, 'w') as output_file:
        gc_id,gc_content = gc_count(inFile)

        output_line = f'{gc_id}\n{gc_content}'
        output_file.writelines(output_line)