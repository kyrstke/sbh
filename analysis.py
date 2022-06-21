from re import A
import Levenshtein as lev

class Analysis():
    def __init__(self, base, result):
        self.base = base
        self.result = result

    def analyze(self):
        self.distance = lev.distance(self.base[10:], self.result[10:])
        self.ratio = lev.ratio(self.base[10:], self.result[10:])

    def print_results(self):
        print(f'Levenshtein distance: {self.distance}')
        print(f'Ratio (similarity): {self.ratio}')


if __name__ == "__main__":
    base = ''
    result = ''

    analysis = Analysis(base, result)
    analysis.analyze()
    analysis.print_results()