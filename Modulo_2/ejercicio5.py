"""
Crea un programa que pida un número y, usando un operador ternario, asigne a una variable el texto
"Par" o "Impar". Luego, imprime el resultado. Adicionalmente, si el número es múltiplo de 5,
debe imprimir un mensaje extra.
Conceptos aplicados: Operador ternario, operador módulo (%), if.

"""


def main():
    """
    Programa que clasifica un número como par o impar
    y muestra un mensaje adicional si es múltiplo de 5.

    Args:
        None

    Returns:
        None
    """
    try:
        numero = int(input("Ingrese un número: "))

        # Usando operador ternario
        tipo = "Par" if numero % 2 == 0 else "Impar"
        print(f"El número {numero} es {tipo}.")

        # Mensaje extra si es múltiplo de 5
        if numero % 5 == 0:
            print("Además, es múltiplo de 5.")
    except ValueError:
        print(" Debe ingresar un número válido.")


if __name__ == "__main__":
    main()
