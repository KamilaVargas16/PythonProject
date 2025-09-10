import pytest
import Modulo_2.ejercicio11

def test_cedula_valida():
    # Ejemplos con suma par → válidos
    assert Modulo_2.ejercicio11.validar_cedula_test("222222") is True   # suma = 12 → par
    assert Modulo_2.ejercicio11.validar_cedula_test("111111") is True   # suma = 6 → par

def test_cedula_invalida_longitud():
    assert Modulo_2.ejercicio11.validar_cedula_test("123") is False   # muy corta
    assert Modulo_2.ejercicio11.validar_cedula_test("12345678901") is False  # muy larga

def test_cedula_con_letras():
    assert Modulo_2.ejercicio11.validar_cedula_test("12a456") is False

def test_cedula_suma_impar():
    # Ejemplo con suma impar → inválido
    assert Modulo_2.ejercicio11.validar_cedula_test("123456") is False  # suma = 21 → impar
    assert Modulo_2.ejercicio11.validar_cedula_test("111112") is False  # suma = 7 → impar
