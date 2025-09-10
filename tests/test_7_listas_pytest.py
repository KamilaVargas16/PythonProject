import pytest
import Modulo_2.ejercicio7


@pytest.mark.parametrize(
    "estudiantes, notas, esperado",
    [
        (["Ana", "Luis"], [[4.0, 5.0], [3.0, 3.5]], {"Ana": 4.5, "Luis": 3.25}),
        (["Pedro"], [[2.0, 3.0, 4.0]], {"Pedro": 3.0}),
        (["Maria", "Jose"], [[5.0], [4.0, 4.0]], {"Maria": 5.0, "Jose": 4.0}),
    ],
)
def test_combinar_estudiantes_y_notas(estudiantes, notas, esperado):
    resultado = Modulo_2.ejercicio7.combinar_estudiantes_y_notas(estudiantes, notas)
    assert resultado == esperado


def test_error_si_longitudes_no_coinciden():
    with pytest.raises(ValueError, match="no coincide"):
        Modulo_2.ejercicio7.combinar_estudiantes_y_notas(["Ana"], [[5.0], [3.0]])


def test_error_si_estudiante_sin_notas():
    with pytest.raises(ValueError, match="no tiene notas"):
        Modulo_2.ejercicio7.combinar_estudiantes_y_notas(["Ana"], [[]])
