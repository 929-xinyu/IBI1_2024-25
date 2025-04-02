# Project Plan:
# 1. The purpose of the program is to find the length of the largest possible intron in a given sequence.
# 2. The sequence is represented as a string.
# 3. Use the for loop and get through the sequence to find "GT" and "AG" sites.
# 4. Calculate the length of the intron as the distance between "GT" and "AG".
# 5. Find the length of intron between the first "GT" and the first "AG".
# 6. Output the length of the largest intron.

seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGCCTAA' # define the sequence
max_intron_length = 0 # initialize the maximum intron length

# find all the "GT" site 
for i in range(len(seq) - 1):
    if seq[i] == 'G' and seq[i+1] == 'T':
        # find all "AG" sites after the current donor site
        for j in range(i + 2, len(seq) - 1):
            if seq[j] == 'A' and seq[j+1] == 'G':
                # calculate intron length (including GT and AG)
                intron_length = j - i + 2
                # update the maximum intron length
                if intron_length > max_intron_length:
                    max_intron_length = intron_length
                # stop after finding the first AG
                break
print("The largest intron length found in the sequence is:", max_intron_length)