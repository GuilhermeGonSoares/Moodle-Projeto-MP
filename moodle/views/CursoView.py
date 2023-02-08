from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic

from moodle import models


class CursoListView(generic.ListView):
  context_object_name = 'cursos'
  queryset = models.Disciplina.objects.all()
  template_name = 'moodle/home.html'

  def get_queryset(self):
    user = self.request.user
    print(user.is_teacher)
    if user.is_teacher:
      professor = user.professor
      queryset = self.queryset.filter(professor=professor)
      return queryset

    aluno = user.aluno
    queryset = self.queryset.filter(aluno=aluno)
    print(queryset)
    return queryset

class CursoDetailView(generic.DetailView):
    model = models.Disciplina
    context_object_name = 'disciplina'
    template_name = 'moodle/curso/curso_detail.html'

    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['provas'] = self.get_object(self.queryset).prova_set.filter(finalizada=False)
      return context

