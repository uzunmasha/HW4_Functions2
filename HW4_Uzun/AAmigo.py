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