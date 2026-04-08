def calculate_protein_mass(amino_acid_seq):
    """
    Calculate the total monoisotopic mass of a protein in atomic mass units (amu)
    based on its one-letter amino acid sequence.
    
    Args:
        amino_acid_seq (str): String of one-letter amino acid codes.
        
    Returns:
        float: Total mass of the protein in amu, rounded to 2 decimal places. 
        
    Raises:
        ValueError: If any character in the sequence is not a valid standard amino acid.
    """
    # Monoisotopic residue mass table (one-letter code: mass in amu)
    aa_mass = {
        'G': 57.02,  # Glycine
        'A': 71.04,  # Alanine
        'S': 87.03,  # Serine
        'P': 97.05,  # Proline
        'V': 99.07,  # Valine
        'T': 101.05, # Threonine
        'C': 103.01, # Cysteine
        'I': 113.08, # Isoleucine
        'L': 113.08, # Leucine
        'N': 114.04, # Asparagine
        'D': 115.03, # Aspartic Acid
        'Q': 128.06, # Glutamine
        'K': 128.09, # Lysine
        'E': 129.04, # Glutamic Acid
        'M': 131.04, # Methionine
        'H': 137.06, # Histidine
        'F': 147.07, # Phenylalanine
        'R': 156.10, # Arginine
        'Y': 163.06, # Tyrosine
        'W': 186.08  # Tryptophan
    }

    total_mass = 0.0
    # Convert input to uppercase for robustness (supports lowercase input)
    seq_upper = amino_acid_seq.upper()

    # Validate each amino acid and accumulate mass
    for aa in seq_upper:
        if aa not in aa_mass:
            raise ValueError(
                f"Invalid amino acid '{aa}' detected. Only standard 20 amino acids "
                "(G, A, S, P, V, T, C, I, L, N, D, Q, K, E, M, H, F, R, Y, W) are allowed."
            )
        total_mass += aa_mass[aa]

    # Return mass rounded to 2 decimal places
    return round(total_mass, 2)


if __name__ == "__main__":
    # Example 1: Test valid sequence "GASVV"
    test_seq_1 = "GASVV"
    mass_1 = calculate_protein_mass(test_seq_1)
    print(f"Sequence: {test_seq_1}")
    print(f"Total protein mass: {mass_1} amu\n")  # Expected output: 413.23 amu

    # Example 2: Test another valid sequence "MALW"
    test_seq_2 = "MALW"
    mass_2 = calculate_protein_mass(test_seq_2)
    print(f"Sequence: {test_seq_2}")
    print(f"Total protein mass: {mass_2} amu\n")  # Expected output: 501.24 amu

    # Example 3: Test error handling (uncomment to run)
    test_seq_3 = "GAXVV"  # Contains invalid amino acid 'X'
    mass_3 = calculate_protein_mass(test_seq_3)
    print(f"Sequence: {test_seq_3}")
    print(f"Total protein mass: {mass_3} amu")
