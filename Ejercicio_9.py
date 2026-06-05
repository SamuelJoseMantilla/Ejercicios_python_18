"""
9. Un banco da a sus ahorradores un interés de 1.5% sobre el monto ahorrado mensual. 
Teniendo como dato de entrada el saldo inicial del ahorrador y el número de meses, determine el saldo final.
"""

def calcular_saldo_final(saldo_inicial: float, meses: int) -> float:
    interes_mensual = 0.015
    saldo_final = saldo_inicial
    for _ in range(meses):
        saldo_final += saldo_final * interes_mensual
    return saldo_final

saldo_inicial = float(input("Ingrese el saldo inicial del ahorrador: "))
meses = int(input("Ingrese el número de meses: "))
saldo_final = calcular_saldo_final(saldo_inicial, meses)
print(f"El saldo final después de {meses} meses es: {saldo_final: }")