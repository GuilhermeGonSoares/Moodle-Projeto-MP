from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
  is_teacher = models.BooleanField(default=False)


class Departamento(models.Model):
  nome = models.CharField(max_length=100)

  def __str__(self):
    return self.nome

class Professor(models.Model):
  user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
  departamento = models.OneToOneField(Departamento, on_delete=models.CASCADE)

  def __str__(self):
    return self.user.first_name


class Aluno(models.Model):
  matricula = models.CharField(max_length=9, primary_key=True)
  user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
  idade = models.IntegerField()

  def __str__(self):
    return self.user.first_name

class Disciplina(models.Model):
  nome = models.CharField(max_length=100)
  professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True)
  aluno = models.ManyToManyField(Aluno, through='Inscricao')
  quantidade_alunos = models.IntegerField(default=0)

  def __str__(self):
    return self.nome

class Inscricao(models.Model):
  disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
  aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)

  def __str__(self):
    return self.disciplina.nome + ' - ' + self.aluno.user.first_name


class Questao(models.Model):
  gabarito_choices = (
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
    ('E', 'E')
  )

  peso = models.IntegerField()
  gabarito = models.CharField(max_length=1, choices=gabarito_choices)
  enunciado = models.TextField()
  departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

  def __str__(self):
    return self.enunciado

class Alternativa(models.Model):
  opcoes = (
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
    ('E', 'E')
  )

  questao = models.ForeignKey(Questao, on_delete=models.CASCADE)
  texto_alternativa = models.CharField(max_length=255)
  alternativa = models.CharField(max_length=1, choices=opcoes)

  def __str__(self):
    return self.texto_alternativa

class Prova(models.Model):
  user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

  nota_total = models.IntegerField()
  disciplina = models.ForeignKey(Disciplina, null=True, on_delete=models.SET_NULL)
  questao = models.ManyToManyField(Questao)
  descricao = models.TextField(null=True, blank=True)
  finalizada = models.BooleanField(default=False)

class CadernoResposta(models.Model):
  resposta_choices = (
    ('A', 'A'),
    ('B', 'B'),
    ('C', 'C'),
    ('D', 'D'),
    ('E', 'E')
  )

  resposta_aluno = models.CharField(max_length=1, choices=resposta_choices)
  questao = models.OneToOneField(Questao, on_delete=models.CASCADE)
  acertou = models.BooleanField(default=False)
  desempenho = models.ForeignKey('Desempenho', on_delete=models.CASCADE)

  def save(self, *args, **kwargs):
    gabarito = self.questao.gabarito
    if gabarito == self.resposta_aluno:
      self.acertou = True;
    super().save(*args, **kwargs)

class Desempenho(models.Model):
  aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
  prova = models.OneToOneField(Prova, on_delete=models.CASCADE)
  nota = models.IntegerField()
  prova_finalizada = models.BooleanField(default=False)
