from main import *

"""
@package tests

Suite de testes para testar os relacionamentos entre
o model Prova e o resto da plataforma
"""


def test_create_prova(create_prova):
    prova = Prova.objects.get(id=create_prova.id)
    assert Prova.objects.count() == 1


def test_prova_nota(create_prova):
    prova = Prova.objects.get(id=create_prova.id)
    assert prova.nota_total == 10


def test_prova_desc(create_prova):
    prova = Prova.objects.get(id=create_prova.id)
    assert prova.descricao == 'Descrição da prova'


def test_prova_quest(create_prova):
    prova = Prova.objects.get(id=create_prova.id)
    assert prova.questao.count() == 1


def test_prova_enun(create_prova):
    prova = Prova.objects.get(id=create_prova.id)
    assert prova.questao.first().enunciado == 'Enunciado da questão'
