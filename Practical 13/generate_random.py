# generate_random.py
import random

# 20 standard amino acid list
amino_acids = list("ACDEFGHIKLMNPQRSTVWY")
# generate equal random sequence between human/mouse（289aa）
random_protein = "".join(random.choice(amino_acids) for _ in range(289))

# save as .fasta file
with open("random_DLX5.fasta", "w") as f:
    f.write(">Random_DLX5_Control (289 aa)\n")
    f.write(random_protein)
