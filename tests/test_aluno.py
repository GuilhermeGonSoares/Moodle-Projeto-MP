import pytest
from moodle.models import Aluno
from user.models import User

"""
@package tests

Suite de testes para testar os relacionamentos entre
o model Aluno e o resto da plataforma
"""


@pytest.mark.django_db
def test_aluno():
    assert Aluno.objects.count() == 0


@pytest.mark.django_db
def test_new_aluno():
    user1 = User.objects.create_user("yan@yan.com", "Abc1234")
    user2 = User.objects.create_user("yan.com", "Abc1234")
    d = Aluno.objects.create(user=user1)
    assert d.user != user2


@pytest.mark.django_db
def test_new_aluno2():
    user1 = User.objects.create_user("yan@yan.com", "Abc1234")
    d = Aluno.objects.create(user=user1)
    assert Aluno.objects.count() == 1


@pytest.mark.django_db
@pytest.mark.xfail
def test_create_invalid_aluno1():
    user1 = User.objects.create_user("yan@yan.com", "Abc1234")
    d = Aluno.objects.create(user=user1)
    assert User.objects.count() == 0


@pytest.mark.django_db
@pytest.mark.xfail
def test_create_invalid_aluno2():
    user1 = User.objects.create_user("yan@yan.com", "Abc1234")
    d = Aluno.objects.create(user="")
    assert User.objects.count() == 0


@pytest.mark.django_db
def test_new_aluno3():
    user1 = User.objects.create_user("yan@yan.com", "Abc1234")
    d = Aluno.objects.create(user=user1)
    v = Aluno.objects.all()[0].user
    assert v == user1
