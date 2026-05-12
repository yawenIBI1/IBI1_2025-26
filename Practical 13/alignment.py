# alignment.py:
# Global pairwise sequence alignment without gaps
# Compatible with human/mouse/random protein sequences

def read_fasta(file_path):
    """Read FASTA file and return sequence name and pure amino acid sequence"""
    with open(file_path, "r") as f:
        lines = f.readlines()
    # The first line is the sequence header 
    seq_name = lines[0].strip().lstrip(">")
    # Concatenate subsequent sequence lines and remove newline characters
    seq = "".join([line.strip() for line in lines[1:] if not line.startswith(">")])
    return seq_name, seq

def load_blosum62(matrix_path):
    """Read BLOSUM62 matrix and convert to dictionary format {(aa1, aa2): score}"""
    blosum_dict = {}
    with open(matrix_path, "r") as f:
        # Filter out empty lines and comment lines 
        lines = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    # The first line is the amino acid list 
    aas = lines[0].split()
    # Read scoring data line by line
    for line in lines[1:]:
        parts = line.split()
        aa1 = parts[0]  # Amino acid of the current row
        scores = list(map(int, parts[1:]))  # All scores corresponding to the row
        # Store the score of each (aa1, aa2) pair into the dictionary
        for aa2, score in zip(aas, scores):
            blosum_dict[(aa1, aa2)] = score
    return blosum_dict

def pairwise_non_gapped_alignment(seq1, seq2, blosum_matrix):
    """Perform global alignment without gaps, calculate total score and identity percentage"""
    # Take the shortest length of the two sequences (compatible with inconsistent lengths)
    min_len = min(len(seq1), len(seq2))
    seq1_trimmed = seq1[:min_len]
    seq2_trimmed = seq2[:min_len]
    
    total_score = 0
    identical_count = 0  # Count the number of identical amino acids
    
    # Loop to compare amino acids at each position
    for a1, a2 in zip(seq1_trimmed, seq2_trimmed):
        # Accumulate BLOSUM62 scores
        total_score += blosum_matrix[(a1, a2)]
        # Count identical amino acids
        if a1 == a2:
            identical_count += 1
    
    # Calculate identity percentage
    identity_percent = (identical_count / min_len) * 100
    return total_score, identity_percent

if __name__ == "__main__":
    # 1. Read all input files (fully matches your filenames)
    human_name, human_seq = read_fasta("human_DLX5.fasta")
    mouse_name, mouse_seq = read_fasta("mouse_DLX5.fasta")
    random_name, random_seq = read_fasta("random_DLX5.fasta")
    blosum = load_blosum62("BLOSUM62.txt")

    # 2. Perform three sets of alignments (fully meets task requirements)
    print("="*60)
    print("          Task4: Global Pairwise Sequence Alignment Without Gaps")
    print("="*60)

    # Alignment 1: Human DLX5 vs Mouse DLX5
    print("\n--- Alignment 1: Human DLX5 vs Mouse DLX5 ---")
    score_hm, identity_hm = pairwise_non_gapped_alignment(human_seq, mouse_seq, blosum)
    print(f"Sequence 1: {human_name}")
    print(f"Sequence 2: {mouse_name}")
    print(f"BLOSUM62 Total Score: {score_hm}")
    print(f"Identity Percentage: {identity_hm:.2f}%")

    # Alignment 2: Human DLX5 vs Random Sequence
    print("\n--- Alignment 2: Human DLX5 vs Random Sequence ---")
    score_hr, identity_hr = pairwise_non_gapped_alignment(human_seq, random_seq, blosum)
    print(f"Sequence 1: {human_name}")
    print(f"Sequence 2: {random_name}")
    print(f"BLOSUM62 Total Score: {score_hr}")
    print(f"Identity Percentage: {identity_hr:.2f}%")

    # Alignment 3: Mouse DLX5 vs Random Sequence
    print("\n--- Alignment 3: Mouse DLX5 vs Random Sequence ---")
    score_mr, identity_mr = pairwise_non_gapped_alignment(mouse_seq, random_seq, blosum)
    print(f"Sequence 1: {mouse_name}")
    print(f"Sequence 2: {random_name}")
    print(f"BLOSUM62 Total Score: {score_mr}")
    print(f"Identity Percentage: {identity_mr:.2f}%")

    print("\n" + "="*60)
    print("Alignment completed! Results can be directly written into the Portfolio report")
    print("="*60)