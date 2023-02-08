from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View, generic
from django.views.generic.edit import FormMixin

from moodle import models
from moodle.forms import QuestaoAlternativasForm
from util.LoginRequired import MyLoginRequired
from util.ProfessorRequired import ProfessorRequiredMixin


class QuestoesListView(MyLoginRequired, ProfessorRequiredMixin, generic.ListView):
  context_object_name = 'questoes'
  #FILTRAR PELO DEPARTAMENTO DO PROFESSOR
  queryset = models.Questao.objects.all()
  template_name = 'moodle/questoes/lista-questoes.html'

  def get_queryset(self):
      queryset = self.queryset
      current_user = self.request.user
      if current_user.user_type == 'Professor':
        professor = current_user.professor
        queryset = queryset.filter(departamento=professor.departamento)
        return queryset

      return queryset


class QuestaoAlternativasCreateView(MyLoginRequired, ProfessorRequiredMixin, View):
  def get(self, request, *args, **kwargs):
    form = QuestaoAlternativasForm()
    return render(request, 'moodle/questoes/create.html', {'form': form})

  def post(self, request, *args, **kwargs):
    form = QuestaoAlternativasForm(data=request.POST)
    professor = self.request.user.professor

    if form.is_valid():
      # Salvar dados da questão
      questao = models.Questao.objects.create(
        enunciado=form.cleaned_data['enunciado'],
        peso=form.cleaned_data['peso'],
        gabarito=form.cleaned_data['gabarito'],
        departamento=professor.departamento,
        professor=professor
      )


      # Salvar dados das alternativas
      alternativa_a = models.Alternativa.objects.create(
        questao=questao,
        texto_alternativa=form.cleaned_data['alternativa_A'],
        alternativa='A'
      )

      alternativa_b = models.Alternativa.objects.create(
        questao=questao,
        texto_alternativa=form.cleaned_data['alternativa_B'],
        alternativa='B'
      )

      alternativa_c = models.Alternativa.objects.create(
        questao=questao,
        texto_alternativa=form.cleaned_data['alternativa_C'],
        alternativa='C'
      )

      alternativa_d = models.Alternativa.objects.create(
        questao=questao,
        texto_alternativa=form.cleaned_data['alternativa_D'],
        alternativa='D'
      )
      alternativa_e = models.Alternativa.objects.create(
        questao=questao,
        texto_alternativa=form.cleaned_data['alternativa_E'],
        alternativa='E'
      )

      return redirect('moodle:questoes')

    return render(request, 'moodle/questoes/create.html', {'form': form})

class QuestoesDeleteView(generic.DeleteView):
  model = models.Questao
  template_name = 'moodle/questoes/delete.html'
  success_url = reverse_lazy('moodle:questoes')
