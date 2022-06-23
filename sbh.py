from importlib.resources import path
import time
import pants
import math
import random
import sys

class sbh_algorithm():
    def __init__(self, n: int = 200, filename: str = 'nucleotides.txt', algorithm: str = 'antColonySearchSW') -> None:
        self.vertices = []
        self.matrix = []
        self.l = 0
        self.n = n
        self.filename = filename
        self.algorithm = algorithm
        self.optimum = []
    

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


    def read_file(self, file):
        f = open(file, "r")
        for line in f:
            self.vertices.append(line.replace("\n", ""))
        f.close()


    def initialize_matrix(self):
        for vertex1 in self.vertices:
            self.matrix.append([])
            for vertex2 in self.vertices:
                n = self.__match__(vertex1, vertex2)
                self.matrix[-1].append(n)

        self.l = len(self.vertices[0])
        


    def aco(self):
        world = pants.World(self.vertices, self.__match__) # self.__euclidean__
        solver = pants.Solver()

        # solution = solver.solve(world)
        self.solutions = solver.solutions(world)


    def show_solutions(self):
        for solution in self.solutions:
            print(f'Distance: {solution.distance}')
            print(f'Tour: {solution.tour}')
            print('Path:')
            for i in solution.path:
                print(f'Start: {i.start}, end: {i.end}, length: {i.length}, pheromone: {i.pheromone}')
    

    def show_solution(self):
        solutions = [*self.solutions]
        # print(solutions)
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


    def __parse_all__(self, strings):
        result = ''
        for i in range(len(strings)):
                result = self.__parse__(result, strings[i])
        return result


    def merge_into_sequence(self, path):
        to_strings = []
        for i in range(len(path)):
            to_strings.append(self.vertices[path[i]])
        self.result = self.__parse_all__(to_strings)
        

    def ant_colony_search(self):
        pheromones_matrix = []
        optimum = []
        random.seed(time.time())
        optlen = 0
        
        # init pheromones matrix
        for i in self.vertices:
            pheromones_matrix.append([])
            for j in self.vertices:
                pheromones_matrix[-1].append(0.1)

        # options for manipulation
        ants_per_vertex = 1
        number_of_vertices_with_ants = 40
        alfa = 10
        beta = 10
        p = 0.3
        max_time = 20

        # no improvement counter
        counter = 0

        # the beginning
        start = time.time()
        while True:
            
            # ant placement
            vertices_with_ants = random.sample(range(0, len(self.vertices)), number_of_vertices_with_ants)
            current_pheromones = []

            for vertex in vertices_with_ants:
                for ant in range(ants_per_vertex):
                    current_path = [vertex]
                    current_sequence_length = self.l
                    counter += 1

                    # ant is going to walk through the graph
                    print(f'ant {ant} started its path at vertex {vertex}...')
                    while True:
                        vertices_probabilites = []
                        sum = 0
                        for i in range(len(self.vertices)):
                            if (i not in current_path) and (current_sequence_length + self.matrix[current_path[-1]][i] <= self.n):
                                sum += pow(pheromones_matrix[current_path[-1]][i], alfa) * pow(1 / self.matrix[current_path[-1]][i], beta)
                                # print(sum)
                            vertices_probabilites.append(sum)

                        if sum == 0:
                            break
                        
                        roll = random.uniform(0, sum)
                        for i in range(len(vertices_probabilites)):
                            if roll <= vertices_probabilites[i]:
                                current_sequence_length += self.matrix[current_path[-1]][i]
                                current_path.append(i)
                                break

                    #chanage optimal path
                    if len(current_path) > len(self.optimum):
                        counter = 0
                        self.optimum = current_path
                        optlen = current_sequence_length
                    
                    # phermonoes reinforcement
                    pheromones = len(current_path) * 10

                    # init clear currentPheromones
                    for i in range(len(self.vertices)):
                        current_pheromones.append([])
                        for j in range(len(self.vertices)):
                            current_pheromones[i].append(0)

                    # add data to the currentPheromones
                    for i in range(len(current_path) - 1):
                        current_pheromones[current_path[i]][current_path[i + 1]] += pheromones

            # add new phermonons to the pheromonesMatrix
            for i in range(len(pheromones_matrix)):
                for j in range(len(pheromones_matrix[i])):
                    pheromones_matrix[i][j] = (p * pheromones_matrix[i][j] + current_pheromones[i][j])

            # end of time
            end = time.time()
            
            if len(self.optimum) == self.n - self.l + 1 or counter >= 10 or end - start > max_time:
                self.merge_into_sequence(self.optimum)
                self.print_results(start, end)
                break


    def ant_colony_search_with_starting_vertex(self):
        pheromones_matrix = []
        self.optimum = []
        random.seed(time.time())
        optlen = 0
        
        # init pheromones matrix
        for i in self.vertices:
            pheromones_matrix.append([])
            for j in self.vertices:
                pheromones_matrix[-1].append(0.1)

        # options for manipulation
        ants_per_vertex = 40
        alfa = 10
        beta = 10
        p = 0.3
        max_time = 20

        # ant placement
        vertex = 0

        # no improvement counter
        counter = 0

        # the beginning
        start = time.time()
        while True:
        
            current_pheromones = []

            for ant in range(ants_per_vertex):
                current_path = [vertex]
                current_sequence_length = self.l
                counter += 1

                # ant is going to walk through the graph
                print(f'ant {ant} started its path...')
                while True:
                    vertices_probabilites = []
                    sum = 0
                    for i in range(len(self.vertices)):
                        if (i not in current_path) and (current_sequence_length + self.matrix[current_path[-1]][i] <= self.n):
                            sum += pow(pheromones_matrix[current_path[-1]][i], alfa) * pow(1 / self.matrix[current_path[-1]][i], beta)
                            # print(sum)
                        vertices_probabilites.append(sum)

                    if sum == 0:
                        break
                    
                    roll = random.uniform(0, sum)
                    for i in range(len(vertices_probabilites)):
                        if roll <= vertices_probabilites[i]:
                            current_sequence_length += self.matrix[current_path[-1]][i]
                            current_path.append(i)
                            break

                #chanage optimal path
                if len(current_path) > len(self.optimum):
                    counter = 0
                    self.optimum = current_path
                    optlen = current_sequence_length
                
                # phermonoes reinforcement
                pheromones = len(current_path) * 10

                # init clear currentPheromones
                for i in range(len(self.vertices)):
                    current_pheromones.append([])
                    for j in range(len(self.vertices)):
                        current_pheromones[i].append(0)

                # add data to the currentPheromones
                for i in range(len(current_path) - 1):
                    current_pheromones[current_path[i]][current_path[i + 1]] += pheromones

            # add new phermonons to the pheromonesMatrix
            for i in range(len(pheromones_matrix)):
                for j in range(len(pheromones_matrix[i])):
                    pheromones_matrix[i][j] = (p * pheromones_matrix[i][j] + current_pheromones[i][j])

            # end of time
            end = time.time()
            print(f'Current time is: {round(end - start, 3)} seconds')

            
            # print(f'Current optimal path: {optimum}')

            if len(self.optimum) == self.n - self.l + 1 or counter >= 10 or end - start > max_time:
                self.merge_into_sequence(self.optimum)
                self.print_results(start, end)
                break
    

    def print_results(self, start, end):
        print(f'Elapsed time: {round(end - start, 3)} seconds')

        print(f'Goal sequence length: {self.n - self.l + 1}')
        print(f'Vertices visiting order: {self.optimum}')
        print(f'Vertices visited: {len(self.optimum)}')

        print(f"Sequence: {self.result}")
        print(f"Sequence length: {len(self.result)}")


    def main(self):
        self.read_file(self.filename)
        self.initialize_matrix()
        # print(f"DATA: \n{self.vertices}\n{self.matrix}\n{self.l}")

        err = False
        if self.algorithm == 'ACO':
            self.aco()
            self.show_solutions()
        elif self.algorithm == 'antColonySearch':
            self.ant_colony_search()
        elif self.algorithm == 'antColonySearchSW':
            self.ant_colony_search_with_starting_vertex()
        else:
            err = True

        if err:
            print('You need to specify a proper algorithm name!')
            print('Available algorithms: \n\t+ ACO \n\t+ antColonySearch \n\t+ antColonySearchSW')
            sys.exit()
                


if __name__ == '__main__':
    filename = sys.argv[1]
    sequence_length = int(sys.argv[2]) # original sequence length
    algorithm = sys.argv[3]

    sbh = sbh_algorithm(sequence_length, filename, algorithm)
    sbh.main()

