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

  enunciado = forms.CharField(max_length=255)
  peso = forms.IntegerField()
  gabarito = forms.ChoiceField(choices=opcoes_choices)


  alternativa_A = forms.CharField(max_length=255)
  alternativa_B = forms.CharField(max_length=255)
  alternativa_C = forms.CharField(max_length=255)
  alternativa_D = forms.CharField(max_length=255)
  alternativa_E = forms.CharField(max_length=255)
