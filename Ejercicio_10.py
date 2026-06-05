"""

Escribe un programa que reciba el precio de un producto y el tipo de cliente (A, B o C). Aplica un descuento según el tipo:

- A: 30%
- B: 20%
- C: 10% Muestra el precio final después del descuento.

**Ejemplo de entrada:**

```
Ingrese el precio del producto: 100
Ingrese el tipo de cliente (A/B/C): B
```

**Ejemplo de salida:**

```
El precio final con descuento es: 80.0
```
"""

def calcular_precio_final(precio: float, tipo_cliente: str) -> float:
    tipo_cliente = tipo_cliente.upper()
    if tipo_cliente == 'A':
        descuento = 0.30
    elif tipo_cliente == 'B':
        descuento = 0.20
    elif tipo_cliente == 'C':
        descuento = 0.10
    else:
        raise ValueError("Tipo de cliente no válido. Debe ser A, B o C.")
    
    precio_final = precio * (1 - descuento)
    return precio_final
precio = float(input("Ingrese el precio del producto: "))
tipo_cliente = input("Ingrese el tipo de cliente (A/B/C): ")

print(f"El precio final con descuento es: {calcular_precio_final(precio, tipo_cliente): }")
