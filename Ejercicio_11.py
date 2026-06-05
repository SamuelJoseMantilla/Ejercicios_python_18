"""
Crea un programa que calcule la tarifa de un estacionamiento basado en el número de horas:

- 1 hora o menos: $5
- 2-3 horas: $10
- 4 o más horas: $15
"""

def calcular_tarifa(horas: int) -> float:
    if horas <= 1:
        return 5.0
    elif 2 <= horas <= 3:
        return 10.0
    else:
        return 15.0
horas = int(input("Ingrese el número de horas de estacionamiento: "))
tarifa = calcular_tarifa(horas)
print(f"La tarifa de estacionamiento es: ${tarifa: }")