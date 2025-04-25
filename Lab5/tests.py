import numpy as np

from individual import Individual
from population import Population

import unittest


class Population_Test(unittest.TestCase):
    def test_fitness_evaluation(self):
        population = Population(1, 10, 0, 0)
        genome = [32, -14, 44, 21, -42, 64, 77, 12, -66, 41]
        fitness = 16.9
        individual = Individual(genome)
        population.fitness_evaluation([individual])

        self.assertEqual(individual.fitness, fitness)

    def test_choose_parents(self):
        population = Population(10, 10, 0, 0)
        population.init_population()
        population.fitness_evaluation(population.individuals)
        parents = population.choose_parents()
        avg_population = np.average([individ.fitness for individ in population.individuals])
        avg_parents = np.average([parent.fitness for parent in parents])

        self.assertGreater(avg_parents,avg_population)

    def assertListNotEqual(self, list1, list2):
        self.assertEqual(len(list1), len(list2))
        for i in range(len(list1)):
            if list1[i] != list2[i]:
                return
        raise AssertionError("lists are equal")

    def test_crossover(self):
        population = Population(1, 10, 0, 0)
        gen1 = [32, -14, 44, 21, -42, 64, 77, 12, -66, 41]
        gen2 = [-42, 24, 94, -51, 12, -84, 97, -19, 69, 91]
        gen_child1,gen_child2 = population.single_point_crossover(gen1, gen2)

        self.assertListNotEqual(gen_child1,gen_child2)
        self.assertListNotEqual(gen1,gen_child1)
        self.assertListNotEqual(gen1,gen_child2)
        self.assertListNotEqual(gen2,gen_child1)
        self.assertListNotEqual(gen2,gen_child2)

    def test_mutation(self):
        population = Population(1, 10, 1, 0)
        gen1 = [32, -14, 44, 21, -42, 64, 77, 12, -66, 41]
        gen2 = population.mutate(gen1)

        self.assertListNotEqual(gen1,gen2)

    def test_next_generation_selection(self):
        individ1 = Individual([100,100])
        individ2 = Individual([-100,-100])
        child1 = Individual([100,-100])
        child2 = Individual([-100,60])
        population = Population(2, 2, 0.5, 0)
        population.individuals = [individ1, individ2]
        population.fitness_evaluation(population.individuals)
        children = [child1, child2]
        population.fitness_evaluation(children)
        population.select_next_generation(children)

        self.assertIn(individ1, population.individuals)
        self.assertIn(child1, population.individuals)
        self.assertNotIn(individ2, population.individuals)
        self.assertNotIn(child2, population.individuals)

    def test_best_individual(self):
        individ1 = Individual([32, -14, 44, 21, -42, 64, 77, 12, -66, 41])
        individ2 = Individual([-42, 24, 94, -51, 12, -84, 97, -19, 69, 91])#у нього придатність вище
        population = Population(2, 10, 0.5, 0)
        population.individuals = [individ1, individ2]
        population.fitness_evaluation(population.individuals)
        better_individual = population.get_the_best_individual()
        self.assertEqual(individ2, better_individual)
