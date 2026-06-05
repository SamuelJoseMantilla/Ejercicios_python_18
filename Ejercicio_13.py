"""
Solicita al usuario un número entero y muestra si es par o impar utilizando.
"""

def es_par_o_impar(numero: int) -> str:
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"
numero = int(input("Ingrese un número entero: "))
resultado = es_par_o_impar(numero)
print(f"El número {numero} es {resultado}.")