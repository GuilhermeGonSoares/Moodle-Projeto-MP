from main import *

"""
@package tests

Suite de testes para testar os relacionamentos entre
o model Desempenho e o resto da plataforma
"""


@pytest.mark.django_db
def test_create_desempenho(create_desempenho):
    desempenho = create_desempenho
    assert desempenho.nota == 5


@pytest.mark.django_db
def test_create_desempenho2(create_desempenho):
    desempenho = create_desempenho
    assert desempenho.nota != 6


@pytest.mark.django_db
def test_create_desempenho3(create_desempenho):
    desempenho = create_desempenho
    assert type(desempenho.nota) == int
