"""
Una tienda de moda ofrece descuentos escalonados según la cantidad de prendas compradas para liquidar inventario. El objetivo es indicar el **porcentaje de descuento** aplicable.

**Reglas:**

- Si compra menos de 3 prendas, no hay descuento (0%).
- Si compra 3 o más prendas, pero menos de 6, aplica un 10% de descuento.
- Si compra 6 o más prendas, pero menos de 12, aplica un 20% de descuento.
- Si compra 12 prendas o más, aplica un 30% de descuento
"""

def calcular_descuento(cantidad: int) -> float:
    if cantidad < 3:
        return 0.0
    elif 3 <= cantidad < 6:
        return 10.0
    elif 6 <= cantidad < 12:
        return 20.0
    else:
        return 30.0

cantidad = int(input("Ingrese la cantidad de prendas compradas: "))
descuento = calcular_descuento(cantidad)
print(f"El porcentaje de descuento aplicable es: {descuento}%")
