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


def aa_substring(seq: str):
    """

    Searches for a substring of amino acids in the entire amino acid sequence.
    Takes a string of amino acids and a substring, which should be found.
    Returns the position where the searched one was found for the first time.
    Amino acids in the string should be indicated as one-letter symbols.

    """
    aa_seq = list(seq)
    aa_seq_upper = []
    for sequences in aa_seq:
        upper_case = sequences.upper()
        aa_seq_upper.append(upper_case)
    amino_acids = aa_seq_upper[:-1]
    substring = aa_seq_upper[-1]
    results = []
    for sequences in amino_acids:
        subst = sequences.find(substring)
        results.append(subst)
    return results


def aa_count(seq: str):
    """

    Finds how many times a particular sequence(s) occurs in the original one.
    Takes a string of amino acids and a substring, which should be counted.
    Returns the count of searched amino acids.
    Amino acids in the string should be indicated as one-letter symbols.

    """
    aa_seq = list(seq)
    aa_seq_upper = []
    for sequences in aa_seq:
        upper_case = sequences.upper()
        aa_seq_upper.append(upper_case)
    amino_acids = aa_seq_upper[:-1]
    substring = aa_seq_upper[-1]
    results = []
    for sequences in amino_acids:
        amino_acid_count = sequences.count(substring)
        results.append(amino_acid_count)
    return results

def protein_length(*seqs: str):
    """

    Calculate the length (number of amino acids) of a protein.
    Takes a string of amino acids, returns the number.
    Amino acids in the string should be indicated as one-letter symbols.

    """
    lengths = []

    for seq in seqs:
        lengths.append(len(seq))

    return lengths


    def essential_amino_acids(*seqs: str):
    """

    Calculate the number of essential amino acids based on its amino acids sequence.
    Takes a string of amino acids, returns only the essential amino acids.
    Amino acids in the string should be indicated as one-letter symbols.

    """
    eaa_dictionary = ['H', 'I', 'K', 'L', 'M', 'F', 'T', 'W', 'V', 'h', 'i', 'k', 'l', 'm', 'f', 't', 'w', 'v']
    eaa_list = []

    for seq in seqs:
        eaa_seq = []
        for amino_acid in seq:
            if amino_acid in eaa_dictionary:
                eaa_seq.append(amino_acid)
        eaa_list.append(eaa_seq)

    return eaa_list


def aa_tools(*args):
    """

    Main function for amino acid sequences processing.
    Parameters: *args (str) - amino acid sequences and operation.
    Returns: List of results or None if non-amino acid chars found.

    """
    seq = args[:-1]
    operation = args[-1]
    non_aa_chars = set('BJOUXbjoux')
    contains_non_aa = False

    for sequence in seq:
        contains_non_aa = False
        for amino_acid in sequence:
            if amino_acid in non_aa_chars:
                contains_non_aa = True
                break
        if contains_non_aa:
            break
    if contains_non_aa:
        return None

    results = []

    for sequence in seq:
        if operation == "protein_mass":
            result = protein_mass(sequence)
            results.append(result)

        elif operation == "aa_profile":
            result = aa_profile(sequence)
            results.append(result)

        if operation == "aa_substring":
            result = aa_substring(seq)
            return result

        if operation == "aa_count":
            result = aa_count(seq)
            return result

        if operation == "protein_length":
            result = protein_length(sequence)
            results.append(result)

        if operation == "essential_amino_acids":
            result = essential_amino_acids(sequence)
            results.append(result)

    return results


aa_tools()

