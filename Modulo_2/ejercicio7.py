import tkinter as tk
from tkinter import simpledialog, messagebox


def combinar_estudiantes_y_notas(estudiantes: list[str], notas: list[list[float]]) -> dict:
    """
    Combina estudiantes y sus listas de notas en un diccionario con promedios.

    Args:
        estudiantes (list[str]): Lista de nombres de estudiantes.
        notas (list[list[float]]): Lista de listas de notas para cada estudiante.

    Returns:
        dict: Diccionario con nombres como claves y promedios como valores.
    """
    if len(estudiantes) != len(notas):
        raise ValueError("La cantidad de estudiantes y de listas de notas no coincide.")

    resultado = {}
    for nombre, lista_notas in zip(estudiantes, notas):
        if not lista_notas:  # evitar división por cero
            raise ValueError(f"El estudiante {nombre} no tiene notas registradas.")
        resultado[nombre] = sum(lista_notas) / len(lista_notas)

    return resultado


def pedir_entero(mensaje: str) -> int:
    # Igual que antes
    while True:
        valor = simpledialog.askstring("Entrada", mensaje)
        if valor and valor.strip().isdigit():
            numero = int(valor.strip())
            if numero > 0:
                return numero
            else:
                messagebox.showwarning("Error", "El número debe ser mayor que 0.")
        else:
            messagebox.showwarning("Error", "Debe ingresar un número entero válido (sin letras ni símbolos).")


def pedir_float(mensaje: str) -> float:
    # Igual que antes
    while True:
        valor = simpledialog.askstring("Entrada", mensaje)
        try:
            numero = float(valor.strip())
            if numero >= 0:
                return numero
            else:
                messagebox.showwarning("Error", "No se permiten números negativos.")
        except (AttributeError, ValueError):
            messagebox.showwarning("Error", "Debe ingresar un número válido (ejemplo: 3 o 3.5).")


def main():
    root = tk.Tk()
    root.withdraw()

    estudiantes = []
    notas_estudiantes = []

    cantidad = pedir_entero("Ingrese la cantidad de estudiantes:")

    for i in range(cantidad):
        while True:
            nombre = simpledialog.askstring("Entrada", f"Ingrese el nombre del estudiante {i + 1}:")
            if nombre and nombre.strip() and nombre.replace(" ", "").isalpha():
                estudiantes.append(nombre)
                break
            else:
                messagebox.showwarning("Error", "El nombre no puede estar vacío y solo debe contener letras.")

        cantidad_notas = pedir_entero(f"Ingrese la cantidad de notas para {nombre}:")
        notas = []
        for j in range(cantidad_notas):
            nota = pedir_float(f"Ingrese la nota {j + 1} de {nombre}:")
            notas.append(nota)
        notas_estudiantes.append(notas)

    promedios = combinar_estudiantes_y_notas(estudiantes, notas_estudiantes)

    mensaje = "Promedios finales de los estudiantes:\n\n"
    for est, prom in promedios.items():
        mensaje += f"{est}: {prom:.2f}\n"

    messagebox.showinfo("Resultados", mensaje)


if __name__ == "__main__":
    main()
