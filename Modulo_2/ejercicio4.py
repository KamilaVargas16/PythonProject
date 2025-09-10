import random


def validar_jugada(jugada: str, opciones: list[str]) -> str:
    """
    Valida la jugada del usuario.

    Args:
        jugada (str): entrada del usuario.
        opciones (list): lista de jugadas válidas.

    Returns:
        str: mensaje de error si es inválida, '' si es válida.
    """
    jugada = jugada.strip().lower()

    if not jugada:
        return "No puede dejar la opción vacía."

    if any(c.isdigit() for c in jugada):
        return "No se permiten números, solo texto."

    if not jugada.isalpha():
        return "No se permiten caracteres especiales, solo letras."

    if jugada not in opciones:
        return f"'{jugada}' no es válido. Escriba piedra, papel o tijeras."

    return ""  # válido


def determinar_ganador(jugador: str, pc: str) -> str:
    """
    Determina el ganador de una ronda.

    Args:
        jugador (str): jugada del usuario.
        pc (str): jugada de la computadora.

    Returns:
        str: 'jugador', 'pc' o 'empate'.
    """
    if jugador == pc:
        return "empate"
    elif (jugador == "piedra" and pc == "tijeras") or \
         (jugador == "tijeras" and pc == "papel") or \
         (jugador == "papel" and pc == "piedra"):
        return "jugador"
    else:
        return "pc"


def main():
    print("-" * 40)
    print("✊✋✌ Juego: Piedra, Papel o Tijeras")
    print("-" * 40)

    opciones = ["piedra", "papel", "tijeras"]
    victorias_jugador = 0
    victorias_pc = 0

    while victorias_jugador < 3 and victorias_pc < 3:
        jugada = input("\nElige (piedra, papel, tijeras): ")
        error = validar_jugada(jugada, opciones)
        if error:
            print(error)
            continue

        jugada = jugada.strip().lower()
        pc = random.choice(opciones)
        print(f"La computadora eligió: {pc}")

        resultado = determinar_ganador(jugada, pc)

        if resultado == "empate":
            print("🤝 Empate.")
        elif resultado == "jugador":
            print("¡Ganaste esta ronda!")
            victorias_jugador += 1
        else:
            print("La computadora gana esta ronda.")
            victorias_pc += 1

        print(f"Marcador: Tú {victorias_jugador} - {victorias_pc} PC")

    if victorias_jugador == 3:
        print("\n🎉 ¡Felicidades, ganaste el juego!")
    else:
        print("\n💻 La computadora ganó el juego. ¡Suerte la próxima!")


if __name__ == "__main__":
    main()
