import pytest
import Modulo_2.ejercicio5


@pytest.mark.parametrize(
    "numero, expected_tipo, expected_mult5",
    [
        (2, "Par", False),     # par y no múltiplo de 5
        (3, "Impar", False),   # impar y no múltiplo de 5
        (10, "Par", True),     # par y múltiplo de 5
        (15, "Impar", True),   # impar y múltiplo de 5
        (0, "Par", True),      # 0 es par y múltiplo de 5
        (-4, "Par", False),    # número negativo par
        (-5, "Impar", True),   # número negativo impar y múltiplo de 5
    ],
)
def test_clasificar_numero(numero, expected_tipo, expected_mult5):
    tipo, es_mult5 = Modulo_2.ejercicio5.clasificar_numero(numero)
    assert tipo == expected_tipo
    assert es_mult5 == expected_mult5
