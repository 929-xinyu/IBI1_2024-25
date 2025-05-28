import datetime
import re
from Bio import SeqIO

print("Script started at:", str(datetime.datetime.now()))

# Example gene counting function
def count_genes(fasta_file):
    gene_count = 0
    pattern = re.compile(r'gene:(\w+)')  # Adjust pattern as needed
    
    for record in SeqIO.parse(fasta_file, "fasta"):
        match = pattern.search(record.description)
        if match:
            gene_count += 1
    
    return gene_count

# Analyze yeast genome
print("Analyzing yeast genome...")
yeast_count = count_genes("Saccharomyces_cerevisiae.R64-1-1.cdna.fa")
print(f"Found {yeast_count} genes in yeast genome")

# Analyze human genome
print("Analyzing human genome...")
human_count = count_genes("hg38.mrna.fa")
print(f"Found {human_count} genes in human genome")

print("Script completed at:", str(datetime.datetime.now()))