import pytest
from user.models import UserManager, User

"""
@package tests

Suite de testes para testar os relacionamentos entre
o model User e o resto da plataforma
"""


@pytest.mark.django_db
def test_user():
    assert User.objects.count() == 0


@pytest.mark.django_db
def test_create_user():
    user = User
    user.email = "yan@test.com"
    UserManager.create_user(user.objects, user.email)
    assert User.objects.all()[0].email == "yan@test.com"


@pytest.mark.django_db
def test_create_user2():
    User.objects.create_user("yan@yan2.com", "abc1234")
    assert User.objects.count() == 1


@pytest.mark.xfail
@pytest.mark.django_db
def test_create_invalid_user():
    user = User
    user.email = ""
    UserManager.create_user(user.objects, user.email)
    assert User.objects.count() == 0


@pytest.mark.django_db
def test_create_superuser():
    user = User
    UserManager.create_superuser(user.objects, "yan", "yan")
    assert User.objects.count() == 1


@pytest.mark.xfail
@pytest.mark.django_db
def test_create_invalid_superuser():
    user = User
    user.email = ""
    UserManager.create_superuser(user.objects, "", "")
    assert User.objects.count() == 0
