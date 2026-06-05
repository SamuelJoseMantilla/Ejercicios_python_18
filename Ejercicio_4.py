"""
Un parqueadero automatizado cobra tarifas diferenciadas según el tiempo de permanencia. El objetivo es calcular el **total a pagar** según la cantidad de horas que el vehículo estuvo estacionado.

**Reglas:**

- Para estancias de hasta 2 horas (menor o igual), la tarifa es fija de $3.000.
- Para estancias mayores a 2 horas y menores o iguales a 5 horas, la tarifa es de $2.000 por hora adicional.
- Para estancias superiores a 5 horas, se cobra una tarifa plena de $15.000 por todo el día.

"""
def calcular_tarifa(horas: float) -> float:
    if horas <= 2:
        return 3000.0
    elif 2 < horas <= 5:
        return 3000.0 + (horas - 2) * 2000.0
    else:
        return 15000.0

horas = float(input("Ingrese la cantidad de horas que el vehículo estuvo estacionado: "))
print(f"El total a pagar es: ${calcular_tarifa(horas):.2f}")