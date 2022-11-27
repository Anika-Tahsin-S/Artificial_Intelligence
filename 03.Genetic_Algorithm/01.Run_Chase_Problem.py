import random as rd
import math

with open('03.Genetic_Algorithm\RunChase_Input.txt', 'r') as f:
      lines = f.readlines()

class GeneticAlgorithm:
    def __init__(self, player_run_PAIR, run_target):
        self.problem = player_run_PAIR # [('Tamim', 68), ('Shoumyo', 25), ('Shakib', 70), ('Afif', 53), ('Mushfiq', 71), ('Liton', 55), ('Mahmudullah', 66), ('Shanto', 29)]
        self.goal = run_target  # 330 

        self.population = None
        self.population_size = 18

        self.max_fitness = math.inf
        self.fittest_individual = False # Setting indivial avg not good for fitness


        self.generation = 1
        self.threshold_guard = 300
        
        
# ================================== Level 2: All function in work here ========================================= #
    def Hashiru(self):
        # Within population_size, checked problem which is player_run_PAIR and randomized in range 0, 1 for player action
        self.population = [[rd.randint(0, 1) for j in range(len(self.problem))] for i in range(self.population_size)] # 18 population within player_set with 0 1

        # print(f"{self.population}")
        # For each generation if threshold greater count GENERATION
        while self.generation < self.threshold_guard:
            #print(f"GENERATIONS: {self.generation}") 

            # Selecting by fitness analyzation
            self.__select() 
            if self.fittest_individual: # when individual not good fitness show the team fitness (found from fitness)
                print([self.problem[i][0] for i in range(len(self.problem))]) # player names
                # print(f"FITTEST COMBINATION: {self.fittest_individual}") # 1, 0 player action indicate
                print(''.join(map(str,self.fittest_individual)))
                return
            
            # perform crossover among the parents from the first half of the population (from 18 took first 9)
            l, r = 0, len(self.population) // 2 - 1
            while l < r:
                offsprings = self.__crossover(self.population[l], self.population[r])
                # print("\nshow offspring", offsprings)
                self.population[l], self.population[r] = offsprings[0], offsprings[1]
                l += 1
                r -= 1

            # randomly generate new population for second half of the array
            start_second_half = len(self.population) // 2
            for i in range(start_second_half, len(self.population)):
                self.population[i] = [rd.randint(0, 1) for j in range(len(self.problem))] # 0 1 randomly set within range players
                # print(self.population[i])
            # Perform mutation
            self.__mutate()
            self.generation += 1 # to check how many generation was performed
        
        # When string cannot be formed
        print([self.problem[i][0] for i in range(len(self.problem))])
        print(f"FAILURE, str cannot be formed: {-1}")

# ================================== Level 1: FITNESS, SELECTION, CROSSOVER, MUTATION ========================================= #

# Fitness
    def __fitness(self):
        fitness_list = [] # All fitness list will be stored here

        for kodomotachi in self.population: # checking kodomotachi fitness, popultion is 0 1 action set
            total_run = 0
            for i in range(len(kodomotachi)):
                # print(kodomotachi) ; each kodomotachi 0, 1 set
                # print(self.problem[i][1]) # each generation run
                total_run += kodomotachi[i] * int(self.problem[i][1]) # with each action 1 * generation run 
                #print("misete!", total_run)

            difference = abs(self.goal - total_run)  # 330 - found_run ; non negative
            if difference == 0:
                self.fittest_individual = kodomotachi
                # print("\n------>",self.fittest_individual)
                fitness_list.append(-math.inf) # max_fitness
                # print(fitness_list)
            else:
                fitness_list.append(1/difference)
        # print(fitness_list)
        
        return fitness_list

# Select
    def __select(self):
        fitness_list = self.__fitness()
        population_on_fitness = [i for _, i in sorted(zip(fitness_list, self.population))] # list tuple version of fitness, population
        # print("\n>>>>>>>>>>>>>>>>>>>>",(fitness_list, self.population))
        self.population = population_on_fitness # best fitness kodomotachi selected
        # print("selected population", self.population)

# Crossover
    def __crossover(self, p1, p2):
        new_kodomotachi = [[], []]
        # print("\nmiseteeeeeeeeeee", p1, p2)
        start = rd.randint(0, len(p1)//2) # randomly taken start range for kodomotachi crossover
        end = start + len(p1) // 2        # randomly taken end range for kodomotachi crossover
        # print("\n>>>>>>>>>>>>", start, end)
        for i in range(len(p1)):
            if start <= i < end:
                new_kodomotachi[0].append(p1[i]) # p1 crossover range in new kodomo first part
                new_kodomotachi[1].append(p2[i]) # p2 crossover range in new kodomo last part
            else:
                new_kodomotachi[0].append(p2[i])
                new_kodomotachi[1].append(p1[i])
        # print("kodomo", new_kodomotachi, "\n")
        return new_kodomotachi

# Mutation
    def __mutate(self):
        # Perform mutation with very low probability to avoid premature convergence
        # choosing spots from the generated population
        mutation_spot = [rd.randint(0, len(self.population) - 1) for z in range(6)] # randomly selecting mutation spots
        # Value change in selected spots
        for m in mutation_spot:
            mutation_val_change = rd.randint(0, len(self.problem) - 1) # changing value from players
            # self.population[m][mutation_val_change] == 1 if self.population[m][mutation_val_change] == 0 else 0
            if self.population[m][mutation_val_change] == 0:
                self.population[m][mutation_val_change] = 1 
            else:
                self.population[m][mutation_val_change] = 0


# ======================================================= #
# Level 0 : Processing Input File
def inputread(lines):
  player = [] # Names
  player_count = [] # rest of the lines from line 2
  all = []

  for s in range(len(lines)): 
    if s == 0:
        firstline = lines[0] # firstlineofTxt
        firstlineList = firstline.rstrip().split()
        n, run_target = int(firstlineList[0]), int(firstlineList[1])
    else:
        string_run = lines[s] # rest lines
        player_count.append(string_run)        
        """ print("show me what you are", player_count) """

  for b in player_count:
    player, player_count = b.rstrip().split()
    all.append((player, int(player_count)))
    # print(all)
    """ print(type(player)) """
  return all, run_target

# ======================================================= #
problem, run_target = inputread(lines)
# print("ki eta", problem)
genetic_algorithm = GeneticAlgorithm(problem, run_target)
genetic_algorithm.Hashiru()