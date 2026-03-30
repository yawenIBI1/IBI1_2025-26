# Practical7 Task2: Identify genes with in-frame stop codons 
# Input and output file names 
input_fa = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_fa = "stop_genes.fa"

# Start and stop codons for DNA sequence 
start_codon = "ATG"
stop_codons = ["TAA", "TAG", "TGA"]

def check_in_frame_stop(seq):
    """Check if there is an in-frame stop codon starting with ATG,
    return (whether exists, list of stop codons)"""
    found_stops = []
    for i in range(len(seq) - 2):
        if seq[i:i+3] == start_codon:
            # Read in triplets starting from ATG
            for j in range(i + 3, len(seq) - 2, 3):
                codon = seq[j:j+3]
                if codon in stop_codons:
                    found_stops.append(codon)
    # Remove duplicates and sort the list
    unique_stops = sorted(list(set(found_stops)))
    return len(unique_stops) > 0, unique_stops

# Read FASTA file and write new file 
with open(input_fa, "r") as f_in, open(output_fa, "w") as f_out:
    gene_header = ""
    gene_seq = ""
    for line in f_in:
        # remove trailing whitespaces and newlines
        line_clean = line.rstrip()
        if line_clean.startswith(">"):
            # Process the previous gene
            if gene_seq:
                has_stop, stops = check_in_frame_stop(gene_seq)
                if has_stop:
                    # Extract gene name (only keep the first word after >)
                    gene_name = gene_header.split()[0][1:]
                    stop_str = "-".join(stops)
                    f_out.write(f">{gene_name} {stop_str}\n")
                    f_out.write(f"{gene_seq}\n")
            # Start processing a new gene
            gene_header = line_clean
            gene_seq = ""
        else:
            # Concatenate multi-line sequence
            gene_seq += line_clean
    # Process the last gene in the file to avoid missing it
    if gene_seq:
        has_stop, stops = check_in_frame_stop(gene_seq)
        if has_stop:
            gene_name = gene_header.split()[0][1:]
            stop_str = "-".join(stops)
            f_out.write(f">{gene_name} {stop_str}\n")
            f_out.write(f"{gene_seq}\n")

print("Task2 finished! Output file: stop_genes.fa")