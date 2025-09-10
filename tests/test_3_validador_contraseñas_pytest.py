import pytest
import Modulo_2.ejercicio3

@pytest.mark.parametrize(
    "contraseña, expected",
    [
        ("hola123", "La contraseña debe tener al menos 8 caracteres."),
        ("contraseña123", "La contraseña debe contener al menos una letra mayúscula."),
        ("Contrasena", "La contraseña debe contener al menos un número."),
        ("Contra123", "Contraseña válida. Registro exitoso."),
        ("CONTRA123", "Contraseña válida. Registro exitoso."),  # todo mayúsculas
        ("contra123", "La contraseña debe contener al menos una letra mayúscula."), # todo minúsculas
    ],
)
def test_validar_contraseña(contraseña, expected):
    assert Modulo_2.ejercicio3.validar_contraseña(contraseña) == expected
