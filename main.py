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
    analysis.print_results()

    return {"ratio": analysis.ratio, "calc_length": len(sbh.result), "elapsed_time": round(sbh.elapsed_time, 1)}

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

        ants_per_vertex = 40
        alfa = 10
        beta = 10
        p = 0.3
        max_time = 20

        filename = 'nucleotides_with_errors.txt'
        algorithm = 'antColonySearchSW'
    
    nucleotide_quantity = sequence_length/nucleotide_length
    print(f"Seqence length: {sequence_length}")
    print(f"Nucleotide length: {nucleotide_length}")
    print(f"Removed nucleotides: {n_remove} {n_remove/nucleotide_quantity}")
    print(f"Inserted nucleotides: {n_insert} {n_insert/nucleotide_quantity}")
    print(f"Duplicated nucleotides: {n_duplicate} {n_duplicate/nucleotide_quantity}")


    result = main(ants_per_vertex, alfa, beta, p, max_time, sequence_length, nucleotide_length, n_remove, n_insert, n_duplicate, filename, algorithm)

    print(f"|_id_|{sequence_length}|{result['calc_length']}|{round(result['ratio'], 3)*100}|{result['elapsed_time']}|{alfa}|{beta}|{p}|{ants_per_vertex}|")
    print(f"|_id_|{sequence_length}|{result['calc_length']}|{round(result['ratio'], 3)*100}|{nucleotide_length}|{round(n_duplicate/nucleotide_quantity, 2)}|{round(n_remove/nucleotide_quantity, 2)}|{round(n_insert/nucleotide_quantity, 2)}|")