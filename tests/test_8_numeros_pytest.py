import pytest
import Modulo_2.ejercicio8


def test_procesar_numeros_lista_base():
    numeros = [-5, 10, -15, 20, -25, 30]
    positivos, cuadrados, signos = Modulo_2.ejercicio8.procesar_numeros(numeros)

    assert positivos == [10, 20, 30]
    assert cuadrados == [25, 100, 225, 400, 625, 900]
    assert signos == ["negativo", "positivo", "negativo", "positivo", "negativo", "positivo"]


@pytest.mark.parametrize(
    "entrada, esperado",
    [
        ([1, -2, 0], ([1], [1, 4, 0], ["positivo", "negativo", "positivo"])),
        ([], ([], [], [])),  # lista vacía
        ([-1, -2, -3], ([], [1, 4, 9], ["negativo", "negativo", "negativo"])),
        ([5], ([5], [25], ["positivo"])),
    ],
)
def test_parametrizado_procesar_numeros(entrada, esperado):
    assert Modulo_2.ejercicio8.procesar_numeros(entrada) == esperado
