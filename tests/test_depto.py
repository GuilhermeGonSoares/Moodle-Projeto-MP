import pytest
from moodle.models import Departamento

"""
@package tests

Suite de testes para testar os relacionamentos entre
o model Departamento e o resto da plataforma
"""


@pytest.mark.django_db
def test_dpto():
    assert Departamento.objects.count() == 0


@pytest.mark.django_db
def test_new_dpto():
    d = Departamento.objects.create(nome="test")
    assert d.nome == "test"
    assert d.nome != "errado"


@pytest.mark.django_db
def test_new_dpto2():
    d = Departamento.objects.create(nome="test")
    assert Departamento.objects.count() == 1


@pytest.mark.django_db
def test_create_invalid_dpto():
    d = Departamento.objects.create(nome="test")
    assert d.nome != "errado"


@pytest.mark.django_db
def test_new_dpto3():
    d = Departamento.objects.create(nome="test")
    v = Departamento.objects.all()[0].nome
    assert v == "test"
