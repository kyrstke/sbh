from generator import Generator 
from sbh import sbh_algorithm
from analysis import Analysis
import sys

def main(sequence_length: int = 209, nucleotide_length: int = 10, n_remove: int = 0, n_insert: int = 0, n_duplicate: int = 0, filename: str = 'nucleotides_with_errors.txt', algorithm: str = 'antColonySearchSW'):
    generator = Generator(sequence_length, nucleotide_length, n_remove, n_insert, n_duplicate)
    generator.main()

    sbh = sbh_algorithm(sequence_length, filename, algorithm)
    sbh.main()

    analysis = Analysis(generator.sequence, sbh.result)
    analysis.analyze()
    analysis.print_results()

if __name__ == '__main__':
    # sequence_length = int(sys.argv[2])
    main(sequence_length=400, n_remove=80, n_insert=0, n_duplicate=0)