def validar_cedula(cedula: str) -> bool:
    """
    Esta función valida un número de cédula basado en la regla de que la suma de sus dígitos debe ser un número par.

    Args:
        cedula (str): número de cédula
    Returns:
        bool: True si es válido, False si no
    """
    # Validar que la cédula sea solo números
    if not cedula.isdigit():
        return False

    # Validar longitud (ejemplo: entre 6 y 10 dígitos)
    if len(cedula) < 6 or len(cedula) > 10:
        return False

    # Validar que la suma de los dígitos sea par
    suma = sum(int(d) for d in cedula)
    return suma % 2 == 0


# ⚡️ Nueva función para usar en las pruebas unitarias
def validar_cedula_test(cedula: str) -> bool:
    return validar_cedula(cedula)


def main():
    """
    Este programa pide al usuario su número de cédula hasta que ingrese una válida.

    Args:
        None
    Returns:
        None
    """
    while True:
        cedula = input("Ingrese su número de cédula: ")
        if validar_cedula(cedula):
            print("✅ Cédula válida. Bienvenido.")
            break
        else:
            print("⚠️ Intente de nuevo.\n")


if __name__ == "__main__":
    main()
