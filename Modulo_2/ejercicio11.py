"""
Bloque 3: Algoritmos y Proyectos de Lógica Aplicada (Ejercicios 11-15)
Estos ejercicios integran todos los conceptos del módulo en la solución de problemas algorítmicos más complejos.
Ejercicio 11: Validador de Cédula (Algoritmo Simple)
Escribe una función que valide un número de cédula (como string) basado en una regla simple: la suma de sus dígitos debe ser un número par. La función debe devolver True si es válido y False si no:
•	Adicionalmente, el programa principal debe pedir al usuario su cédula hasta que ingrese una válida, usando un bucle.
Conceptos aplicados: Funciones, bucle while, conversión de tipos (str a int), bucle for sobre un string.

"""


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
        print("❌ Error: la cédula debe contener solo números.")
        return False

    # Validar longitud (ejemplo: entre 6 y 10 dígitos)
    if len(cedula) < 6 or len(cedula) > 10:
        print("❌ Error: la cédula debe tener entre 6 y 10 dígitos.")
        return False


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
