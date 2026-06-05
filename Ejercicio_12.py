"""
Escribe un programa que solicite una temperatura y la unidad de origen (Celsius o Fahrenheit). Convierte la temperatura a la unidad opuesta y muestra el resultado.

**Fórmulas:**

- De Celsius a Fahrenheit: `(C * 9/5) + 32`
- De Fahrenheit a Celsius: `(F - 32) * 5/9`
"""

def convertir_temperatura(temperatura: float, unidad_origen: str) -> float:
    unidad_origen = unidad_origen.upper()
    if unidad_origen == 'C':
        return (temperatura * 9/5) + 32
    elif unidad_origen == 'F':
        return (temperatura - 32) * 5/9
    else:
        raise ValueError("Unidad de origen no válida. Debe ser 'C' para Celsius o 'F' para Fahrenheit.")
temperatura = float(input("Ingrese la temperatura: "))
unidad_origen = input("Ingrese la unidad de origen (C/F): ")
temperatura_convertida = convertir_temperatura(temperatura, unidad_origen)
if unidad_origen.upper() == 'C':
    print(f"{temperatura}°C es igual a {temperatura_convertida}°F")
else:    print(f"{temperatura}°F es igual a {temperatura_convertida}°C")