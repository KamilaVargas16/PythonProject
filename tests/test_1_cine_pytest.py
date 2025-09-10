import pytest
from Modulo_2.ejercicio1 import obtener_precio


@pytest.mark.parametrize(
    "edad, estudiante, esperado",
    [
        (10, "no", 10000),     # Niño sin descuento
        (10, "si", 9000),      # Niño con descuento
        (15, "no", 15000),     # Joven sin descuento
        (15, "si", 13500),     # Joven con descuento
        (25, "no", 20000),     # Adulto sin descuento
        (25, "si", 18000),     # Adulto con descuento
        (-5, "no", None),      # Edad negativa inválida
        (150, "si", None),     # Edad demasiado alta inválida
        (20, "quizas", None),  # Respuesta estudiante inválida
    ]
)
def test_obtener_precio_entrada(edad, estudiante, esperado):
    assert obtener_precio(edad, estudiante) == esperado
