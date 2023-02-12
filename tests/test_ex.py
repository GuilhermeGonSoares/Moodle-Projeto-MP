import pytest

"""
@package tests

Suite de testes para assegurar que a ferramenta Pytest
está fucnionando corretamente
"""


@pytest.fixture
def fixture1():
    print("Fixture 1")
    return 1


@pytest.fixture
def yieldFixture():
    print("Start test")
    yield 6
    print("Stop test")


def testExample1():
    assert 1 == 1


def testExample2():
    assert True != False


def testExample3(fixture1):
    n = fixture1
    assert n == 1


def testExample4(yieldFixture):
    assert yieldFixture == 6
