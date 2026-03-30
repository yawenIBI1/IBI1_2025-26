# Practical7 Task1: Find the largest ORF 
seq = 'AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG'
# define stop codons（mRNA）
stop_codons = ['UAA', 'UAG', 'UGA']
# initiate two variables
longest_orf_seq = ""
max_orf_length = 0

# Range len(seq)-2: Ensure slicing 3 characters without out-of-bounds error
for start_idx in range(len(seq) - 2):
    # check if it is AUG
    if seq[start_idx:start_idx+3] == 'AUG':
        # Find the first stop codon in triplets after AUG 
        for stop_idx in range(start_idx + 3, len(seq) - 2, 3):
            current_codon = seq[stop_idx:stop_idx+3]
            if current_codon in stop_codons:
                # Calculate current ORF length: include start and stop codons(stop position needs +3)
                current_orf_length = stop_idx + 3 - start_idx
                current_orf_seq = seq[start_idx:stop_idx+3]
                # Compare and update the longest ORF
                if current_orf_length > max_orf_length:
                    max_orf_length = current_orf_length
                    longest_orf_seq = current_orf_seq
                # Stop when the first stop codon is found
                break

print("=== Longest Open Reading Frame (ORF) ===")
print(f"Longest ORF sequence: {longest_orf_seq}")
print(f"Length of longest ORF (nucleotides): {max_orf_length}")