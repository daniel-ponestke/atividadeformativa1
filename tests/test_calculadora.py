import pytest
from src.calculadora import somar, subtrair, multiplicar, dividir


def test_somar_dois_numeros_positivos():
    assert somar(2, 3) == 5


def test_somar_com_numero_negativo():
    assert somar(-5, 10) == 5


def test_subtrair_dois_numeros():
    assert subtrair(10, 4) == 6


def test_multiplicar_dois_numeros():
    assert multiplicar(6, 7) == 42


def test_dividir_dois_numeros():
    assert dividir(10, 2) == 5


def test_dividir_por_zero_levanta_erro():
    with pytest.raises(ValueError):
        dividir(10, 0)