import itertools
import matplotlib.pylab as plt
from math import log
available_genome_sequences = ["wuhan", "philippines"]
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
    else:
        return None
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


def get_mutation_list(codon):
    all_bases = ['A', 'C', 'G', 'T']
    mutation_list = []

    first_position_complement_list = [x for x in all_bases if x != codon[0]]
    second_position_complement_list = [x for x in all_bases if x != codon[1]]
    third_position_complement_list = [x for x in all_bases if x != codon[2]]

    mutation_list.append(codon[:2] + third_position_complement_list[0])
    mutation_list.append(codon[:2] + third_position_complement_list[1])
    mutation_list.append(codon[:2] + third_position_complement_list[2])

    mutation_list.append(codon[0] + second_position_complement_list[0] + codon[2])
    mutation_list.append(codon[0] + second_position_complement_list[1] + codon[2])
    mutation_list.append(codon[0] + second_position_complement_list[2] + codon[2])

    mutation_list.append(first_position_complement_list[0] + codon[1:])
    mutation_list.append(first_position_complement_list[1] + codon[1:])
    mutation_list.append(first_position_complement_list[2] + codon[1:])

    return mutation_list


def calculate_neutral_mutations(codon):
    neutral_count = 0
    single_mutations = get_mutation_list(codon)

    for mutation in single_mutations:
        if codon_wheel[mutation] == codon_wheel[codon]:
            neutral_count += 1

    return neutral_count

def calculate_non_neutral_mutations_with_mutated_codons(codon):
    neutral_count = 0
    mutated_codons=[]
    single_mutations = get_mutation_list(codon)

    for mutation in single_mutations:
        if codon_wheel[mutation] != codon_wheel[codon]:
            neutral_count += 1
            mutated_codons.append(mutation)

    return neutral_count,mutated_codons

def calculate_non_neutral_mutations(codon):
    non_neutral_count = 0
    single_mutations = get_mutation_list(codon)

    for mutation in single_mutations:
        if codon_wheel[mutation] != codon_wheel[codon]:
            non_neutral_count += 1

    return non_neutral_count

def check_for_neutral_mutations(genome):
    codon = ""
    amino_acid_sequence = {}

    for nucleotide in genome:
        if len(codon) < 3:
            codon += nucleotide.upper()
        else:
            neutral_mutations = calculate_neutral_mutations(codon)
            amino_acid_sequence[codon] = neutral_mutations
            codon = nucleotide.upper()

    x, y = zip(*sorted(amino_acid_sequence.items()))
    plt.plot(x, y)
    plt.xticks(x, x, rotation='vertical')
    plt.savefig("plots/neutral_amino_acid_count_per_codon.jpg")
    plt.show()


    return amino_acid_sequence


def mutation_network(amino_acid_seq, n_mutations):
    if n_mutations is None:
        n_mutations = 0

    for codon in amino_acid_seq:
        pass

def spike_protein_mutations(genome):
    codon = ""

    #for only one mutation
    no_of_sequecnces_one_mutation_away = 0
    for nucleotide in genome:
        if len(codon) < 3:
            codon += nucleotide.upper()
        else:
            non_neutral_mutations = calculate_non_neutral_mutations(codon)
            print(non_neutral_mutations)
            no_of_sequecnces_one_mutation_away = no_of_sequecnces_one_mutation_away + non_neutral_mutations
            codon = nucleotide.upper()

    #for 2-15 mutations away
    final = [no_of_sequecnces_one_mutation_away]
    codon=""
    x=[1]
    for i in range(1,4):
        possible_sequences = [genome]
        i += 1
        x.append(i)
        print("checking possibilities for ", i , " mutations away ")
        for _ in range(0,i):
            temp=[]

            for sequence in possible_sequences:
                for nucleotide_index in range(0,len(sequence)):
                    # temp_seq=sequence
                    if len(codon) < 3:
                        codon += sequence[nucleotide_index].upper()
                    else:
                        non_neutral_mutations,mutated_codons = calculate_non_neutral_mutations_with_mutated_codons(codon)
                        # no_of_sequecnces_one_mutation_away = no_of_sequecnces_one_mutation_away + non_neutral_mutations
                        codon = sequence[nucleotide_index].upper()
                        for new_codon in mutated_codons:
                            # temp_seq = sequence
                            # temp_seq[nucleotide_index-3] = new_codon[0]
                            # temp_seq[nucleotide_index - 2] = new_codon[1]
                            # temp_seq[nucleotide_index - 1] = new_codon[2]
                            temp.append(sequence[:nucleotide_index-3] + codon + sequence[nucleotide_index:])
            possible_sequences=temp

        final.append(len(possible_sequences))
    # y = [log(y, 10) for y in final]
    # print(y)
    # plt.plot(x, y)
    # plt.xticks(x, x, rotation='vertical')
    # plt.savefig("plots/neutral_amino_acid_count_per_codon.jpg")
    # plt.show()


    return final
