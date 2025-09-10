def obtener_precio(edad: int, estudiante: str) -> int | None:
    """
    Calcula el precio de la entrada de cine según la edad y si es estudiante.

    Retorna:
    - int: precio de la entrada
    - None: si los datos son inválidos
    """
    if edad < 0 or edad > 120:
        return None

    estudiante = estudiante.strip().lower()
    if estudiante not in ["si", "no"]:
        return None

    # Precio base según la edad
    if edad < 12:
        precio = 10000

    elif 12 <= edad <= 17:
        precio = 15000
    else:
        precio = 20000

    # Descuento por estudiante
    if estudiante == "si":
        precio = int(precio * 0.9)

    return precio


def calcular_precio_entrada():
    """Función interactiva que usa input() y print()."""
    try:
        edad = int(input("Ingrese su edad: "))
        estudiante = input("¿Es estudiante? (si/no): ")

        precio = obtener_precio(edad, estudiante)

        if precio is None:
            print("⚠️ Datos inválidos. Intente de nuevo.")
        else:
            print(f"✅ El precio de su entrada es: ${precio:,.0f} COP")

    except ValueError:
        print("⚠️ Error: debe ingresar un número válido para la edad.")

if __name__ == "__main__":
    calcular_precio_entrada()
