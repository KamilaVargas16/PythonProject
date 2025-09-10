def procesar_numeros(numeros: list[int]) -> tuple[list[int], list[int], list[str]]:
    """
    Procesa una lista de números para generar:
    - Números positivos.
    - Cuadrados de todos los números.
    - Signos ("positivo" o "negativo") para cada número.

    Args:
        numeros (list[int]): Lista de números enteros.

    Returns:
        tuple: (positivos, cuadrados, signos)
    """
    positivos = [n for n in numeros if n > 0]
    cuadrados = [n**2 for n in numeros]
    signos = ["positivo" if n >= 0 else "negativo" for n in numeros]

    return positivos, cuadrados, signos


def main():
    numeros = [-5, 10, -15, 20, -25, 30]

    positivos, cuadrados, signos = procesar_numeros(numeros)

    print(f"La lista de numeros positivos es: {positivos}")
    print(f"La lista con los cuadrados de todos los números: {cuadrados}")
    print(f"La lista de positivos y negativos es: {signos}")


if __name__ == "__main__":
    main()
