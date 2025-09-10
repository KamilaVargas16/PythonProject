"""
Ejercicio 10: Transpuesta de una Matriz
Crea una función que reciba una matriz (lista de listas) y devuelva su transpuesta.
La transpuesta se logra intercambiando filas por columnas.
Ejemplo: [[1, 2, 3], [4, 5, 6]] se convierte en [[1, 4], [2, 5], [3, 6]].
"""

def transpuesta(matriz):
    """
    Calcula la transpuesta de una matriz usando bucles for anidados.

    Args:
        matriz (list): lista de listas que representa la matriz

    Returns:
        list: matriz transpuesta
    """
    filas = len(matriz)
    columnas = len(matriz[0])
    resultado = []

    for j in range(columnas):  # recorre columnas
        nueva_fila = []
        for i in range(filas):  # recorre filas
            nueva_fila.append(matriz[i][j])
        resultado.append(nueva_fila)

    return resultado


def transpuesta_comprehension(matriz):
    """
    Calcula la transpuesta de una matriz usando list comprehensions anidadas.

    Args:
        matriz (list): lista de listas que representa la matriz

    Returns:
        list: matriz transpuesta
    """
    return [[matriz[i][j] for i in range(len(matriz))] for j in range(len(matriz[0]))]


def main():
    """
    Ejemplo de uso de las dos funciones de transposición.
    """
    m = [[1, 2, 3], [4, 5, 6]]
    print("Matriz original:", m)
    print("Transpuesta (con bucles):", transpuesta(m))
    print("Transpuesta (con comprensión de listas):", transpuesta_comprehension(m))


if __name__ == "__main__":
    main()
