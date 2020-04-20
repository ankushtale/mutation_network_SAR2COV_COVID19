from utils import read_file, translation, check_for_neutral_mutations
from collections import Counter
import pprint


def main():
    genome = read_file("wuhan")
    polypeptide = translation(genome)
    pp = pprint.PrettyPrinter(indent=4)
    # print(genome)
    # print(polypeptide)
    # pp.pprint(Counter(polypeptide))
    pp.pprint(check_for_neutral_mutations(genome))


if __name__ == "__main__":
    main()
