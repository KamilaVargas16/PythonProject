import pytest
import Modulo_2.ejercicio6


@pytest.mark.parametrize(
    "frase, letra, esperado",
    [
        ("Hola SENA", "a", [3, 8]),       # Ejemplo dado
        ("banana", "a", [1, 3, 5]),       # varias repeticiones
        ("banana", "b", [0]),             # letra inicial
        ("banana", "n", [2, 4]),          # letra intermedia
        ("banana", "x", []),              # letra no existente
        ("AAAaaa", "a", [0, 1, 2, 3, 4, 5]),  # mayúsculas/minúsculas iguales
        ("", "a", []),                    # cadena vacía
        ("   ", " ", [0, 1, 2]),          # búsqueda de espacios
    ],
)
def test_encontrar_indices(frase, letra, esperado):
    resultado = Modulo_2.ejercicio6.encontrar_indices(frase, letra)
    assert resultado == esperado
