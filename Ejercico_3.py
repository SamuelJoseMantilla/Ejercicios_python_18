"""
Un centro de salud está realizando una campaña de prevención y necesita un algoritmo que, dado el IMC calculado de un paciente, le indique su **categoría de riesgo**.

**Reglas:**

- Si el IMC es menor a 18.5, la categoría es "Bajo peso".
- Si el IMC es mayor o igual a 18.5 y menor a 25, la categoría es "Peso normal".
- Si el IMC es mayor o igual a 25 y menor a 30, la categoría es "Sobrepeso".
- Si el IMC es mayor o igual a 30, la categoría es "Obesidad".
"""
peso = float(input("Ingrese su peso en kilogramos: "))
estatura = float(input("Ingrese su estatura en metros: "))

imc = peso / (estatura ** 2)

print(f"Su IMC es: {imc:.2f}")

if imc < 18.5:
    print("Clasificación: Bajo peso")
elif 18.5 <= imc <= 24.9:
    print("Clasificación: Peso normal")
elif 25 <= imc <= 29.9:
    print("Clasificación: Sobrepeso")
else:
    print("Clasificación: Obesidad")