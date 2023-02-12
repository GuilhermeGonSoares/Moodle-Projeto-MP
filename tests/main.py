import pytest
from user.models import User
from moodle.models import (
    Aluno,
    Departamento,
    Desempenho,
    Disciplina,
    Inscricao,
    Professor,
    Prova,
    Questao,
    Alternativa,
    CadernoResposta
)

"""
@package tests

Aqui se encontram as fixtures da ferramenta Pytest,
que serão utilizadas nas suites de teste para a criação
de objetos para os testes dos models.

"""


@pytest.fixture
def create_department():
    """
    Fixture com o propósito de adicionar um 
    departamento válido ao banco de dados
    """
    department = Departamento.objects.create(nome='Department 1')
    return department


@pytest.fixture
def create_user():
    """
    Fixture com o propósito de adicionar um 
    usuário válido ao banco de dados
    """
    user = User.objects.create_user("test@test.com", "Abc123")
    return user


@pytest.fixture
def create_professor(create_department, create_user):
    """
    Fixture com o propósito de adicionar um 
    professor válido ao banco de dados

    @param create_department, create_user
    """
    professor = Professor.objects.create(
        user=create_user,
        departamento=create_department
    )
    return professor


@pytest.fixture
def create_aluno(create_user):
    """
    Fixture com o propósito de adicionar um 
    aluno válido ao banco de dados
    @param create_user
    """
    aluno = Aluno.objects.create(user=create_user)
    return aluno


@pytest.fixture
def create_discipline(create_professor):
    """
    Fixture com o propósito de adicionar uma
    disciplina válida ao banco de dados
    @param create_professor
    """
    discipline = Disciplina.objects.create(
        nome='Discipline 1',
        professor=create_professor
    )
    return discipline


@pytest.fixture
def create_inscricao(create_discipline, create_aluno):
    """
    Fixture com o propósito de adicionar uma
    inscrição válida ao banco de dados
    @param create_disciplina, create_aluno
    """
    inscription = Inscricao.objects.create(
        disciplina=create_discipline,
        aluno=create_aluno
    )
    return inscription


@pytest.fixture
def create_question(create_department, create_professor):
    """
    Fixture com o propósito de adicionar uma
    questão válida ao banco de dados
    @param create_department, create_professor
    """
    question = Questao.objects.create(
        enunciado='What is a test?',
        gabarito='A',
        peso=1,
        departamento=create_department,
        professor=create_professor
    )
    return question


@pytest.fixture
def create_alternative(create_question):
    """
    Fixture com o propósito de adicionar uma 
    alternativa válida ao banco de dados
    @param question
    """
    alternative = Alternativa.objects.create(
        texto_alternativa='A test is a procedure',
        alternativa='A',
        questao=create_question
    )
    return alternative


@pytest.fixture
def create_prova(db):
    """
    Fixture com o propósito de adicionar uma 
    prova válida ao banco de dados

    @param db
    """
    departamento = Departamento.objects.create(nome='Department 1')
    professor = Professor.objects.create(
        user=User.objects.create_user("yan@yan.com", "Abc123"),
        departamento=departamento
    )
    questao = Questao.objects.create(
        peso=1,
        gabarito='A',
        enunciado='Enunciado da questão',
        departamento=departamento,
        professor=professor
    )
    prova = Prova.objects.create(
        nota_total=10,
        descricao='Descrição da prova',
        professor=professor
    )
    prova.questao.add(questao)

    return prova


@pytest.fixture
def create_desempenho(create_aluno, create_prova):
    """
    Fixture com o propósito de adicionar um 
    desempenho válido ao banco de dados

    @param create_aluno, create_prova
    """
    aluno = create_aluno
    prova = create_prova
    desempenho = Desempenho.objects.create(aluno=aluno, prova=prova, nota=5)

    return desempenho


@pytest.fixture
def create_caderno(create_question, create_desempenho):
    """
    Fixture com o propósito de adicionar um 
    caderno válido ao banco de dados

    @param create_question, create_desempenho
    """
    questao = create_question
    desempenho = create_desempenho
    resposta_aluno = "Resposta teste"
    acertou = False
    caderno = CadernoResposta.objects.create(
        questao=questao, desempenho=desempenho, resposta_aluno=resposta_aluno, acertou=acertou)
    return caderno
