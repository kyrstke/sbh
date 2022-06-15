from copy import deepcopy
import random
import sys
import numpy as np

class generator:
    def __init__(self, sequence_length: int = 200, nucleotide_length: int = 10, n_remove: int = 0, n_insert: int = 0, n_duplicate: int = 0):
        self.sequence_length = sequence_length
        self.nucleotide_length = nucleotide_length
        self.nucleotides_with_errors = []
        self.n_remove = n_remove
        self.n_insert = n_insert
        self.n_duplicate = n_duplicate

        self.letters = 'ACGT'
        self.nucleotides = []
        self.sequence = ''


        
    def generateSequence(self, size: int):
        return ''.join([random.choice(self.letters) for _ in range(size)])
    

    def cutSequence(self, sequence: str, nucleotide_length: int):
        nucleotide = ''
        for i, c in enumerate(sequence):
            nucleotide += c
            if i > nucleotide_length - 1:
                yield nucleotide[i-nucleotide_length:]


    def saveToFile(self, filename: str, nucleotides: str):
        first_node = nucleotides[0]
        nucleotides = nucleotides[1:]
        random.shuffle(nucleotides)
        with open(filename, 'w') as f:
            f.write(first_node)
            for nucleotide in nucleotides:
                f.write('\n' + nucleotide)


    def removeRandomList(self, li: list, quantity: int):
        to_duplicate = random.sample(li, quantity)
        result = [[] if i in to_duplicate else [i] for i in li]
        return list(np.concatenate(result).flat)

    def insertRandomList(self, li: list, quantity: int):
        to_duplicate = random.sample(li, quantity)
        result = [[i, ''.join([random.choice(self.letters) for i in range(len(li[0]))])] if i in to_duplicate 
            else [i] for i in li]
        return list(np.concatenate(result).flat)

    def duplicateRandomList(self, li: list, quantity: int):
        to_duplicate = random.sample(li, quantity)
        result = [[i, i] if i in to_duplicate else [i] for i in li]
        return list(np.concatenate(result).flat)

    def createErrors(self):
        self.nucleotides_with_errors = deepcopy(self.nucleotides)
        self.nucleotides_with_errors = self.removeRandomList(self.nucleotides_with_errors, self.n_remove)
        self.nucleotides_with_errors = self.insertRandomList(self.nucleotides_with_errors, self.n_insert)
        self.nucleotides_with_errors = self.duplicateRandomList(self.nucleotides_with_errors, self.n_duplicate)
        



    def main(self):
        self.sequence = self.generateSequence(self.sequence_length)
        print(self.sequence)

        self.nucleotides = [*self.cutSequence(self.sequence, self.nucleotide_length)]
        print(self.nucleotides)

        self.createErrors()

        self.saveToFile('nucleotides.txt', self.nucleotides)
        self.saveToFile('nucleotides_with_errors.txt', self.nucleotides_with_errors)


if __name__ == '__main__': 
    sequence_length = int(sys.argv[1])
    nucleotide_length = int(sys.argv[2])
    n_remove = 0
    n_insert = 0
    n_duplicate = 0

    if (len(sys.argv) > 3):
        option = [i.split(':') for i in sys.argv[3].split(',')]
        for i in option:
            if i[0] == 'r':
                n_remove = int(i[1])
            elif i[0] == 'i':
                n_insert = int(i[1])
            elif i[0] == 'd':
                n_duplicate = int(i[1])
            else:
                print('Unknown option')
                sys.exit(1)
        print(n_remove, n_insert, n_duplicate)


    obj = generator(sequence_length, nucleotide_length, n_remove, n_insert, n_duplicate)
    obj.main()
