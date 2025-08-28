"""
Ejercicio 2: Intérprete de Comandos Sencillo
Desarrolla un programa que simule un menú de consola usando la estructura match-case. El programa mostrará una lista de comandos disponibles ("guardar", "cargar", "salir") y el usuario ingresará uno
•	El programa debe ejecutar una acción simulada para cada comando (ej. imprimir "Guardando archivo...").
•	Si el comando no es válido, debe mostrar un mensaje de error.
•	El programa debe seguir pidiendo comandos hasta que el usuario escriba "salir".
•	Conceptos aplicados: Bucle while, match-case, input(), lower().

"""


def main():
    """
    Función principal que ejecuta el intérprete de comandos sencillo.

    Args:
        None
    Returns:
        None
    """
    print("-" * 40)
    print("Bienvenido al sistema  de comandos")
    print("-" * 40)

    while True:
        comando = input("\nIngrese un comando (guardar, cargar, salir): ").strip().lower()
        if not comando:
            print(" No puede dejar el campo vacío.")
            continue

        match comando:
            case "guardar":
                print("Guardando  archivo...")
            case "cargar":
                print(" Cargando archivo...")
            case "salir":
                print("Saliendo del programa...")
                break
            case _:  # Default
                print(f" Comando inválido: '{comando}'. Intente nuevamente.")

    print(" Programa finalizado.")


if __name__ == "__main__":
    main()
