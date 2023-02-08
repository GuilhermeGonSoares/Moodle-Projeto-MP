from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic

from moodle import models
from moodle.forms import ProvaForm


class ProvaListView(generic.ListView):
  context_object_name = 'provas'
  queryset = models.Prova.objects.filter(finalizada=False)
  template_name = 'moodle/prova/lista-provas.html'


class ProvaCreateView(generic.CreateView):
    model = models.Prova
    form_class = ProvaForm
    template_name = 'moodle/prova/create.html'
    success_url = reverse_lazy('moodle:provas')

    def form_valid(self, form):
      prova = form.save(commit=False)
      questoes = [models.Questao.objects.get(pk=int(id)) for id in self.request.POST.getlist('questao')]
      prova.nota_total = 0
      prova.user = self.request.user
      prova.save()

      for questao in questoes:
        prova.nota_total += questao.peso

      prova.questao.set(questoes)

      return super().form_valid(form)

class ProvaUpdateView(generic.UpdateView):
    model = models.Prova
    form_class = ProvaForm
    template_name = 'moodle/prova/create.html'
    success_url = reverse_lazy('moodle:provas')

    def form_valid(self, form):
      prova = form.save(commit=False)
      questoes = [models.Questao.objects.get(pk=int(id)) for id in self.request.POST.getlist('questao')]
      prova.nota_total = 0
      prova.user = self.request.user
      prova.save()

      for questao in questoes:
        prova.nota_total += questao.peso

      prova.questao.set(questoes)

      return super().form_valid(form)


def finalizarProva(req, prova_id):
  try:
    prova = models.Prova.objects.get(pk=prova_id)
    prova.finalizada = True
    prova.save()
  except ObjectDoesNotExist:
    raise Http404('Objects not found in database')

  return redirect('moodle:provas')


def exibirProva(req, prova_id):
  prova = models.Prova.objects.get(pk=prova_id)
  questoes = prova.questao.all()


  return render(req, 'moodle/prova/fazer_prova.html', {
    'questoes': questoes,
    'prova': prova,
  })

def corrigirProva(req: HttpRequest, prova_id):
  dados = req.POST
  print(dados.keys())
  for q in dados.keys():
    ...
