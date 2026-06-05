"""
# 7. Calcular el número de pulsaciones que una persona debe tener por cada 10 segundos de ejercicio, si la fórmula es: 

> [!NOTE]
>
> Num. Pulsaciones = (200 –edad) /10. 
"""

def calcular_pulsaciones(edad: int) -> float:
    return (200 - edad) / 10
edad = int(input("Ingrese la edad de la persona: "))
pulsaciones = calcular_pulsaciones(edad)
print(f"El número de pulsaciones por cada 10 segundos de ejercicio es: {pulsaciones:.2f}")
