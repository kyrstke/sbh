import Levenshtein as lev
import sys

class Analysis():
    def __init__(self, base, result):
        self.base = base
        self.result = result

    def analyze(self):
        self.distance = lev.distance(self.base, self.result)
        self.ratio = lev.ratio(self.base, self.result)

    def print_results(self):
        print(f'Levenshtein distance: {self.distance}')
        print(f'Ratio (similarity): {round(self.ratio, 3)}')


if __name__ == "__main__":
    base = sys.argv[1]
    result = sys.argv[2]

    analysis = Analysis(base, result)
    analysis.analyze()
    analysis.print_results()