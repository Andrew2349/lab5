from django import forms

from simulation_app.models import Simulation


class SimulationForm(forms.ModelForm):
    amount = forms.IntegerField(min_value=2, max_value=1000)
    genome_length = forms.IntegerField(min_value=2, max_value=1000)
    mutation_rate = forms.DecimalField(min_value=0, max_value=1, step_size=0.01)
    iterations = forms.IntegerField(min_value=1, max_value=1000)

    class Meta:
        model = Simulation
        fields = '__all__'
