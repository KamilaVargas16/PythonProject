"""
Ejercicio 13: Aventura de Texto Simple
Diseña un pequeño juego de aventura basado en texto. El jugador comienza en una habitación y puede tomar decisiones ('ir al norte', 'abrir cofre'):
•	El juego debe tener al menos 3 habitaciones y un estado final (ganar o perder).
•	Utiliza un bucle while para el bucle principal del juego y estructuras if/elif/else para manejar las decisiones del jugador y el estado del juego.
Conceptos integrados: Bucles, condicionales, manejo de estado con variables, input().
"""


def aventura():
    """
    Este es un juego de aventura basado en texto donde el jugador navega por habitaciones y toma decisiones.
    El juego comienza en una habitación y puede tomar decisiones ('ir al norte', 'abrir cofre'):

    Args:
        None
    Returns:
        None
    """
    print("Bienvenido a la Aventura del Castillo Misterioso ")
    print("Estás en una habitación oscura con dos puertas: una al norte y otra al este.\n")

    habitacion = "inicio"
    tiene_llave = False
    juego_activo = True

    while juego_activo:
        accion = input("¿Qué quieres hacer? ").lower()

        # HABITACIÓN INICIAL
        if habitacion == "inicio":
            if accion == "ir al norte":
                habitacion = "tesoro"
                print("\nEntras en una habitación con un gran cofre en el centro.")
            elif accion == "ir al este":
                habitacion = "trampa"
                print("\n¡Oh no! Has caído en una trampa llena de pinchos.  GAME OVER.")
                juego_activo = False
            else:
                print("No entiendo esa acción. Intenta: 'ir al norte' o 'ir al este'.")

        # HABITACIÓN DEL TESORO
        elif habitacion == "tesoro":
            if accion == "abrir cofre":
                if not tiene_llave:
                    print("El cofre está cerrado con llave. Necesitas encontrarla.")
                else:
                    print("¡Abres el cofre y encuentras un tesoro brillante!  GANASTE ")
                    juego_activo = False
            elif accion == "ir al sur":
                habitacion = "inicio"
                print("\nRegresas a la primera habitación.")
            elif accion == "ir al oeste":
                habitacion = "llave"
                print("\nEncuentras una pequeña habitación con una llave en el suelo.")
            else:
                print("Acción no válida. Intenta: 'abrir cofre', 'ir al sur' o 'ir al oeste'.")

        # HABITACIÓN DE LA LLAVE
        elif habitacion == "llave":
            if accion == "tomar llave":
                if not tiene_llave:
                    tiene_llave = True
                    print("Has recogido la llave. ")
                else:
                    print("Ya tienes la llave.")
            elif accion == "ir al este":
                habitacion = "tesoro"
                print("\nRegresas a la habitación del cofre.")
            else:
                print("Acción no válida. Intenta: 'tomar llave' o 'ir al este'.")

    print("\nGracias por jugar. ")


def main():
    aventura()


if __name__ == "__main__":
    main()
