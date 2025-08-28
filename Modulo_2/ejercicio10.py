"""
Crea una función que reciba una matriz (lista de listas) y devuelva su transpuesta.
La transpuesta se logra intercambiando filas por columnas.
•	Ejemplo: [[1, 2, 3], [4, 5, 6]] se convierte en [[1, 4], [2, 5], [3, 6]].
•	Resuelve este problema usando bucles for anidados y
    luego intenta resolverlo con una list comprehension anidada.
Conceptos aplicados: c, bucles anidados, list comprehensions anidadas.

"""


def transpuesta(matriz):
    """
    Esta función recibe una matriz y devuelve su transpuesta.
    La transpuesta se logra intercambiando filas por columnas.

    Args:
        matriz (list): lista de listas que representa la matriz
    Returns:
        list: lista de listas que representa la matriz transpuesta
    """
    filas = len(matriz)
    columnas = len(matriz[0])
    resultado = []

    for j in range(columnas):  # recorro columnas
        nueva_fila = []
        for i in range(filas):  # recorro filas
            nueva_fila.append(matriz[i][j])
        resultado.append(nueva_fila)

    return resultado


def main():
    """
    Este programa crea una matriz y muestra su transpuesta.

    Args:
        None
    Returns:
        None
    """
    m = [[1, 2, 3], [4, 5, 6]]
    print("Matriz original:", m)
    print("Transpuesta (con bucles):", transpuesta(m))


if __name__ == "__main__":
    main()

# def transpuesta_comprehension(matriz):
#     return [[matriz[i][j] for i in range(len(matriz))] for j in range(len(matriz[0]))]


# def main():
#     m = [[1, 2, 3], [4, 5, 6]]
#     print("Matriz original:", m)
#     print("Transpuesta (con comprensión de listas):", transpuesta_comprehension(m))


# if __name__ == "__main__":
#     main()




