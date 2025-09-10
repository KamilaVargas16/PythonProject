import pytest
import Modulo_2.ejercicio2

@pytest.mark.parametrize(
    "comando, expected",
    [
        ("guardar", "Guardando archivo..."),
        ("cargar", "Cargando archivo..."),
        ("salir", "Saliendo del programa..."),
        ("", "No puede dejar el campo vacío."),
        ("xxx", "Comando inválido: 'xxx'. Intente nuevamente."),
        ("   ", "No puede dejar el campo vacío."),   # prueba con solo espacios
        ("GUARDAR", "Guardando archivo..."),         # prueba case-insensitive
    ],
)
def test_procesar_comando(comando, expected):
    assert Modulo_2.ejercicio2.procesar_comando(comando) == expected
