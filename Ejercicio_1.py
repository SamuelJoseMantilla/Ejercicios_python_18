"""
El sistema académico de una universidad necesita un algoritmo para clasificar el **rendimiento académico** de un estudiante según su nota final (en escala de 0.0 a 5.0).

**Reglas:**

- Si la nota es mayor o igual a 0.0 y menor a 3.0, el rendimiento es "Insuficiente".
- Si la nota es mayor o igual a 3.0 y menor o igual a 4.0, el rendimiento es "Aceptable".
- Si la nota es mayor a 4.0 y menor o igual a 5.0, el rendimiento es "Excelente".
"""

def clasificar_rendimiento(nota: float) -> str:
    if 0.0 <= nota < 3.0:
        return "Insuficiente"
    elif 3.0 <= nota <= 4.0:
        return "Aceptable"
    elif 4.0 < nota <= 5.0:
        return "Excelente"
    else:
        return "Nota inválida"

nota = float(input("Ingrese la nota final del estudiante (0.0 - 5.0): "))
print(clasificar_rendimiento(nota))