import pytest
import Modulo_2.ejercicio4


# Tests para validar_jugada
@pytest.mark.parametrize(
    "jugada, expected",
    [
        ("", "No puede dejar la opción vacía."),
        ("123", "No se permiten números, solo texto."),
        ("piedra!", "No se permiten caracteres especiales, solo letras."),
        ("lagarto", "'lagarto' no es válido. Escriba piedra, papel o tijeras."),
        ("piedra", ""),   # válida
        ("papel", ""),    # válida
        ("tijeras", ""),  # válida
        ("   tijeras  ", ""),  # con espacios extra
        ("PIEDRA", ""),
    ],
)
def test_validar_jugada(jugada, expected):
    opciones = ["piedra", "papel", "tijeras"]
    assert Modulo_2.ejercicio4.validar_jugada(jugada, opciones) == expected


# Tests para determinar_ganador
@pytest.mark.parametrize(
    "jugador, pc, expected",
    [
        # empates
        ("piedra", "piedra", "empate"),
        ("papel", "papel", "empate"),
        ("tijeras", "tijeras", "empate"),

        # jugador gana
        ("piedra", "tijeras", "jugador"),
        ("tijeras", "papel", "jugador"),
        ("papel", "piedra", "jugador"),

        # pc gana
        ("tijeras", "piedra", "pc"),
        ("papel", "tijeras", "pc"),
        ("piedra", "papel", "pc"),
    ],
)
def test_determinar_ganador(jugador, pc, expected):
    assert Modulo_2.ejercicio4.determinar_ganador(jugador, pc) == expected
