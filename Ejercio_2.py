"""
El departamento de Recursos Humanos de una empresa de tecnología desea calcular el **porcentaje de bono** anual que le corresponde a sus empleados basándose en su antigüedad (años trabajados). Solo aplica para empleados con 1 o más años de servicio.

**Reglas:**

- Para antigüedad igual a 1 año y menor a 3 años, el bono es del 5% de su sueldo.
- Para antigüedad mayor o igual a 3 años y menor a 10 años, el bono es del 10% de su sueldo.
- Para antigüedad de 10 años o más, el bono es del 20% de su sueldo.
"""
def calcular_bono(antiguedad: int, sueldo: float) -> float:
    if antiguedad >= 1 and antiguedad < 3:
        return sueldo * 0.05
    elif antiguedad >= 3 and antiguedad < 10:
        return sueldo * 0.10
    elif antiguedad >= 10:
        return sueldo * 0.20
    else:
        return 0.0

antiguedad = int(input("Ingrese la antigüedad del empleado (en años): "))
sueldo = float(input("Ingrese el sueldo del empleado: "))
bono = calcular_bono(antiguedad, sueldo)
print(f"El bono anual para el empleado es: ${bono:.2f}")