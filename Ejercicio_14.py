"""
Crea un programa que reciba un número de mes (1-12) y determine a qué estación pertenece:

- Primavera: marzo (3) a mayo (5)
- Verano: junio (6) a agosto (8)
- Otoño: septiembre (9) a noviembre (11)
- Invierno: diciembre (12) a febrero (2)
"""

def determinar_estacion(mes: int) -> str:
    if mes in [3, 4, 5]:
        return "Primavera"
    elif mes in [6, 7, 8]:
        return "Verano"
    elif mes in [9, 10, 11]:
        return "Otoño"
    elif mes in [12, 1, 2]:
        return "Invierno"
    else:
        raise ValueError("Número de mes no válido. Debe ser entre 1 y 12.")
mes = int(input("Ingrese el número del mes (1-12): "))
estacion = determinar_estacion(mes)
print(f"El mes {mes} pertenece a la estación: {estacion}")