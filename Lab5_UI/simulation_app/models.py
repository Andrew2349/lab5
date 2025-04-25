from django.db import models

class Simulation(models.Model):
    amount = models.IntegerField()
    genome_length = models.IntegerField()
    mutation_rate = models.FloatField()
    quality = models.IntegerField()
    iterations = models.IntegerField()
    last_alive = models.BooleanField()
    min_fitness = models.FloatField()

class Result(models.Model):
    simulation = models.ForeignKey(Simulation, on_delete=models.CASCADE)
    fitness = models.FloatField()
    genome = models.TextField()