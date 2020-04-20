available_genome_sequences = ["wuhan", "phillippines"]
codon_wheel = {
    "TTT": "F",
    "TTC": "F",
    "TTA": "L",
    "TTG": "L",
    "TCT": "S",
    "TCC": "S",
    "TCA": "S",
    "TCG": "S",
    "TAT": "Y",
    "TAC": "Y",
    "TAA": ">",
    "TAG": ">",
    "TGT": "C",
    "TGC": "C",
    "TGA": ">",
    "TGG": "W",
    "CTT": "L",
    "CTC": "L",
    "CTA": "L",
    "CTG": "L",
    "CCT": "P",
    "CCC": "P",
    "CCA": "P",
    "CCG": "P",
    "CAT": "H",
    "CAC": "H",
    "CAA": "Q",
    "CAG": "Q",
    "CGT": "R",
    "CGC": "R",
    "CGA": "R",
    "CGG": "R",
    "ATT": "I",
    "ATC": "I",
    "ATA": "I",
    "ATG": "<",
    "ACT": "T",
    "ACC": "T",
    "ACA": "T",
    "ACG": "T",
    "AAT": "N",
    "AAC": "N",
    "AAA": "K",
    "AAG": "K",
    "AGT": "S",
    "AGC": "S",
    "AGA": "R",
    "AGG": "R",
    "GTT": "V",
    "GTC": "V",
    "GTA": "V",
    "GTG": "V",
    "GCT": "A",
    "GCC": "A",
    "GCA": "A",
    "GCG": "A",
    "GAT": "D",
    "GAC": "D",
    "GAA": "E",
    "GAG": "E",
    "GGT": "G",
    "GGC": "G",
    "GGA": "G",
    "GGG": "G",
}


def read_file(file_id):
    if file_id in available_genome_sequences:
        gen_seq_file = open("data/sars_2_virus_" + file_id + "_genome_sequence.txt", "r")

    gen_seq_data = ""
    for line in gen_seq_file:
        gen_seq_data += line.replace(" ", "").rstrip()

    gen_seq_file.close()

    return gen_seq_data


def translation(genome):
    codon = ""
    polypeptide = ""

    for nucleotide in genome:
        if len(codon) < 3:
            codon += nucleotide.upper()
        else:
            polypeptide += codon_wheel.get(codon, "?")
            codon = nucleotide.upper()


    # ignore the remaining incomplete codon
    # polypeptide += codon

    return polypeptide
