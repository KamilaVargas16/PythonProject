def aventura_simulada(acciones):
    """
    Versión de la aventura para pruebas unitarias.
    Recibe una lista de acciones simuladas en lugar de usar input().

    Args:
        acciones (list[str]): lista de acciones del jugador

    Returns:
        tuple: (mensajes, estado_final)
            mensajes (list[str]) → todos los mensajes mostrados en el juego
            estado_final (str) → "ganaste", "perdiste" o "en juego"
    """
    mensajes = []
    habitacion = "inicio"
    tiene_llave = False
    juego_activo = True
    estado_final = "en juego"

    mensajes.append("Bienvenido a la Aventura del Castillo Misterioso ")
    mensajes.append("Estás en una habitación oscura con dos puertas: una al norte y otra al este.\n")

    for accion in acciones:
        accion = accion.lower()

        if habitacion == "inicio":
            if accion == "ir al norte":
                habitacion = "tesoro"
                mensajes.append("\nEntras en una habitación con un gran cofre en el centro.")
            elif accion == "ir al este":
                habitacion = "trampa"
                mensajes.append("\n¡Oh no! Has caído en una trampa llena de pinchos.  GAME OVER.")
                juego_activo = False
                estado_final = "perdiste"
                break
            else:
                mensajes.append("No entiendo esa acción. Intenta: 'ir al norte' o 'ir al este'.")

        elif habitacion == "tesoro":
            if accion == "abrir cofre":
                if not tiene_llave:
                    mensajes.append("El cofre está cerrado con llave. Necesitas encontrarla.")
                else:
                    mensajes.append("¡Abres el cofre y encuentras un tesoro brillante!  GANASTE ")
                    juego_activo = False
                    estado_final = "ganaste"
                    break
            elif accion == "ir al sur":
                habitacion = "inicio"
                mensajes.append("\nRegresas a la primera habitación.")
            elif accion == "ir al oeste":
                habitacion = "llave"
                mensajes.append("\nEncuentras una pequeña habitación con una llave en el suelo.")
            else:
                mensajes.append("Acción no válida. Intenta: 'abrir cofre', 'ir al sur' o 'ir al oeste'.")

        elif habitacion == "llave":
            if accion == "tomar llave":
                if not tiene_llave:
                    tiene_llave = True
                    mensajes.append("Has recogido la llave. ")
                else:
                    mensajes.append("Ya tienes la llave.")
            elif accion == "ir al este":
                habitacion = "tesoro"
                mensajes.append("\nRegresas a la habitación del cofre.")
            else:
                mensajes.append("Acción no válida. Intenta: 'tomar llave' o 'ir al este'.")

    mensajes.append("\nGracias por jugar. ")
    return mensajes, estado_final


def main():
    # Mantengo el main original con input() para jugar manualmente
    print("Bienvenido a la Aventura del Castillo Misterioso ")
    print("Estás en una habitación oscura con dos puertas: una al norte y otra al este.\n")

    habitacion = "inicio"
    tiene_llave = False
    juego_activo = True

    while juego_activo:
        accion = input("¿Qué quieres hacer? ").lower()

        # ... (misma lógica que arriba, sin return) ...


if __name__ == "__main__":
    main()
