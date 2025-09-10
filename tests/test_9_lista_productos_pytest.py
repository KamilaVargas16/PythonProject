import pytest
import Modulo_2.ejercicio9


def test_aplicar_iva_basico():
    productos = [
        {"nombre": "Camisa", "precio": 50000},
        {"nombre": "Pantalón", "precio": 80000}
    ]
    resultado = Modulo_2.ejercicio9.aplicar_iva(productos)
    esperado = {
        "Camisa": 59500.0,
        "Pantalón": 95200.0
    }
    assert resultado == esperado


@pytest.mark.parametrize(
    "productos, tasa, esperado",
    [
        (
            [{"nombre": "Zapatos", "precio": 100000}], 0.19,
            {"Zapatos": 119000.0}
        ),
        (
            [{"nombre": "Gorra", "precio": 20000}], 0.10,
            {"Gorra": 22000.0}
        ),
        (
            [], 0.19,
            {}
        ),
    ]
)
def test_parametrizado_aplicar_iva(productos, tasa, esperado):
    assert Modulo_2.ejercicio9.aplicar_iva(productos, tasa) == esperado
