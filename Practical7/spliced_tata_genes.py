import re
import sys

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
    """从FASTA头信息中提取基因名"""
    return header.split()[0][1:]

def contains_splice_site(sequence, splice_site):
    """检查序列是否包含指定的剪接位点组合"""
    return splice_site in sequence

def count_tata_boxes(sequence):
    """统计序列中TATA盒的数量"""
    pattern = re.compile(r'TATA[AT]A[AT]')
    return len(pattern.findall(sequence))

def process_genes(input_file, splice_site):
    """处理基因数据，返回符合条件的基因列表"""
    valid_genes = []
    for header, sequence in read_fasta(input_file):
        gene_name = extract_gene_name(header)
        tata_count = count_tata_boxes(sequence)
        
        if tata_count > 0 and contains_splice_site(sequence, splice_site):
            valid_genes.append((gene_name, sequence, tata_count))
 