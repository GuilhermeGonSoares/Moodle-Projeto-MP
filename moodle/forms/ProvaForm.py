from django import forms

from moodle.models import Alternativa, Prova, Questao


class ProvaForm(forms.ModelForm):
    questao = forms.ModelMultipleChoiceField(
        queryset=Questao.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Prova
        fields = ['disciplina', 'questao', 'descricao']
