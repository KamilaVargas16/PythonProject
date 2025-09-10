import Modulo_2.ejercicio14 as e14


def test_ganar_ahorcado():
    palabra = "agua"
    intentos = ["a", "g", "u"]
    estado, tablero, vidas = e14.jugar_simulado(palabra, intentos)
    assert estado == "ganaste"
    assert "a g u a" in tablero or "a g u a".replace(" ", "") in tablero


def test_perder_ahorcado():
    palabra = "celular"
    intentos = ["x", "y", "z", "q", "w", "t"]  # todas incorrectas
    estado, tablero, vidas = e14.jugar_simulado(palabra, intentos)
    assert estado == "perdiste"
    assert vidas == 0


def test_en_juego_ahorcado():
    palabra = "banano"
    intentos = ["b", "n"]  # aún faltan letras
    estado, tablero, vidas = e14.jugar_simulado(palabra, intentos)
    assert estado == "en juego"
    assert "_" in tablero
