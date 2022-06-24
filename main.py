from generator import Generator 
from sbh import sbhAlgorithm
from analysis import Analysis
import sys

def main(sequence_length: int = 209, nucleotide_length: int = 10, n_remove: int = 0, n_insert: int = 0, n_duplicate: int = 0, filename: str = 'nucleotides_with_errors.txt', algorithm: str = 'antColonySearchSW'):
    generator = Generator(sequence_length, nucleotide_length, n_remove, n_insert, n_duplicate)
    generator.main()

    sbh = sbhAlgorithm(sequence_length, filename, algorithm)
    sbh.main()

    analysis = Analysis(generator.sequence, sbh.result)
    analysis.analyze()
    analysis.print_results()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        sequence_length = int(sys.argv[1])
        nucleotide_length = int(sys.argv[2])
        n_remove = int(sys.argv[3])
        n_insert = int(sys.argv[4])
        n_duplicate = int(sys.argv[5])
        filename = sys.argv[6]
        algorithm = sys.argv[7]
    else:
        sequence_length = 400
        nucleotide_length = 10
        n_remove = 100
        n_insert = 100
        n_duplicate = 0
        filename = 'nucleotides_with_errors.txt'
        algorithm = 'antColonySearchSW'

    main(sequence_length, nucleotide_length, n_remove, n_insert, n_duplicate, filename, algorithm)