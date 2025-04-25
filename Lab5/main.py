from population import Population



def main():
    population = Population(1000, 100, 0.02, 15)
    population.simulate(100, True, 0)
    print(population.get_the_best_individual())


if __name__ == '__main__':
    main()
