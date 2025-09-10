import Modulo_2.ejercicio13


def test_aventura_ganar():
    acciones = ["ir al norte", "ir al oeste", "tomar llave", "ir al este", "abrir cofre"]
    mensajes, estado = Modulo_2.ejercicio13.aventura_simulada(acciones)
    assert estado == "ganaste"
    assert any("tesoro brillante" in msg for msg in mensajes)


def test_aventura_perder():
    acciones = ["ir al este"]
    mensajes, estado = Modulo_2.ejercicio13.aventura_simulada(acciones)
    assert estado == "perdiste"
    assert any("GAME OVER" in msg for msg in mensajes)


def test_aventura_accion_invalida():
    acciones = ["saltar", "ir al norte"]
    mensajes, estado = Modulo_2.ejercicio13.aventura_simulada(acciones)
    assert estado == "en juego" or estado == "ganaste"  # depende de si sigue jugando
    assert any("No entiendo esa acción" in msg for msg in mensajes)
