"""
Un videojuego de rol (RPG) necesita determinar el **Rango del Jugador** basándose en sus Puntos de Experiencia (XP) acumulados.

**Reglas:**

- Si los XP son menores a 1.000, el rango es "Novato".
- Si los XP son mayores o iguales a 1.000 y menores a 5.000, el rango es "Veterano".
- Si los XP son mayores o iguales a 5.000 y menores a 10.000, el rango es "Maestro".
- Si los XP son 10.000 o más, el rango es "Leyenda".
"""
def determinar_rango(xp: int) -> str:
    if xp < 1000:
        return "Novato"
    elif 1000 <= xp < 5000:
        return "Veterano"
    elif 5000 <= xp < 10000:
        return "Maestro"
    else:
        return "Leyenda"
xp = int(input("Ingrese los Puntos de Experiencia (XP) del jugador: "))
print(f"El rango del jugador es: {determinar_rango(xp)}")