# Define the BLOSUM62 matrix
blosum62 = {
    ('A', 'A'): 4, ('A', 'R'): -1, ('A', 'N'): -2, ('A', 'D'): -2, ('A', 'C'): 0, ('A', 'Q'): -1, ('A', 'E'): -1,
    ('A', 'G'): 0, ('A', 'H'): -2, ('A', 'I'): -1, ('A', 'L'): -1, ('A', 'K'): -1, ('A', 'M'): -1, ('A', 'F'): -2,
    ('A', 'P'): -1, ('A', 'S'): 1, ('A', 'T'): 0, ('A', 'W'): -3, ('A', 'Y'): -2, ('A', 'V'): 0,
    ('R', 'A'): -1, ('R', 'R'): 5, ('R', 'N'): 0, ('R', 'D'): -2, ('R', 'C'): -3, ('R', 'Q'): 1, ('R', 'E'): 0,
    ('R', 'G'): -2, ('R', 'H'): 0, ('R', 'I'): -3, ('R', 'L'): -2, ('R', 'K'): 2, ('R', 'M'): -1, ('R', 'F'): -3,
    ('R', 'P'): -2, ('R', 'S'): -1, ('R', 'T'): -1, ('R', 'W'): -3, ('R', 'Y'): -2, ('R', 'V'): -3,
    ('N', 'A'): -2, ('N', 'R'): 0, ('N', 'N'): 6, ('N', 'D'): 1, ('N', 'C'): -3, ('N', 'Q'): 0, ('N', 'E'): 0,
    ('N', 'G'): 0, ('N', 'H'): 1, ('N', 'I'): -3, ('N', 'L'): -3, ('N', 'K'): 0, ('N', 'M'): -2, ('N', 'F'): -3,
    ('N', 'P'): -2, ('N', 'S'): 1, ('N', 'T'): 0, ('N', 'W'): -4, ('N', 'Y'): -2, ('N', 'V'): -3,
    # Add other pairs as needed
}

# Function to read sequences from a FASTA file
def read_fasta(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        sequence = ""
        for line in lines:
            if not line.startswith('>'):
                sequence += line.strip()
    return sequence

# Function to calculate alignment score using BLOSUM62
def calculate_alignment_score(seq1, seq2, blosum62):
    score = 0
    identical_count = 0
    for i in range(len(seq1)):
        aa1 = seq1[i]
        aa2 = seq2[i]
        if (aa1, aa2) in blosum62:
            score += blosum62[(aa1, aa2)]
        else:
            score += blosum62.get((aa2, aa1), 0)  # Handle symmetric pairs
        if aa1 == aa2:
            identical_count += 1
    return score, identical_count

# Function to calculate percentage identity
def calculate_percentage_identity(identical_count, length):
    return (identical_count / length) * 100

# Main function to perform sequence alignment
def main():
    # Example sequences (replace with actual sequences)
    human_sequence = "MLSRAVCGT"
    mouse_sequence = "MLCRAACST"
    random_sequence = "GCTAVRMLS"

    # Ensure sequences are of the same length
    if len(human_sequence) != len(mouse_sequence) or len(human_sequence) != len(random_sequence):
        print("Sequences are not of the same length.")
        return

    # Calculate alignment scores and percentage identities
    human_mouse_score, human_mouse_identical = calculate_alignment_score(human_sequence, mouse_sequence, blosum62)
    human_random_score, human_random_identical = calculate_alignment_score(human_sequence, random_sequence, blosum62)
    mouse_random_score, mouse_random_identical = calculate_alignment_score(mouse_sequence, random_sequence, blosum62)

    human_mouse_percentage_identity = calculate_percentage_identity(human_mouse_identical, len(human_sequence))
    human_random_percentage_identity = calculate_percentage_identity(human_random_identical, len(human_sequence))
    mouse_random_percentage_identity = calculate_percentage_identity(mouse_random_identical, len(mouse_sequence))

    # Print results
    print("Alignment Results:")
    print("Human vs Mouse:")
    print("Score:", human_mouse_score)
    print("Percentage Identity:", human_mouse_percentage_identity)
    print("Human vs Random:")
    print("Score:", human_random_score)
    print("Percentage Identity:", human_random_percentage_identity)
    print("Mouse vs Random:")
    print("Score:", mouse_random_score)
    print("Percentage Identity:", mouse_random_percentage_identity)

# Execute the main function
if __name__ == "__main__":
    main()