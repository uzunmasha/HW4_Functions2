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
#print(protein_mass('MARY'))

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


#print(aa_profile('EEKFG', 'EEKFG'))

def aa_substring(*seq: str):
    """
    
    Searches for a substring of amino acids in the entire amino acid sequence.
    Takes a string of amino acids and a substring, which should be found.
    Returns the position in the original sequence where the searched one was found for the first time.
    Amino acids in the string should be indicated as one-letter symbols.

    """
    aa_seq = list(seq)
    aa_seq_upper = []
    for sequences in aa_seq:
        up = sequences.upper()
        aa_seq_upper.append(up)
    amino_acids = aa_seq_upper[:-1]
    substring = aa_seq_upper[-1]
    results = []
    for sequences in amino_acids:
        subst = sequences.find(substring)
        results.append(subst)
    return results
#aa_substring('RNDCEQEZGHeILKMFPESTWYa', 'A')

def aa_count(*seq: str):
    """
    
    Finds how many times a particular amino acid or sequence of several amino acids occurs in the original sequence.
    Takes a string of amino acids and a substring, which should be counted.
    Returns the count of searched amino acids.
    Amino acids in the string should be indicated as one-letter symbols.

    """
    aa_seq = list(seq)
    aa_seq_upper = []
    for sequences in aa_seq:
        up = sequences.upper()
        aa_seq_upper.append(up)
    amino_acids = aa_seq_upper[:-1]
    substring = aa_seq_upper[-1]
    results = []
    for sequences in amino_acids:
        aa_count = sequences.count(substring)
        results.append(aa_count)  
    return results
#aa_count('ARNDCQEeEZGHILKMFPSTWY','NDCQZGHILKMFPS','HI')

def aa_tools(*args):
    seq = args[:-1]
    operation = args[-1]
    non_aa_chars = set('BJOUXbjoux')
    contains_non_aa = False
    for sequence in seq:
        contains_non_aa = False
        for aa in sequence:
            if aa in non_aa_chars:
                contains_non_aa = True
                break
        if contains_non_aa:
            break
    if contains_non_aa:
        return None

    if operation == "protein_mass":
        protein_mass_result = protein_mass(*seq)
        return protein_mass_result
    
    if operation == "aa_profile":
        aa_profile_result = aa_profile(*seq)
        return aa_profile_result

    if operation == "aa_substring":
        aa_substring_result = aa_substring(*seq)
        return aa_substring_result

    if operation == "aa_count":
        aa_count_result = aa_count(*seq)
        return aa_count_result
aa_tools(*args))