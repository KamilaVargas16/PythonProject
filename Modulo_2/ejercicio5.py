def clasificar_numero(numero: int) -> tuple[str, bool]:
    """
    Clasifica un número como par o impar y determina si es múltiplo de 5.

    Args:
        numero (int): número a evaluar.

    Returns:
        tuple[str, bool]: ("Par"/"Impar", True si es múltiplo de 5, False en caso contrario)
    """
    tipo = "Par" if numero % 2 == 0 else "Impar"
    es_multiplo5 = (numero % 5 == 0)
    return tipo, es_multiplo5


def main():
    """
    Programa que clasifica un número como par o impar
    y muestra un mensaje adicional si es múltiplo de 5.
    """
    try:
        numero = int(input("Ingrese un número: "))

        tipo, es_multiplo5 = clasificar_numero(numero)
        print(f"El número {numero} es {tipo}.")

        if es_multiplo5:
            print("Además, es múltiplo de 5.")
    except ValueError:
        print("Debe ingresar un número válido.")


if __name__ == "__main__":
    main()
