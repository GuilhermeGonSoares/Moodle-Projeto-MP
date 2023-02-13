from django import forms
from django.core.exceptions import ValidationError
from moodle.models import Alternativa, Prova, Questao, Disciplina


class ProvaForm(forms.ModelForm):
    disciplina = forms.ModelChoiceField(
        queryset=Disciplina.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Disciplina'
    )
    questoes = forms.ModelMultipleChoiceField(
        queryset=Questao.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Questões'
    )
    descricao = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control'}),
        label='Descrição'
    )

    class Meta:
        model = Prova
        fields = ('disciplina', 'questoes', 'descricao')

    def __init__(self, *args, **kwargs):
        professor = kwargs.pop('professor')
        super().__init__(*args, **kwargs)
        self.fields['disciplina'].queryset = Disciplina.objects.filter(professor=professor)
        self.fields['questoes'].queryset = Questao.objects.filter(departamento=professor.departamento)
        