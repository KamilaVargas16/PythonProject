"""
Ejercicio 6: Analizador de Posiciones de Letras con enumerate
Crea una función que reciba una frase y una letra. La función debe devolver una lista con todos los índices
(posiciones) en los que aparece esa letra en la frase.
•	Ejemplo: encontrar_indices("Hola SENA", "a") debería devolver [3, 8].
Conceptos aplicados: Funciones, enumerate(), bucle for, list.append().

"""


def encontrar_indices(frase: str, letra: str) -> list:
    """
    Busca todas las posiciones en las que aparece una letra en una frase.

    Args:
        frase (str): La frase donde se realizará la búsqueda.
        letra (str): La letra a buscar dentro de la frase.

    Returns:
        list: Lista de índices donde aparece la letra en la frase.
    """
    indices = []
    for i, caracter in enumerate(frase):
        if caracter.lower() == letra.lower():
            indices.append(i)
    return indices


def validacion_frase(mensaje: str) -> str:
    """
    Solicita una frase y valida que solo contenga letras y espacios.

    Args:
        mensaje (str): Texto que se muestra al usuario.

    Returns:
        str: La frase válida ingresada por el usuario.
    """
    while True:
        entrada = input(mensaje).strip()

        if not entrada:
            print("🔔 No puede dejar la respuesta vacía.")
        elif not all(c.isalpha() or c.isspace() for c in entrada):
            print("🔔 Solo se permiten letras y espacios.")
        else:
            return entrada


def validacion_letra(mensaje: str) -> str:
    """
    Solicita una letra y valida que sea un solo carácter alfabético.

    Args:
        mensaje (str): Texto que se muestra al usuario.

    Returns:
        str: La letra válida ingresada por el usuario.
    """
    while True:
        entrada = input(mensaje).strip()

        if len(entrada) != 1 or not entrada.isalpha():
            print("🔔 Debe ingresar solo una letra válida.")
        else:
            return entrada


def main():
    frase = validacion_frase("Ingrese una frase: ")
    letra = validacion_letra("Ingrese la letra a buscar: ")

    resultado = encontrar_indices(frase, letra)

    if resultado:
        print(f"La letra '{letra}' aparece en las posiciones: {resultado}")
    else:
        print(f"La letra '{letra}' no aparece en la frase.")


if __name__ == "__main__":
    main()


