Add your code here
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