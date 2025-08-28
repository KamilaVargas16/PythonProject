"""
Ejercicio 3: Validador de Contraseñas
Escribe un programa que pida al usuario crear una contraseña y la valide usando un bucle while. El bucle solo terminará cuando la contraseña cumpla todos los criterios:
•	Mínimo 8 caracteres de longitud.
•	Contiene al menos una letra mayúscula.
•	Contiene al menos un número.
•	En cada intento fallido, el programa debe indicar qué regla no se cumplió.
Conceptos aplicados: Bucle while True, if/elif/else, len(), métodos de string (isupper(), islower(), isdigit()), break.

"""


def main():
    """
    Función principal que ejecuta el validador de contraseñas.

    Args:
        None
    Returns:
        None
    """
    print("-" * 40)
    print(" Validador de Contraseñas")
    print("-" * 40)

    while True:
        contraseña = input("\nCree una contraseña: ").strip()

        if len(contraseña) < 8:
            print(" La contraseña debe tener al menos 8 caracteres.")
            continue

        if not any(c.isupper() for c in contraseña):
            print(" La contraseña debe contener al menos una letra mayúscula.")
            continue

        if not any(c.isdigit() for c in contraseña):
            print(" La contraseña debe contener al menos un número.")
            continue

        print(" Contraseña válida. Registro exitoso.")
        break


if __name__ == "__main__":
    main()
