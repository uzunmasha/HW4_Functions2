def protein_mass(seq: str):
    """

    Calculate the mass (Da) of a protein based on its amino acids sequence.
    Takes a string of amino acids, returns the molecular weight in Da.
    Amino acids in the string should be indicated as one-letter symbols.

    """
    aa_seq = list(seq)
    mass_dictionary = dict({'A': 89, 'R': 174, 'N': 132, 'D': 133, 'C': 121, 'Q': 146, 'E': 147, 'Z': 147,
                            'G': 75, 'H': 155, 'I': 131, 'L': 131, 'K': 146, 'M': 149, 'F': 165, 'P': 115, 'S': 105,
                            'T': 119, 'W': 204, 'Y': 181, 'V': 117})
    mass = 0
    for aa in aa_seq:
        mass += mass_dictionary[aa]

    return mass
