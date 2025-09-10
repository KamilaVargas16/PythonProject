import random


PALABRAS = ["agua", "celular", "programacion", "pastel", "banano"]

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
    return random.choice(PALABRAS)


def mostrar_tablero(palabra_secreta, letras_correctas, letras_incorrectas, vidas):
    """Muestra el tablero con el muñeco, palabra y letras intentadas"""
    tablero = ""
    for letra in palabra_secreta:
        tablero += letra + " " if letra in letras_correctas else "_ "
    return tablero.strip()


def validar_entrada(letra, letras_correctas, letras_incorrectas):
    """Valida que la letra sea válida y no repetida"""
    if len(letra) != 1 or not letra.isalpha():
        return False
    if letra in letras_correctas or letra in letras_incorrectas:
        return False
    return True


def jugar():
    """Versión interactiva (con input)"""
    palabra_secreta = elegir_palabra()
    letras_correctas = set()
    letras_incorrectas = set()
    vidas = 6

    print(" Bienvenido al Juego del Ahorcado ")

    while vidas > 0:
        print(AHORCADO[vidas])
        print("\nPalabra:", mostrar_tablero(palabra_secreta, letras_correctas, letras_incorrectas, vidas))
        print("Letras incorrectas:", " ".join(letras_incorrectas) if letras_incorrectas else "Ninguna")
        print(f"Vidas restantes: {vidas}\n")

        letra = input("Ingresa una letra: ").lower()

        if not validar_entrada(letra, letras_correctas, letras_incorrectas):
            print("⚠️ Entrada inválida, intenta de nuevo.")
            continue

        if letra in palabra_secreta:
            letras_correctas.add(letra)
            print(f"✅ ¡Bien! La letra '{letra}' está en la palabra.")
        else:
            letras_incorrectas.add(letra)
            vidas -= 1
            print(f"❌ La letra '{letra}' no está en la palabra.")

        if all(l in letras_correctas for l in palabra_secreta):
            print("🎉 ¡Felicidades! Adivinaste la palabra.")
            return

    print(f"\n💀 Te quedaste sin vidas. La palabra era: {palabra_secreta}")


# para pruebas unitarias
def jugar_simulado(palabra_secreta, intentos):
    """
    Simula una partida del ahorcado para pruebas.

    Args:
        palabra_secreta (str): palabra secreta fija
        intentos (list[str]): lista de letras a intentar

    Returns:
        tuple: (estado_final, tablero_final, vidas_restantes)
            estado_final -> "ganaste" o "perdiste"
            tablero_final -> str con la palabra revelada o con guiones
            vidas_restantes -> int
    """
    letras_correctas = set()
    letras_incorrectas = set()
    vidas = 6

    for letra in intentos:
        letra = letra.lower()
        if not validar_entrada(letra, letras_correctas, letras_incorrectas):
            continue

        if letra in palabra_secreta:
            letras_correctas.add(letra)
        else:
            letras_incorrectas.add(letra)
            vidas -= 1

        if all(l in letras_correctas for l in palabra_secreta):
            return "ganaste", mostrar_tablero(palabra_secreta, letras_correctas, letras_incorrectas, vidas), vidas

        if vidas == 0:
            return "perdiste", mostrar_tablero(palabra_secreta, letras_correctas, letras_incorrectas, vidas), vidas

    return "en juego", mostrar_tablero(palabra_secreta, letras_correctas, letras_incorrectas, vidas), vidas


def main():
    jugar()


if __name__ == "__main__":
    main()
