# Practical7 Task3: Codon frequency analysis and pie chart
import matplotlib.pyplot as plt

# Define input FASTA file 
input_fa = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
valid_stops = ["TAA", "TAG", "TGA"]
start_codon = "ATG"

# 1. Ask user to input a stop codon (only accept TAA/TAG/TGA)
user_stop = input("Please enter a stop codon (TAA/TAG/TGA): ").strip().upper()
if user_stop not in valid_stops:
    print("Invalid input! Only TAA, TAG, TGA are allowed.")
    exit()

# 2. Function to get upstream codons from the longest ORF for a given stop codon
def get_longest_upstream_codons(seq, target_stop):
    seq = seq.upper()
    max_codon_count = 0
    best_codons = []
    for i in range(len(seq) - 2):
        if seq[i:i+3] == start_codon:
            current_codons = []
            found = False
            for j in range(i + 3, len(seq) - 2, 3):
                codon = seq[j:j+3]
                if codon == target_stop:
                    found = True
                    break
                current_codons.append(codon)
            if found:
                if len(current_codons) > max_codon_count:
                    max_codon_count = len(current_codons)
                    best_codons = current_codons.copy()
    return best_codons

# 3. Read FASTA and collect all upstream codons
total_codons = []
with open(input_fa, "r") as f:
    gene_seq = ""
    for line in f:
        line_clean = line.rstrip()
        if line_clean.startswith(">"):
            if gene_seq:
                codons = get_longest_upstream_codons(gene_seq, user_stop)
                total_codons.extend(codons)
            gene_seq = ""
        else:
            gene_seq += line_clean
    if gene_seq:
        codons = get_longest_upstream_codons(gene_seq, user_stop)
        total_codons.extend(codons)

# 4. Count codon frequency 
codon_count = {}
for codon in total_codons:
    if codon in codon_count:
        codon_count[codon] += 1
    else:
        codon_count[codon] = 1

# 5. Print frequency results
print(f"\n=== Codon Frequency Upstream of {user_stop} ===")
total = sum(codon_count.values())
for codon, cnt in codon_count.items():
    pct = (cnt / total) * 100
    print(f"{codon}: {cnt} ({pct:.1f}%)")

# 6. Generate and save pie chart 
if codon_count:
    labels = list(codon_count.keys())
    sizes = list(codon_count.values())
    
    plt.figure(figsize=(12, 12))  # expand feature
    wedges, texts, autotexts = plt.pie(
        sizes,
        labels=labels,        
        autopct='%1.1f%%',  
        startangle=90,     
        pctdistance=0.85,   
        labeldistance=1.05,
        textprops={'fontsize': 9},  
        rotatelabels=False  # no label rotation
    )
    


    plt.title(f"Codon Frequency Upstream of Stop Codon {user_stop}", fontsize=16, pad=20)
    plt.tight_layout()  
    
    # save
    pie_file = f"codon_frequency_{user_stop}.png"
    plt.savefig(pie_file, dpi=300, bbox_inches='tight')  
    plt.close()
    print(f"\nPie chart saved to: {pie_file}")
else:
    print(f"\nNo {user_stop} found in sequences, no pie chart generated.")