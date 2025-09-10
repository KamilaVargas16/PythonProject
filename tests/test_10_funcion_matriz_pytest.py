import pytest
import Modulo_2.ejercicio10

def test_transpuesta_bucles():
    matriz = [[1, 2, 3], [4, 5, 6]]
    esperado = [[1, 4], [2, 5], [3, 6]]
    assert Modulo_2.ejercicio10.transpuesta(matriz) == esperado

def test_transpuesta_comprehension():
    matriz = [[7, 8], [9, 10], [11, 12]]
    esperado = [[7, 9, 11], [8, 10, 12]]
    assert Modulo_2.ejercicio10.transpuesta_comprehension(matriz) == esperado
