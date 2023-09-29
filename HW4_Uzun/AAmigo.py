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

def aa_profile(seq: str):
    """

     Displays the proportion of hydrophobic, polar, negatively and positively charged amino acids in the protein.
     Takes a string of amino acids, returns a dictionary.
     Amino acids in the string should be indicated as one-letter symbols.

    """
    aa_seq = list(seq)
    aa_biochemistry = dict(
        {'hydrophobic': ['G', 'A', 'V', 'L', 'I', 'P', 'F', 'M', 'W'], 'polar': ['S', 'T', 'C', 'N', 'Q', 'Y'],
         '- charged': ['E', 'D'], '+ charged': ['K', 'H', 'R']})
    profile = dict({'hydrophobic': 0, 'polar': 0, '- charged': 0, '+ charged': 0})

    for aa in aa_seq:
        for group_name, group_list in aa_biochemistry.items():
            if aa in group_list:
                profile[group_name] += 1

    for group, count in profile.items():
        profile[group] = round((count/len(seq)), 2)
    return profile
