def aplicar_iva(productos: list[dict], tasa: float = 0.19) -> dict:
    """
    Calcula el precio con IVA para una lista de productos.

    Args:
        productos (list[dict]): Lista de diccionarios con 'nombre' y 'precio'.
        tasa (float): Tasa de IVA a aplicar (por defecto 19%).

    Returns:
        dict: Diccionario con el nombre como clave y precio con IVA como valor.
    """
    return {
        p["nombre"]: round(p["precio"] * (1 + tasa), 2)
        for p in productos
    }


def main():
    productos = [
        {"nombre": "Camisa", "precio": 50000},
        {"nombre": "Pantalón", "precio": 80000}
    ]

    productos_con_iva = aplicar_iva(productos)
    print(productos_con_iva)


if __name__ == "__main__":
    main()
