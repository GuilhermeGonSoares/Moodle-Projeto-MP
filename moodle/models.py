import datetime

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models

"""
@package moodle

@brief Aqui são definidos os models para relações do banco de dados.
"""


class Departamento(models.Model):
    """
    Define os atributos do elemento Departamento no banco de dados.
    @param models.Model
    """
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Professor(models.Model):
    """
    Define os atributos do elemento Professor no banco de dados.
    @param models.Model
    """
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name


class Aluno(models.Model):
    """
    Define os atributos do elemento Aluno no banco de dados.
    @param models.Model
    """
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name


class Disciplina(models.Model):
    """
    Define os atributos do elemento Disciplina no banco de dados.
    @param models.Model
    """
    nome = models.CharField(max_length=100)
    professor = models.ForeignKey(
        Professor, on_delete=models.SET_NULL, null=True)
    aluno = models.ManyToManyField(Aluno, through='Inscricao')
    quantidade_alunos = models.IntegerField(default=0)

    def __str__(self):
        return self.nome


class Inscricao(models.Model):
    """
    Define os atributos do elemento Inscrição no banco de dados.
    @param models.Model
    """
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)

    def __str__(self):
        return self.disciplina.nome + ' - ' + self.aluno.user.name


class Questao(models.Model):
    """
    Define os atributos do elemento Questão no banco de dados.
    @param models.Model
    """
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
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self):
        return self.enunciado


class Alternativa(models.Model):
    """
    Define os atributos do elemento Alternativa no banco de dados.
    @param models.Model
    """
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
    """
    Define os atributos do elemento Prova no banco de dados.
    @param models.Model
    """
    nota_total = models.IntegerField()
    disciplina = models.ForeignKey(
        Disciplina, null=True, on_delete=models.SET_NULL)
    questao = models.ManyToManyField(Questao)
    descricao = models.TextField(null=True, blank=True)
    finalizada = models.BooleanField(default=False)
    data = models.DateTimeField(default=datetime.datetime.now)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao


class CadernoResposta(models.Model):
    """
    Define os atributos do elemento CadernoResposta no banco de dados.
    @param models.Model
    """
    resposta_choices = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E')
    )

    resposta_aluno = models.CharField(max_length=1, choices=resposta_choices)
    questao = models.ForeignKey(Questao, on_delete=models.CASCADE)
    acertou = models.BooleanField(default=False)
    desempenho = models.ForeignKey('Desempenho', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        gabarito = self.questao.gabarito
        if gabarito == self.resposta_aluno:
            self.acertou = True
        super().save(*args, **kwargs)


class Desempenho(models.Model):
    """
    Define os atributos do elemento Desempenho no banco de dados.
    @param models.Model
    """
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    prova = models.ForeignKey(Prova, on_delete=models.CASCADE)
    nota = models.IntegerField()
    prova_finalizada = models.BooleanField(default=False)
    data = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return 'Aluno: ' + self.aluno.user.name + ' Prova: ' + self.prova.descricao
