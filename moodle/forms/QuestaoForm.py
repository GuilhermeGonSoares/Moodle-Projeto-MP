from django import forms

from moodle.models import Departamento


class QuestaoAlternativasForm(forms.Form):
    def __init__(self, instance=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if instance:
            self.fields['enunciado'].initial = instance.enunciado
            self.fields['peso'].initial = instance.peso
            self.fields['gabarito'].initial = instance.gabarito
            self.fields['departamento'].initial = instance.departamento

    opcoes_choices = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E')
    )

    enunciado = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class': 'form-control'}))
    peso = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'style': 'width:25%'}))
    gabarito = forms.ChoiceField(choices=opcoes_choices, widget=forms.Select(attrs={'class': 'form-control', 'style': 'width:7%'}))

    alternativa_A = forms.CharField(max_length=255, label='Alternativa A', widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width:50%'}))
    alternativa_B = forms.CharField(max_length=255, label='Alternativa B', widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width:50%'}))
    alternativa_C = forms.CharField(max_length=255, label='Alternativa C', widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width:50%'}))
    alternativa_D = forms.CharField(max_length=255, label='Alternativa D', widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width:50%'}))
    alternativa_E = forms.CharField(max_length=255, label='Alternativa E', widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width:50%'}))
