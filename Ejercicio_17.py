"""
Crea un programa que determine si un año es:

- Bisiesto (divisible entre 4 pero no entre 100, excepto si también es divisible entre 400).
- Común.
"""

def es_bisiesto(año: int) -> bool:
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else:
        return False
año = int(input("Ingrese un año: "))
if es_bisiesto(año):
    print(f"El año {año} es bisiesto.")
else:    print(f"El año {año} es común.")