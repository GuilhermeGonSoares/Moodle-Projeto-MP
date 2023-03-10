import datetime

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpRequest
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import generic

from moodle import models
from moodle.forms import ProvaForm
from util.LoginRequired import MyLoginRequired
from util.ProfessorRequired import ProfessorRequiredMixin


class PseudoDesempenho:
  def __init__(self, nota, data):
    self.nota = nota
    self.data = data

class ProvaListView(ProfessorRequiredMixin, generic.ListView):
  context_object_name = 'provas'
  queryset = models.Prova.objects.all()
  template_name = 'moodle/prova/lista-provas.html'

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['provasabertas'] = self.get_queryset().filter(finalizada=False)
    context['provasfinalizadas'] = self.get_queryset().filter(finalizada=True)
    return context

  def get_queryset(self):
    queryset = self.queryset
    professor = self.request.user.professor
    queryset = queryset.filter(professor=professor)
    return queryset


class ProvaCreateView(MyLoginRequired, ProfessorRequiredMixin, generic.CreateView):
    model = models.Prova
    form_class = ProvaForm
    template_name = 'moodle/prova/create.html'
    success_url = reverse_lazy('moodle:provas')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['professor'] = self.request.user.professor
        return kwargs
      
    def form_valid(self, form):
      print("ESTOU AQUI NO FORM_VALID")
      prova = form.save(commit=False)
      questoes = [models.Questao.objects.get(pk=int(id)) for id in self.request.POST.getlist('questoes')]
      prova.nota_total = 0
      prova.professor=self.request.user.professor
      prova.save()
      
      for questao in questoes:
        prova.nota_total += questao.peso
      prova.questao.set(questoes)
      
      return super().form_valid(form)

class ProvaUpdateView(MyLoginRequired, ProfessorRequiredMixin, generic.UpdateView):
    model = models.Prova
    form_class = ProvaForm
    template_name = 'moodle/prova/update.html'
    success_url = reverse_lazy('moodle:provas')

    def get_form_kwargs(self):
      kwargs = super().get_form_kwargs()
      kwargs['professor'] = self.request.user.professor
      return kwargs
  

    def form_valid(self, form):
      prova = form.save(commit=False)
      prova.disciplina = form.cleaned_data['disciplina']
      prova.descricao = form.cleaned_data['descricao']
      questoes = form.cleaned_data['questoes']
      prova.save()
      
      prova.questao.set(questoes)
      
      prova.nota_total = 0
      for questao in questoes:
        prova.nota_total += questao.peso
      
      
      return super().form_valid(form)


@login_required(login_url='user:login')
def finalizarProva(req, prova_id):
  try:
    prova = models.Prova.objects.get(pk=prova_id)
    prova.finalizada = True
    prova.data = datetime.datetime.now()
    prova.save()
  except ObjectDoesNotExist:
    raise Http404('Objects not found in database')

  return redirect('moodle:provas')

@login_required(login_url='user:login')
def exibirProva(req, prova_id):
  prova = models.Prova.objects.get(pk=prova_id)
  questoes = prova.questao.all()


  return render(req, 'moodle/prova/fazer_prova.html', {
    'questoes': questoes,
    'prova': prova,
  })
@login_required(login_url='user:login')
def corrigirProva(req: HttpRequest, prova_id):
  prova = models.Prova.objects.get(pk=prova_id)
  dados = req.POST
  questoes_resolvidas = []
  pk = prova.disciplina.id
  desempenho_aluno = models.Desempenho.objects.create(
    aluno = req.user.aluno,
    prova=prova,
    nota=0,
    prova_finalizada=True
  )
  for q in dados.keys():
    if 'quest' in q:
      questoes_resolvidas.append(dados.get(q))

  for i, questao in enumerate(prova.questao.all()):
    correto = False
    if questoes_resolvidas[i] == questao.gabarito:
      correto = True

    caderno_resposta = models.CadernoResposta.objects.create(
      resposta_aluno=questoes_resolvidas[i],
      acertou=correto,
      desempenho=desempenho_aluno,
      questao=questao
    )

    if correto:
      desempenho_aluno.nota += questao.peso
      desempenho_aluno.save()


  return redirect(reverse('moodle:curso-detail', args=(pk,)), context={'desempenho': desempenho_aluno})

def alunos_provas_feitas(req, prova_id):
  prova = models.Prova.objects.get(pk=prova_id)
  alunos = prova.disciplina.aluno.all()
  prova_finalizada = []
  for aluno in alunos:
    desempenho = prova.desempenho_set.filter(aluno=aluno)
    if desempenho:
      prova_finalizada.append((aluno, desempenho.first(), True))
    else:
      desempenho = PseudoDesempenho(0, prova.data)
      prova_finalizada.append((aluno, desempenho, False))

  print(prova_finalizada)
  return render(req, 'moodle/prova/alunos_provas.html', {
    'prova_finalizada': prova_finalizada,
    'prova': prova,
  })

def relatorioProva(req, prova_id):
  prova = models.Prova.objects.get(pk=prova_id)
  aluno = req.user.aluno
  desempenho = prova.desempenho_set.filter(aluno=aluno)
  respostas_aluno = desempenho[0].cadernoresposta_set.all()
  relatorio = []
  for resp in respostas_aluno:
    relatorio.append((resp.questao, resp.questao.peso, resp.questao.gabarito, resp.resposta_aluno))

  return render(req, 'moodle/curso/relatorio_prova.html', {
    'relatorio': relatorio,
  })