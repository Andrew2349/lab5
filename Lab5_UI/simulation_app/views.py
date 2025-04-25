from django.shortcuts import render, redirect

from simulation_app.population import Population
from simulation_app.forms import SimulationForm
from simulation_app.models import Result


def simulation(request):
    if request.method == 'POST':
        form = SimulationForm(request.POST)
        if not form.is_valid():
            return render(request, 'index.html', {'form': form})
        sim = form.save()
        population = Population(sim.amount, sim.genome_length, sim.mutation_rate, sim.quality)
        population.simulate(sim.iterations, sim.last_alive, sim.min_fitness)
        individ = population.get_the_best_individual()
        result = Result.objects.create(simulation=sim, fitness=individ.fitness, genome=str(individ.genome))
        return redirect(f'/{result.id}')
    form = SimulationForm()
    return render(request, 'index.html', {'form': form})

def load_simulation(request, result_id):
    result = Result.objects.filter(id=result_id).first()
    if result is None:
        return redirect("/")
    form = SimulationForm(instance=result.simulation)
    return render(request, 'index.html', {'form': form,'individual': result})