from utils import read_file, translation
from collections import Counter
import pprint


def main():
    genome = read_file("wuhan")
    polypeptide = translation(genome)
    pp = pprint.PrettyPrinter(indent=4)
    print(genome)
    print(polypeptide)
    pp.pprint(Counter(polypeptide))


if __name__ == "__main__":
    main()
