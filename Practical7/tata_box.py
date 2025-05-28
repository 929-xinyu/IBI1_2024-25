# Project Plan:
# 1. The purpose of the program is to find genes containing TATA boxes in a given FASTA file.
# 2. Read the FASTA file and extract gene names and sequences.
# 3. It will check if the sequence contains a TATA box (TATAWAW, where W is A or T).
# 4. If a TATA box is found, the program will write the gene name and sequence to a new FASTA file.
# 5. The output file will only contain genes with TATA boxes.
# 6. The program will handle file reading and writing, and ensure the input file exists.

# Import necessary libraries
import re

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
    """Extract gene name (e.g., YOL245C) from FASTA header"""
    # Assumes gene name is the first whitespace-separated field (after '>')
    return header.split()[0][1:]

def contains_tata_box(sequence):
    """Check if sequence contains a TATA box (TATAWAW, where W=A/T)"""
    # Use regex to match TATAWAW pattern
    pattern = re.compile(r'TATA[AT]A[AT]')
    return bool(pattern.search(sequence))

def process_fasta(input_file, output_file):
    """Process FASTA file and output genes containing TATA boxes"""
    with open(output_file, 'w') as out:
        for header, sequence in read_fasta(input_file):
            if contains_tata_box(sequence):
                gene_name = extract_gene_name(header)
                # Write to new FASTA file with only gene name and sequence
                out.write(f'>{gene_name}\n{sequence}\n')

# Main program
if __name__ == "__main__":
    input_fasta = "c:/Users/HUAWEI/Desktop/IBI/IBI1_2024-25/Practical7/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa.txt"
    output_fasta = "tata_genes.fa"

    import os
    if not os.path.exists(input_fasta):
        print(f"Error: The file '{input_fasta}' does not exist.")
    else:
        process_fasta(input_fasta, output_fasta)
        print(f"Processing complete. Results saved to {output_fasta}")