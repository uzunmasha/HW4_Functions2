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
