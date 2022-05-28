from importlib.resources import path
import pants
import math
import random
import sys

class sbhAlgorithm():
    def __init__(self, argv) -> None:
        self.vertices = []
        self.matrix = []
        self.l = 0
        self.argv = argv
    

    def __euclidean__(self, a, b):
        return math.sqrt(pow(a[1] - b[1], 2) + pow(a[0] - b[0], 2))


    def __match__(self, v1, v2):
        n = 1
        if v1 == v2:
            return 0
        while n < len(v1):
            if v1[n:] == v2[:-n]:
                break
            else:
                n += 1
        return n


    def readfile(self, file):
        f = open(file, "r")

        for line in f:
            self.vertices.append(line.replace("\n", ""))

        f.close()

        for vertex1 in self.vertices:
            self.matrix.append([])
            for vertex2 in self.vertices:
                n = self.__match__(vertex1, vertex2)
                self.matrix[-1].append(n)

        self.l = len(self.vertices[0])
        
        # return vertices, matrix, l


    def antColonySearch(self):
        self.readfile(sys.argv[1])
        world = pants.World(self.vertices, self.__euclidean__)
        solver = pants.Solver()
        solutions = solver.solutions(world)
        print(solutions.distance)
        print(solutions.tour)
        print(solutions.path)


    def main(self):
        self.antColonySearch()


if __name__ == '__main__':
    obj = sbhAlgorithm(sys.argv[0])
    obj.main()