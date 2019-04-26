import numpy as np
import random

def init_population(population_size,
                    chromosome_length ):
    population = np.zeros((population_size,chromosome_length))
    for i in range(population_size):
        ones = random.randint(0,chromosome_length)
        population[i,0:ones]=1
        np.random.shuffle(population[i])
    return population

def calculateFitness(reference, population):
    identicals = population == reference
    fitness_scores = identicals.sum(axis=1)
    return fitness_scores

def tournament(population, scores):
    size = len(scores)

    fighter_1 = random.randint(0,size-1)
    fighter_2 = random.randint(0,size-1)
    print(str(fighter_1)+'vs'+str(fighter_2))
    f_1_score = scores[fighter_1]
    f_2_score = scores[fighter_2]

    return population[fighter_1,:] if f_1_score >= f_2_score else population[fighter_2,:]


def crossover(parent_1, parent_2):
    size= len(parent_1)
    crossover_pont = random.randint(1,size-1)
    child_1 = np.hstack((parent_1[0:crossover_pont],
                         parent_2[crossover_pont:]))
    child_2 = np.hstack((parent_2[0:crossover_pont],
                         parent_1[crossover_pont:]))
    return child_1, child_2

def mutation(population, mutation_rate):
    mutation = np.random.random(size=population.shape)
    mutation_boolean = mutation <= mutation_rate
    population[mutation_boolean] = np.logical_not(population[mutation_boolean])
    return population

reference = [0,0,1,1,0,0,1,0,0]
chromosome_length = len(reference)
population_size = 16
generation_max = 500
population = init_population(population_size,chromosome_length)

fitness = calculateFitness(reference,population)
print(fitness)
best_scores = []
best_scores.append((np.max(fitness)/chromosome_length)*100)
for gen in range(generation_max):
    new_population =[]
    for i in range(int(population_size/2)):
        parent_1 = tournament(population,fitness)
        parent_2 = tournament(population,fitness)
        child_1, child_2 = crossover(parent_1,parent_2)
        new_population.append(child_1)
        new_population.append(child_2)
    population= np.array(new_population)
    population = mutation(population,0.005)
    fitness = calculateFitness(reference,population)
    best_scores.append((np.max(fitness) / chromosome_length) * 100)

print(population)

import matplotlib.pyplot as plt
plt.plot(best_scores)
plt.xlabel("Generation")
plt.ylabel("Best Score (%)")
plt.ylim(0,100)
plt.show()
