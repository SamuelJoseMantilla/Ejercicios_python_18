"""
8. Tres personas deciden invertir su dinero para fundar una empresa. Cada una de ellas invierte una cantidad  distinta.  
Obtener  el  porcentaje  que  cada  quien  invierte  con  respecto  a  la  cantidad  total invertida. 
"""
def calcular_porcentaje_inversion(inversion: float, total: float) -> float:
    return (inversion / total) * 100

inversion1 = float(input("Ingrese la cantidad invertida por la persona 1: "))
inversion2 = float(input("Ingrese la cantidad invertida por la persona 2: "))
inversion3 = float(input("Ingrese la cantidad invertida por la persona 3: "))
total_inversion = inversion1 + inversion2 + inversion3
porcentaje1 = calcular_porcentaje_inversion(inversion1, total_inversion)
porcentaje2 = calcular_porcentaje_inversion(inversion2, total_inversion)
porcentaje3 = calcular_porcentaje_inversion(inversion3, total_inversion)
print(f"El porcentaje de inversión de la persona 1 es: {porcentaje1:}%")
print(f"El porcentaje de inversión de la persona 2 es: {porcentaje2:}%")
print(f"El porcentaje de inversión de la persona 3 es: {porcentaje3:}%")