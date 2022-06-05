from importlib.resources import path
import time
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
        self.n = int(argv[2]) # original sequence length

        # if self.argv[3]: self.argv[3] = int(self.argv[3])
    

    def __euclidean__(self, a, b):
        return math.sqrt(pow(int(a[1]) - int(b[1]), 2) + pow(int(a[0]) - int(b[0]), 2))


    def __match__(self, v1, v2):
        v1 = v1[len(v1) - len(v2):]
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
        


    def ACO(self):
        world = pants.World(self.vertices, self.__match__) # self.__euclidean__
        solver = pants.Solver()

        # solution = solver.solve(world)
        solutions = solver.solutions(world)

        return solutions


    def showSolutions(self, solutions):
        for solution in solutions:
            print(f'Distance: {solution.distance}')
            print(f'Tour: {solution.tour}')
            print('Path:')
            for i in solution.path:
                print(f'Start: {i.start}, end: {i.end}, length: {i.length}, pheromone: {i.pheromone}')
    

    def showSolution(self, solutions):
        solution = solutions[-1]
        print(f'Distance: {solution.distance}')
        print(f'Tour: {solution.tour}')
        print('Path:')
        for i in solution.path:
            print(f'Start: {i.start}, end: {i.end}, length: {i.length}, pheromone: {i.pheromone}')

    def __parse__(self, string1, string2):
        if string1 == '':
            return string2
        n = self.__match__(string1, string2)
        return string1 + string2[-n:]

    def __parseAll__(self, strings):
        result = ''
        for i in range(len(strings)):
                result = self.__parse__(result, strings[i])
        return result

    def printNicely(self, path):
        toStrings = []
        for i in range(len(path)):
            toStrings.append(self.vertices[path[i]])
        
        print(f"{self.__parseAll__(toStrings)}")
        print(f"{len(self.__parseAll__(toStrings))}")


    def ant_colony_search(self):
        pheromonesMatrix = []
        optimum = []
        random.seed(time.time())
        optlen = 0
        
        # init pheromones matrix
        for i in self.vertices:
            pheromonesMatrix.append([])
            for j in self.vertices:
                pheromonesMatrix[-1].append(0.1)

        # options for manipulation
        antsPerVertex = 1
        numberOfVerticesWithAnts = 40
        alfa = 10
        beta = 10
        p = 0.3
        maxTime = 120

        # the beginning
        start = time.time()
        while True:
            
            # ant placement
            verticesWithAnts = random.sample(range(0, len(self.vertices)), numberOfVerticesWithAnts)
            currentPheromones = []

            for vertex in verticesWithAnts:
                for ant in range(antsPerVertex):
                    currentPath = [vertex]
                    currentSequenceLength = self.l

                    # ant is going to walk through the graph
                    while True:
                        verticesProbabilities = []
                        sum = 0
                        for i in range(len(self.vertices)):
                            if (i not in currentPath and currentSequenceLength + self.matrix[currentPath[-1]][i] <= self.n):
                                sum += pow(pheromonesMatrix[currentPath[-1]][i], alfa) * pow(1 / self.matrix[currentPath[-1]][i], beta)
                            verticesProbabilities.append(sum)

                        if sum == 0:
                            break

                        roll = random.uniform(0, sum)
                        for i in range(len(verticesProbabilities)):
                            if roll <= verticesProbabilities[i]:
                                currentSequenceLength += self.matrix[currentPath[-1]][i]
                                currentPath.append(i)
                                break

                    #chanage optimal path
                    if len(currentPath) > len(optimum):
                        optimum = currentPath
                        optlen = currentSequenceLength
                    
                    # phermonoes reinforcement
                    pheromones = len(currentPath) * 10

                    
                    #init clear currentPheromones
                    for i in range(len(self.vertices)):
                        currentPheromones.append([])
                        for j in range(len(self.vertices)):
                            currentPheromones[i].append(0)

                    # add data to the currentPheromones
                    for i in range(len(currentPath) - 1):
                        currentPheromones[currentPath[i]][currentPath[i + 1]] += pheromones

            # add new phermonons to the pheromonesMatrix
            for i in range(len(pheromonesMatrix)):
                for j in range(len(pheromonesMatrix[i])):
                    pheromonesMatrix[i][j] = (p * pheromonesMatrix[i][j] + currentPheromones[i][j])

            # end of time
            end = time.time()
            if currentSequenceLength == self.n - self.l + 1 or end - start > maxTime:
                print(optimum)
                print(len(optimum))
                print(optlen)
                self.printNicely(optimum)
                break



    def main(self):
        self.readfile(self.argv[1])
        # print(f"DATA: \n{self.vertices}\n{self.matrix}\n{self.l}")
        err = False
        if len(self.argv) > 3:
            if self.argv[3] == 'ACO':
                self.ACO()
            elif self.argv[3] == 'antColonySearch':
                self.ant_colony_search()
            else:
                err = True
        else:
            err = True

        if err:
            print('You need to specify a proper algorithm name!')
            print('Available algorithms: \n\t+ ACO \n\t+ antColonySearch')
            sys.exit()
                


if __name__ == '__main__':
    obj = sbhAlgorithm(sys.argv)
    obj.main()

