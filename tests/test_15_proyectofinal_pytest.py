import Modulo_2.ejercicio15 as e15


def test_ganar_batalla_naval():
    barco = [(0, 0), (0, 1), (0, 2)]  # Barco fijo en A1-A3
    disparos = ["A1", "A2", "A3"]
    estado, tablero, intentos = e15.jugar_simulado(barco, disparos)
    assert estado == "ganaste"
    assert tablero[0][0] == "X" and tablero[0][1] == "X" and tablero[0][2] == "X"


def test_perder_batalla_naval():
    barco = [(2, 2), (2, 3), (2, 4)]
    disparos = ["A1", "B1", "C1", "D1", "E1", "A2", "B2", "C3", "D3", "E5"]  # 10 fallos
    estado, tablero, intentos = e15.jugar_simulado(barco, disparos)
    assert estado == "perdiste"
    assert intentos == 0


def test_disparos_invalidos():
    barco = [(1, 1), (1, 2), (1, 3)]
    disparos = ["Z9", "AA", "55", "B2", "B3", "B4"]
    estado, tablero, intentos = e15.jugar_simulado(barco, disparos)
    assert estado == "ganaste"
    assert tablero[1][1] == "X" and tablero[1][2] == "X" and tablero[1][3] == "X"
