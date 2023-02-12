from main import *

"""
@package tests

Suite de testes para testar os relacionamentos entre
o model Caderno e o resto da plataforma
"""


@pytest.mark.django_db
def test_new_caderno():
    assert CadernoResposta.objects.count() == 0


@pytest.mark.django_db
def test_new_caderno1(create_caderno):
    caderno = create_caderno
    assert caderno.acertou == False


@pytest.mark.django_db
def test_new_caderno2(create_caderno):
    caderno = create_caderno
    assert caderno.resposta_aluno == "Resposta teste"


@pytest.mark.django_db
def test_new_caderno3(create_caderno):
    caderno = create_caderno
    assert CadernoResposta.objects.count() == 1


@pytest.mark.django_db
def test_new_caderno4(create_caderno, create_desempenho):
    caderno = create_caderno
    assert caderno.desempenho == create_desempenho


@pytest.mark.django_db
def test_new_caderno4(create_caderno, create_question):
    caderno = create_caderno
    assert caderno.questao == create_question
