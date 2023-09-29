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