
import datetime

from django.views import generic

from moodle import models
from util.LoginRequired import MyLoginRequired


class PseudoDesempenho:
  def __init__(self, nota, data):
    self.nota = nota
    self.data = data

class CursoListView(MyLoginRequired, generic.ListView):
  context_object_name = 'cursos'
  queryset = models.Disciplina.objects.all()
  template_name = 'moodle/home.html'

  def get_template_names(self):
    user = self.request.user
    if user.user_type == 'Professor':
      self.template_name = 'moodle/home_professor.html'
      return self.template_name

    return self.template_name



  def get_queryset(self):
    user = self.request.user
    if user.user_type == 'Professor':
      professor = user.professor
      queryset = self.queryset.filter(professor=professor)
      return queryset

    aluno = user.aluno
    queryset = self.queryset.filter(aluno=aluno)
    return queryset


class CursoDetailView(MyLoginRequired, generic.DetailView):
    model = models.Disciplina
    context_object_name = 'disciplina'
    template_name = 'moodle/curso/curso_detail.html'

    def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      provas = self.get_object(self.queryset).prova_set.filter(finalizada=False)
      provas_finalizadas = self.get_object(self.queryset).prova_set.filter(finalizada=True)
      aluno = self.request.user.aluno
      provas_diponiveis = []
      provas_feitas = []
      for prova in provas:
        desempenho = prova.desempenho_set.filter(aluno=aluno)
        if desempenho:
          provas_feitas.append((prova, desempenho[0], True))
        else:
          provas_diponiveis.append(prova)

      for prova in provas_finalizadas:
        desempenho = prova.desempenho_set.filter(aluno=aluno)
        if desempenho:
          provas_feitas.append((prova, desempenho[0], True))
        else:
          desempenho = PseudoDesempenho(0, prova.data)
          provas_feitas.append((prova, desempenho, False))

      context['provas_diponiveis'] = provas_diponiveis
      context['provas_feitas'] = provas_feitas
      context['aluno'] = aluno
      return context

