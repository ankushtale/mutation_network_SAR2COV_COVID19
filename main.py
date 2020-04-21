from utils import read_file, translation, check_for_neutral_mutations, mutation_network
import pprint


def main():
    genome = read_file("wuhan")
    pp = pprint.PrettyPrinter(indent=4)
    polypeptide = translation(genome)
    neutral_mutations_count_per_codon = check_for_neutral_mutations(genome)

    mutation_network(amino_acid_seq = "", n_mutations=15)


if __name__ == "__main__":
    main()
