import Levenshtein as lev


if __name__ == "__main__":
    # base = 'TGGAATCCCGCTACCGCGTAGAAAAGAGGAGCAAGGTGTTATCTCTTGGG'
    # result = 'TGGAATCCCGCTATCTCTTGGGAATCCCGCTACCGCGTAGAAAAGAGGAG'
    # # base = '12345678'
    # # result = '12345678'
    # distance = levenshtein(base, result)
    # l = len(base) + len(result)
    # percentage = (l - distance) / l * 100
    # print(f'Distance: {distance}\nMatching percentage: {percentage}%')

    base = "CGGCATCTCTTCTCCGTGCCGCCTTATGCCATCTCACTTGGTGATTTATG"
    result = "CGGCATCTCTTTTATGCCATCTCACTTGGTGATTTATGCCGCCTTATGCC"
    distance = lev.distance(base[10:], result[10:])
    # print(distance)
    print(f'Levenshtein distance: {distance}')

    ratio = lev.ratio(base[10:], result[10:])
    # print(ratio)
    print(f'Ratio: {ratio}')