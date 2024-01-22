#!/usr/bin/python
import sys
inFile = sys.argv[1]
outFile = sys.argv[2]

def translate_protein(sequence):
    """Translates input RNA sequence into protein.
    """
    codon_table = {
        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 'UGU': 'C', 'UGC': 'C',
        'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 'UUU': 'F', 'UUC': 'F',
        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G', 'CAU': 'H', 'CAC': 'H',
        'AUA': 'I', 'AUU': 'I', 'AUC': 'I', 'AAA': 'K', 'AAG': 'K', 'UUA': 'L', 
        'UUG': 'L', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L', 'AUG': 'M',
        'AAU': 'N', 'AAC': 'N', 'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'CAA': 'Q', 'CAG': 'Q', 'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AGA': 'R', 'AGG': 'R', 'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
        'AGU': 'S', 'AGC': 'S', 'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V', 'UGG': 'W', 'UAU': 'Y',
        'UAC': 'Y', 'UAA': '*', 'UAG': '*', 'UGA': '*'
    }

    # Generator yields RNA codon every three base pairs.
    def RNA_to_codon(sequence):
        while True:
            try:
                base_1, base_2, base_3 = sequence[0], sequence[1], sequence[2]
                sequence = sequence[3:]
            except IndexError:
                return
            yield base_1, base_2, base_3
    
    # Translate RNA codon to amino acid using codon_table and append to protein.
    protein = ''
    for base_1, base_2, base_3 in RNA_to_codon(sequence):
        protein += codon_table[base_1 + base_2 + base_3]
    
    # Return protein without stop codon
    return protein[:-1]

if __name__ == '__main__':
    with open(inFile, 'r') as input_file, open(outFile, 'w') as output_file:
        input = input_file.read()
        output_file.writelines(translate_protein(input))