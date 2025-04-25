import random
import numpy as np
from individual import Individual

class Population:
    def __init__(self, amount, genome_length, mutation_rate,quality):
        self.individuals = []
        self.amount = amount
        self.quality = quality
        self.genome_length = genome_length
        self.mutation_rate = mutation_rate

    def init_population(self):
        for i in range(self.amount):
            individual = Individual(np.random.uniform(-100+self.quality,100+self.quality, self.genome_length))
            self.individuals.append(individual)

    def fitness_evaluation(self, individuals):
        for ind in individuals:
            ind.fitness = np.average(ind.genome)

    def choose_parents(self):
        parents = set()
        for _ in range(self.amount):
            contenders = random.sample(self.individuals, 2)
            winner = max(contenders, key=lambda ind: ind.fitness)
            parents.add(winner)
        return list(parents)

    def single_point_crossover(self, g1, g2):
        point = random.randint(1, self.genome_length - 1)
        return (
            np.concatenate((g1[:point], g2[point:])),
            np.concatenate((g2[:point], g1[point:]))
        )

    def mutate(self, genome):
        return np.array([
            gene + np.random.uniform(-1, 1) if random.random() < self.mutation_rate else gene
            for gene in genome
        ])

    def create_descendants(self, parents):
        descendants = []
        for i in range(0, len(parents), 2):
            p1, p2 = parents[i], parents[(i + 1) % len(parents)]
            child1_genome, child2_genome = self.single_point_crossover(p1.genome, p2.genome)
            child_count = random.randint(0, 2)
            if child_count > 0:
                descendants.append(Individual(self.mutate(child1_genome)))
            if child_count > 1:
                descendants.append(Individual(self.mutate(child2_genome)))
        return descendants

    def get_the_best_individual(self):
        return max(self.individuals, key=lambda ind: ind.fitness)

    def simulate(self, iterations, last_alive=False, min_fitness=50):
        self.init_population()
        for i in range(iterations):
            self.fitness_evaluation(self.individuals)
            avg_fitness = np.average([individ.fitness for individ in self.individuals])
            if last_alive and len(self.individuals)==0 or avg_fitness < min_fitness:
                return None

            parents = self.choose_parents()
            descendants = self.create_descendants(parents)
            self.fitness_evaluation(descendants)
            self.select_next_generation(descendants)



    def select_next_generation(self, descendants):
        combined = self.individuals + descendants
        combined.sort(key=lambda ind: ind.fitness, reverse=True)
        self.individuals = combined[:self.amount]