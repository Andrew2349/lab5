class Individual:
    def __init__(self, genome):
        self.genome = genome
        self.fitness = 0
    def __repr__(self):
        return f"Genome: {self.genome}\nFitness: {self.fitness}"
