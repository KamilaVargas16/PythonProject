"""
Implementa el clásico juego para jugar contra la computadora.
•	El usuario elige una opción y la computadora elige una al azar.
•	El programa determina el ganador basándose en las reglas (piedra vence a tijeras, tijeras a papel, papel a piedra).
•	Se debe llevar un conteo de las victorias del jugador y de la computadora. El juego termina cuando uno de los dos llegue a 3 victorias.
Conceptos aplicados: random.choice(), bucle while, if/elif/else, contadores, f-strings.
Ejercicio 5: Clasificador de Números (Par/Impar con Ternario)
Crea un programa que pida un número y, usando un operador ternario, asigne a una variable el texto "Par" o "Impar". Luego, imprime el resultado. Adicionalmente, si el número es múltiplo de 5, debe imprimir un mensaje extra.
Conceptos aplicados: Operador ternario, operador módulo (%), if.

"""
import random

def main():
    """
    Juego: Piedra, Papel o Tijeras contra la computadora.

    Args:
        None

    Returns:
        None
    """
    print("-" * 40)
    print("✊✋✌ Juego: Piedra, Papel o Tijeras")
    print("-" * 40)

    opciones = ["piedra", "papel", "tijeras"]
    victorias_jugador = 0
    victorias_pc = 0

    while victorias_jugador < 3 and victorias_pc < 3:
        jugador = input("\nElige (piedra, papel, tijeras): ").strip().lower()

        if not jugador:
            print("No puede dejar la opción vacía.")
            continue

        if any(c.isdigit() for c in jugador):
            print("No se permiten números, solo texto.")
            continue

        if not jugador.isalpha():
            print(" No se permiten caracteres especiales, solo letras.")
            continue

        if jugador not in opciones:
            print(f" '{jugador}' no es válido. Escriba piedra, papel o tijeras.")
            continue

        # Jugada de la computadora
        pc = random.choice(opciones)
        print(f" La computadora eligió: {pc}")

        # Determinar ganador
        if jugador == pc:
            print("🤝 Empate.")
        elif (jugador == "piedra" and pc == "tijeras") or \
            (jugador == "tijeras" and pc == "papel") or \
            (jugador == "papel" and pc == "piedra"):
            print(" ¡Ganaste esta ronda!")
            victorias_jugador += 1
        else:
            print(" La computadora gana esta ronda.")
            victorias_pc += 1

        print(f" Marcador: Tú {victorias_jugador} - {victorias_pc} PC")

    # Resultado final
    if victorias_jugador == 3:
        print("\n🎉 ¡Felicidades, ganaste el juego!")
    else:
        print("\n💻 La computadora ganó el juego. ¡Suerte la próxima!")


if __name__ == "__main__":
    main()
