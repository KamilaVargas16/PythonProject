"""
Tienes una lista de productos, donde cada producto es un diccionario: [{"nombre": "Camisa", "precio": 50000},
{"nombre": "Pantalón", "precio": 80000}]:
•	Usa una dictionary comprehension para crear un nuevo diccionario
donde los nombres de los productos sean las claves y los precios con un 19% de IVA incluido sean los valores.
Conceptos aplicados: Dictionary comprehensions, acceso a valores de diccionario.
"""


def main():
    """
    Este programa crea un diccionario de productos con precios que incluyen IVA.
    El programa utiliza una dictionary comprehension para crear un diccionario
    con los nombres de los productos como claves y los precios con IVA como valores.

    Args:
        None
    Returns:
        None
    """
    productos = [
        {"nombre": "Camisa", "precio": 50000},
        {"nombre": "Pantalón", "precio": 80000}
    ]

    # Dictionary comprehension con IVA del 19%
    productos_con_iva = {
        p["nombre"]: round(p["precio"] * 1.19, 2)  # nombre como clave, precio con IVA como valor
        for p in productos
    }

    print(productos_con_iva)


if __name__ == "__main__":
    main()