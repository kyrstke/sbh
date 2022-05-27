import random


def generateString(size: int):
    letters = 'CATG'
    return ''.join([random.choice(letters) for i in range(size)])


def main():
    length = 10
    print(generateString(length))


if __name__ == '__main__': 
    main()