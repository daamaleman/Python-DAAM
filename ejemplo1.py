# Ejemplo 1. Calcular el area de un circulo
"""
    Programa que permite calcular
    el area de un circulo 
    realizado por: Ing. Aleman
"""

import math
print("Calculo del area de un circulo")
radio = float(input("Radio: "))

area = math.pi * (math.pow(radio, 2))

print(f"El area es: {area}")