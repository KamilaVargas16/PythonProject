"""
Ejercicio 14: Juego del Ahorcado (Hangman)
Diseña una versión para consola del clásico juego del "Ahorcado". El programa debe ser capaz de gestionar toda la lógica del juego, desde la selección de la palabra hasta determinar si el jugador ha ganado o perdido.
Lógica del Juego:
•	El programa debe tener una lista predefinida de palabras secretas y seleccionar una al azar para cada partida.
•	Debe mostrar al jugador el "tablero", que consiste en guiones bajos representando las letras de la palabra secreta y una lista de las letras ya intentadas.
•	El jugador tiene un número limitado de intentos (ej. 6 vidas).
•	En cada turno, el jugador ingresa una letra. El programa debe validar si la entrada es una sola letra y si no ha sido intentada antes.
•	Si la letra está en la palabra secreta, se revelan todas sus apariciones (ej. _ _ _ _ _ -> _ a _ a _). Si no está, el jugador pierde una vida.
•	El juego termina cuando el jugador adivina todas las letras (gana) o se queda sin vidas (pierde).
Conceptos integrados: Lógica de juegos, random.choice, listas y/o sets (para letras adivinadas), manipulación de strings, bucles while, condicionales if/else, funciones para modularizar (ej. mostrar_tablero(), validar_entrada()), manejo de estado del juego.

"""

import random

# Lista de palabras secretas
PALABRAS = ["python", "ahorcado", "programacion", "algoritmo", "juego"]

# Dibujos del ahorcado según las vidas
AHORCADO = [
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =======""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =======""",
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =======""",
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =======""",
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =======""",
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =======""",
    """
     +---+
     |   |
         |
         |
         |
         |
    ======="""
]


def elegir_palabra():
    """
    """
    return random.choice(PALABRAS)


def mostrar_tablero(palabra_secreta, letras_correctas, letras_incorrectas, vidas):
    """
    Esta función muestra el tablero con el muñeco, palabra y letras intentadas.

    Args:
        palabra_secreta (str): palabra secreta
        letras_correctas (set): conjunto de letras correctas
        letras_incorrectas (set): conjunto de letras incorrectas
        vidas (int): número de vidas restantes
    Returns:
        None
    """

    """Muestra el tablero con el muñeco, palabra y letras intentadas"""
    print(AHORCADO[vidas])  # Dibujo según vidas
    tablero = ""
    for letra in palabra_secreta:
        tablero += letra + " " if letra in letras_correctas else "_ "
    print("\nPalabra:", tablero)
    print("Letras incorrectas:", " ".join(letras_incorrectas) if letras_incorrectas else "Ninguna")
    print(f"Vidas restantes: {vidas}\n")


def validar_entrada(letra, letras_correctas, letras_incorrectas):
    """
    Esta función valida la entrada del usuario.

    Args:
        letra (str): letra ingresada por el usuario
        letras_correctas (set): conjunto de letras correctas
        letras_incorrectas (set): conjunto de letras incorrectas
    Returns:
        bool: True si la entrada es válida, False si no
    """
    if len(letra) != 1 or not letra.isalpha():
        print(" Ingresa solo una letra válida.")
        return False
    if letra in letras_correctas or letra in letras_incorrectas:
        print(" Ya intentaste esa letra.")
        return False
    return True


def jugar():
    """
    Juega el juego del ahorcado.

    Args:
        None
    Returns:
        None
    """
    palabra_secreta = elegir_palabra()
    letras_correctas = set()
    letras_incorrectas = set()
    vidas = 6  # índice en AHORCADO

    print(" Bienvenido al Juego del Ahorcado ")

    while vidas > 0:
        mostrar_tablero(palabra_secreta, letras_correctas, letras_incorrectas, vidas)

        letra = input("Ingresa una letra: ").lower()

        if not validar_entrada(letra, letras_correctas, letras_incorrectas):
            continue

        if letra in palabra_secreta:
            letras_correctas.add(letra)
            print(f"✅ ¡Bien! La letra '{letra}' está en la palabra.")
        else:
            letras_incorrectas.add(letra)
            vidas -= 1
            print(f" La letra '{letra}' no está en la palabra.")

        if all(l in letras_correctas for l in palabra_secreta):
            mostrar_tablero(palabra_secreta, letras_correctas, letras_incorrectas, vidas)
            print("🎉 ¡Felicidades! Adivinaste la palabra.")
            return

    # Perdió
    mostrar_tablero(palabra_secreta, letras_correctas, letras_incorrectas, vidas)
    print(f"\n💀 Te quedaste sin vidas. La palabra era: {palabra_secreta}")


def main():
    jugar()


if __name__ == "__main__":
    main()
