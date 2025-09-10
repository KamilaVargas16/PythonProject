"""
Ejercicio 2: Intérprete de Comandos Sencillo
"""

def procesar_comando(comando: str) -> str:
    """
    Procesa un comando y devuelve la respuesta correspondiente.

    Args:
        comando (str): El comando ingresado por el usuario.

    Returns:
        str: Mensaje asociado al comando.
    """
    comando = comando.strip().lower()
    if not comando:
        return "No puede dejar el campo vacío."

    match comando:
        case "guardar":
            return "Guardando archivo..."
        case "cargar":
            return "Cargando archivo..."
        case "salir":
            return "Saliendo del programa..."
        case _:
            return f"Comando inválido: '{comando}'. Intente nuevamente."


def main():
    """
    Función principal que ejecuta el intérprete de comandos sencillo.
    """
    print("-" * 40)
    print("Bienvenido al sistema  de comandos")
    print("-" * 40)

    while True:
        comando = input("\nIngrese un comando (guardar, cargar, salir): ")
        mensaje = procesar_comando(comando)
        print(mensaje)
        if comando.strip().lower() == "salir":
            break

    print("Programa finalizado.")


if __name__ == "__main__":
    main()
