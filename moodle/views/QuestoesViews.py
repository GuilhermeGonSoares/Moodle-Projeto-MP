from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View, generic

from moodle import models


class QuestoesListView(generic.ListView):
  context_object_name = 'questoes'
  queryset = models.Questao.objects.all()
  template_name = 'moodle/questoes/lista-questoes.html'

class QuestoesCreateView(generic.CreateView):
  model = models.Questao
  fields = ['peso', 'gabarito', 'enunciado', 'departamento']
  template_name = 'moodle/questoes/create.html'
  success_url = reverse_lazy('moodle:questoes')

class QuestoesUpdateView(generic.UpdateView):
  model = models.Questao
  fields = ['peso', 'gabarito', 'enunciado', 'departamento']
  template_name = 'moodle/questoes/create.html'
  success_url = reverse_lazy('moodle:questoes')

class QuestoesDeleteView(generic.DeleteView):
  model = models.Questao
  template_name = 'moodle/questoes/delete.html'
  success_url = reverse_lazy('moodle:questoes')
