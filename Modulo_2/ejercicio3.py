"""
Ejercicio 3: Validador de Contraseñas
"""

def validar_contraseña(contraseña: str) -> str:
    """
    Valida una contraseña según las reglas del sistema.

    Args:
        contraseña (str): La contraseña a validar.

    Returns:
        str: Mensaje indicando si es válida o qué regla falla.
    """
    if len(contraseña) < 8:
        return "La contraseña debe tener al menos 8 caracteres."

    if not any(c.isupper() for c in contraseña):
        return "La contraseña debe contener al menos una letra mayúscula."

    if not any(c.isdigit() for c in contraseña):
        return "La contraseña debe contener al menos un número."

    return "Contraseña válida. Registro exitoso."


def main():
    """
    Función principal que ejecuta el validador de contraseñas.
    """
    print("-" * 40)
    print("Validador de Contraseñas")
    print("-" * 40)

    while True:
        contraseña = input("\nCree una contraseña: ").strip()
        mensaje = validar_contraseña(contraseña)
        print(mensaje)
        if mensaje == "Contraseña válida. Registro exitoso.":
            break


if __name__ == "__main__":
    main()
