# Blucle While

import math

numero = int(input("Dijite un numero: "))

while numero<0:
    print("Error -> Deberia ser un numero positivo")
    numero = int(input("Dijite un numero: "))

print(f"\nSu raiz cuadrada es: {(math.sqrt(numero)):.2f}")
