"""
Ejercicio 1: Sistema de Precios de Entradas de Cine

Este programa calcula el precio de una entrada de cine basándose en:
- La edad del cliente.
- Si es estudiante o no.

Reglas:
• Niños (< 12 años): $10.000.
• Jóvenes (12 - 17 años): $15.000.
• Adultos (18 años en adelante): $20.000.
• Si es estudiante (sin importar la edad), obtiene un 10% de descuento.

Conceptos aplicados:
- if/elif/else anidados
- Operadores lógicos
- Manejo de input(), int(), lower()
- f-strings
- Validaciones de entrada
"""

def calcular_precio_entrada():
    try:
        # Solicitar edad y validar
        edad = int(input("Ingrese su edad: "))
        if edad < 0 or edad > 120:
            print("⚠️ Error: Edad no válida. Intente de nuevo.")
            return

        # Preguntar si es estudiante
        estudiante = input("¿Es estudiante? (si/no): ").strip().lower()
        if estudiante not in ["si", "no"]:
            print("⚠️ Error: Respuesta no válida. Debe escribir 'si' o 'no'.")
            return

        # Determinar precio según la edad
        if edad < 12:
            precio = 10000
        elif 12 <= edad <= 17:
            precio = 15000
        else:  # 18 o más
            precio = 20000

        # Aplicar descuento si es estudiante
        if estudiante == "si":
            precio = precio * 0.9  # 10% de descuento

        print(f"✅ El precio de su entrada es: ${precio:,.0f} COP")

    except ValueError:
        print("⚠️ Error: Debe ingresar un número válido para la edad.")


# Ejecución del programa
if __name__ == "__main__":
    calcular_precio_entrada()
