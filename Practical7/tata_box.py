# Project Plan:
# 1. The purpose of the program is to find genes containing TATA boxes in a given FASTA file.
# 2. Read the FASTA file and extract gene names and sequences.
# 3. It will check if the sequence contains a TATA box (TATAWAW, where W is A or T).
# 4. If a TATA box is found, the program will write the gene name and sequence to a new FASTA file.
# 5. The output file will only contain genes with TATA boxes.
# 6. The program will handle file reading and writing, and ensure the input file exists.

import re

def read_fasta(file_path):
    """读取FASTA文件，返回生成器，每次产生(header, sequence)"""
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
    """从FASTA头信息中提取基因名(如YOL245C)"""
    # 假设基因名是头信息中空格分隔的第一个字段(去掉>)
    return header.split()[0][1:]

def contains_tata_box(sequence):
    """检查序列是否包含TATA盒(TATAWAW，W=A/T)"""
    # 使用正则表达式匹配TATAWAW模式
    pattern = re.compile(r'TATA[AT]A[AT]')
    return bool(pattern.search(sequence))

def process_fasta(input_file, output_file):
    """处理FASTA文件，输出含有TATA盒的基因"""
    with open(output_file, 'w') as out:
        for header, sequence in read_fasta(input_file):
            if contains_tata_box(sequence):
                gene_name = extract_gene_name(header)
                # 写入新FASTA文件，只包含基因名和序列
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