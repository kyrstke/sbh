import random


def generateSequence(size: int):
    letters = 'CATG'
    return ''.join([random.choice(letters) for _ in range(size)])


def cutSequence(sequence: str, nucleotide_length: int):
    nucleotide = ''
    for i, c in enumerate(sequence):
        nucleotide += c
        if i > nucleotide_length - 1:
            yield nucleotide[i-nucleotide_length:]


def saveToFile(filename: str, nucleotides: str):
    first_node = nucleotides[0]
    nucleotides = nucleotides[1:]
    random.shuffle(nucleotides)
    with open(filename, 'w') as f:
        f.write(first_node)
        for nucleotide in nucleotides:
            f.write('\n' + nucleotide)


def main():
    sequence_length = 209
    nucleotide_length = 10
    sequence = generateSequence(sequence_length)
    print(sequence)

    data = [*cutSequence(sequence, nucleotide_length)]
    print(data)

    saveToFile('nucleotides.txt', data)


if __name__ == '__main__': 
    main()