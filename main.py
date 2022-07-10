from generator import Generator 
from sbh import sbhAlgorithm
from analysis import Analysis
import sys

def main(ants_per_vertex, alfa, beta, p, max_time, sequence_length: int = 209, nucleotide_length: int = 10, n_remove: int = 0, n_insert: int = 0, n_duplicate: int = 0, filename: str = 'nucleotides_with_errors.txt', algorithm: str = 'antColonySearchSW'):
    generator = Generator(sequence_length, nucleotide_length, n_remove, n_insert, n_duplicate)
    generator.main()

    sbh = sbhAlgorithm(ants_per_vertex, alfa, beta, p, max_time,  sequence_length, filename, algorithm)
    sbh.main()

    analysis = Analysis(generator.sequence, sbh.result)
    analysis.analyze()
    # analysis.print_results()

    return {"ratio": analysis.ratio, "calc_length": len(sbh.result), "elapsed_time": round(sbh.elapsed_time, 2)}

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
        sequence_length = 100
        nucleotide_length = 10
        n_remove = int(0.5 * sequence_length)
        n_insert = 0  # int(0.75 * sequence_length)
        n_duplicate = 0

        filename = 'nucleotides_with_errors.txt'
        algorithm = 'antColonySearchSW'
    
    ants_per_vertex = 25
    alfa = 12
    beta = 12
    p = 0.45
    max_time = 30
    
    nucleotide_quantity = sequence_length/nucleotide_length
    print(f"Seqence length: {sequence_length}")
    print(f"Nucleotide length: {nucleotide_length}")
    print(f"Removed nucleotides: {n_remove} {round(n_remove/nucleotide_quantity, 2)}%")
    print(f"Inserted nucleotides: {n_insert} {round(n_insert/nucleotide_quantity, 2)}%")
    print(f"Duplicated nucleotides: {n_duplicate} {round(n_duplicate/nucleotide_quantity, 2)}%\n")

    for i in range(10):
        for j in range(5):
            result = main(ants_per_vertex, alfa, beta, p, max_time, sequence_length, nucleotide_length, n_remove, n_insert, n_duplicate, filename, algorithm)
            print(f"|{i*5+j}|{sequence_length}|{result['calc_length']}|{round(result['ratio'], 3)*100}|{result['elapsed_time']}|{nucleotide_length}|{round(n_duplicate/nucleotide_quantity, 2)}|{round(n_remove/nucleotide_quantity, 2)}|{round(n_insert/nucleotide_quantity, 2)}|")
        sequence_length += 100

        # print(f"|{i}|{sequence_length}|{result['calc_length']}|{round(result['ratio'], 3)*100}|{result['elapsed_time']}|{alfa}|{beta}|{p}|{ants_per_vertex}|")
        # ants_per_vertex += 3
        # p += 0.05
        # alfa += 1
        # beta += 1