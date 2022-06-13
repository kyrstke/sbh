from importlib.resources import path
import time
import pants
import math
import random
import sys

class sbh_algorithm():
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


    def read_file(self, file):
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
        


    def aco(self):
        world = pants.World(self.vertices, self.__match__) # self.__euclidean__
        solver = pants.Solver()

        # solution = solver.solve(world)
        solutions = solver.solutions(world)

        return solutions


    def show_solutions(self, solutions):
        for solution in solutions:
            print(f'Distance: {solution.distance}')
            print(f'Tour: {solution.tour}')
            print('Path:')
            for i in solution.path:
                print(f'Start: {i.start}, end: {i.end}, length: {i.length}, pheromone: {i.pheromone}')
    

    def show_solution(self, solutions):
        solutions = [*solutions]
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


    def print_nicely(self, path):
        to_strings = []
        
        for i in range(len(path)):
            to_strings.append(self.vertices[path[i]])
        result = self.__parse_all__(to_strings)

        print(f"Sequence: {result}")
        print(f"Sequence length: {len(result)}")


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

                    # ant is going to walk through the graph
                    while True:
                        vertices_probabilites = []
                        sum = 0
                        for i in range(len(self.vertices)):
                            if (i not in current_path) and (current_sequence_length + self.matrix[current_path[-1]][i] <= self.n):
                                sum += pow(pheromones_matrix[current_path[-1]][i], alfa) * pow(1 / self.matrix[current_path[-1]][i], beta)
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
                    if len(current_path) > len(optimum):
                        optimum = current_path
                        optlen = current_sequence_length
                    
                    # phermonoes reinforcement
                    pheromones = len(current_path) * 10

                    
                    #init clear currentPheromones
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
            print(f'Current sequence length: {current_sequence_length}')
            if current_sequence_length == self.n - self.l + 1 or end - start > max_time:
                print(f'Goal sequence length: {self.n - self.l + 1}')
                print(f'Elapsed time: {end - start}')
                print(f'Current sequence length: {current_sequence_length}')
                print(f'Vertices visiting order: {optimum}')
                print(f'Vertices visited: {len(optimum)}')
                print(f'Vertices probabilities: {vertices_probabilites}')
                print(f'Optlen: {optlen}')
                self.print_nicely(optimum)
                break


    def ant_colony_search_with_starting_vertex(self):
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
        ants_per_vertex = 40
        number_of_vertices_with_ants = 1
        alfa = 10
        beta = 10
        p = 0.3
        max_time = 20

        # ant placement
        vertex = 0

        # the beginning
        start = time.time()
        while True:
        
            current_pheromones = []

            for ant in range(ants_per_vertex):
                current_path = [vertex]
                current_sequence_length = self.l

                # ant is going to walk through the graph
                while True:
                    vertices_probabilites = []
                    sum = 0
                    for i in range(len(self.vertices)):
                        if (i not in current_path) and (current_sequence_length + self.matrix[current_path[-1]][i] <= self.n):
                            sum += pow(pheromones_matrix[current_path[-1]][i], alfa) * pow(1 / self.matrix[current_path[-1]][i], beta)
                            print(sum)
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
                if len(current_path) > len(optimum):
                    optimum = current_path
                    optlen = current_sequence_length
                
                # phermonoes reinforcement
                pheromones = len(current_path) * 10

                
                #init clear currentPheromones
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
            # print(f'Current sequence length: {current_sequence_length}')
            if current_sequence_length == self.n - self.l + 1 or end - start > max_time:
                print(f'Goal sequence length: {self.n - self.l + 1}')
                print(f'Elapsed time: {end - start}')
                print(f'Current sequence length: {current_sequence_length}')
                print(f'Vertices visiting order: {optimum}')
                print(f'Vertices visited: {len(optimum)}')
                print(f'Vertices probabilities: {vertices_probabilites}')
                print(f'Optlen: {optlen}')
                self.print_nicely(optimum)
                break


    def main(self):
        self.read_file(self.argv[1])
        print(f"DATA: \n{self.vertices}\n{self.matrix}\n{self.l}")
        err = False
        if len(self.argv) > 3:
            if self.argv[3] == 'ACO':
                solution = self.aco()
                self.show_solutions(solution)
            elif self.argv[3] == 'antColonySearch':
                self.ant_colony_search()
            elif self.argv[3] == 'antColonySearchSW':
                self.ant_colony_search_with_starting_vertex()
            else:
                err = True
        else:
            err = True

        if err:
            print('You need to specify a proper algorithm name!')
            print('Available algorithms: \n\t+ ACO \n\t+ antColonySearch')
            sys.exit()
                


if __name__ == '__main__':
    obj = sbh_algorithm(sys.argv)
    obj.main()

