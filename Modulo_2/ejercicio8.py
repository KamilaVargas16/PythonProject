"""
Ejercicio 8: Filtrado de Datos con List Comprehensions
Dada una lista de números [-5, 10, -15, 20, -25, 30], utiliza una list comprehension para crear tres nuevas listas:
•	Una lista con solo los números positivos.
•	Una lista con los cuadrados de todos los números.
•	Una lista de strings que diga "positivo" o "negativo" para cada número, usando un ternario dentro de la comprensión.
•	Conceptos aplicados: List comprehensions, operador ternario.

"""

def main():
    numeros = [-5, 10, -15, 20, -25, 30]

    #Lista de numeros positivos
    positivo = [n for n in numeros if n > 0]

    #Lista con los cuadrados de todos los números.
    cuadrados = [n**2 for n in numeros]

    #Lista de strings que diga "positivo" o "negativo" para cada número, usando un ternario dentro de la comprensión.
    signos = ["positivo" if n >= 0 else "negativo" for n in numeros]

    print(f"La lista de numeros positivos es: {positivo}")
    print(f"La lista con los cuadrados de todos los números: {cuadrados}")
    print(f"La lista de positivos y negativos es: {signos}")

if __name__ == "__main__":
    main()
