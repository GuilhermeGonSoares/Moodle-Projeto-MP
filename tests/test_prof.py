import pytest
from moodle.models import Professor, Departamento
from user.models import User

"""
@package tests

Suite de testes para testar os relacionamentos entre
o model Professor e o resto da plataforma
"""


@pytest.mark.django_db
def test_prof():
    assert Professor.objects.count() == 0


@pytest.mark.django_db
def test_new_prof():
    depto = Departamento.objects.create(nome="Teste")
    user1 = User.objects.create_user("yan@yan.com", "Abc1234")
    user2 = User.objects.create_user("yan.com", "Abc1234")
    d = Professor.objects.create(user=user1, departamento=depto)
    assert d.user != user2


@pytest.mark.django_db
def test_new_prof2():
    depto = Departamento.objects.create(nome="Teste")
    user1 = User.objects.create_user("yan@yan.com", "Abc1234")
    d = Professor.objects.create(user=user1, departamento=depto)
    assert Professor.objects.count() == 1


@pytest.mark.django_db
@pytest.mark.xfail
def test_create_invalid_prof1():
    depto = Departamento.objects.create(nome="Teste")
    user1 = User.objects.create_user("yan@yan.com", "Abc1234")
    d = Professor.objects.create(user=user1)
    assert User.objects.count() == 0


@pytest.mark.django_db
@pytest.mark.xfail
def test_create_invalid_prof2():
    depto = Departamento.objects.create(nome="Teste")
    user1 = User.objects.create_user("yan@yan.com", "Abc1234")
    d = Professor.objects.create(depto=user1, user=depto)
    assert User.objects.count() == 0


@pytest.mark.django_db
def test_new_prof3():
    depto = Departamento.objects.create(nome="Teste")
    user1 = User.objects.create_user("yan@yan.com", "Abc1234")
    d = Professor.objects.create(user=user1, departamento=depto)
    v = Professor.objects.all()[0].user
    assert v == user1


@pytest.mark.django_db
def test_new_prof4():
    depto = Departamento.objects.create(nome="Teste")
    user1 = User.objects.create_user("yan@yan.com", "Abc1234")
    d = Professor.objects.create(user=user1, departamento=depto)
    v = Professor.objects.all()[0].departamento
    assert v == depto
