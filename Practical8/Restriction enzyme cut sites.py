# Project Plan:
# 1. The purpose of this code is to find the restriction sites in a DNA sequence based on a given recognition sequence.
# 2. Define a function that takes the DNA sequence and recognition sequence as input parameters.
# 3. Check if the input sequences are valid (only contain A, C, G, T).
# 4. Find all the restriction sites in the DNA sequence and return their positions (1-based index).
# 5. Test the function with sample data to ensure it works as expected.

def find_restriction_sites(dna_sequence, recognition_sequence): #define the function and input the parameter
    # check if the input sequences are valid
    if not set(dna_sequence).issubset('ACGT') or not set(recognition_sequence).issubset('ACGT'):
        raise ValueError("the sequence must conclude the standard 'ACGT'") # if the input sequences are not valid, raise an error

    # find all the restriction sites in the DNA sequence
    sites = []
    recognition_length = len(recognition_sequence)
    for i in range(len(dna_sequence) - recognition_length + 1):
        if dna_sequence[i:i + recognition_length] == recognition_sequence:
            sites.append(i + 1)  # return 1-based index

    return sites 

# the example I give is to use it to test the code.
dna_seq = "ACGTACGTACGTACGTACGTACGTACGTACGT"
recognition_seq = "ACGT"
try:
    sites = find_restriction_sites(dna_seq, recognition_seq)
    print("cutting site:", sites)
except ValueError as e:
    print(e)