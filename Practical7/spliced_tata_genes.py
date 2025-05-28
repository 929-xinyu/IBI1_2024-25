# Project Plan:
# 1. The purpose of the program is to find genes that contain both a TATA box and a specific splice site in a given FASTA file.
# 2. The program reads a FASTA file, extracts gene names and sequences, and checks for the presence of a TATA box and a specified splice site.
# 3. If a gene contains at least one TATA box and the specified splice site, it is added to the results.
# 4. The program counts the number of TATA boxes in each gene and outputs the results to the console.

# Import necessary libraries
import re
import sys

def read_fasta(file_path):
    """Read a FASTA file and yield (header, sequence) tuples"""
    with open(file_path, 'r') as file:
        header = ''
        sequence = []
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if header:
                    yield (header, ''.join(sequence))
                header = line
                sequence = []
            else:
                sequence.append(line)
        if header:
            yield (header, ''.join(sequence))

def extract_gene_name(header):
    """Extract gene name from FASTA header"""
    return header.split()[0][1:]

def contains_splice_site(sequence, splice_site):
    """Check if sequence contains the specified splice site motif"""
    return splice_site in sequence

def count_tata_boxes(sequence):
    """Count the number of TATA boxes in the sequence"""
    pattern = re.compile(r'TATA[AT]A[AT]')
    return len(pattern.findall(sequence))

def process_genes(input_file, splice_site):
    """Process gene data and return a list of qualifying genes"""
    valid_genes = []
    for header, sequence in read_fasta(input_file):
        gene_name = extract_gene_name(header)
        tata_count = count_tata_boxes(sequence)
        
        if tata_count > 0 and contains_splice_site(sequence, splice_site):
            valid_genes.append((gene_name, sequence, tata_count))