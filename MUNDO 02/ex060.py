# Faça um programa que leia um número qualquer e mostre o seu fatorial.
from unicodedata import numeric

# Ex: 5! = 5x4x3x2x1 = 120

n = int(input(f"Informe um numero: "))

fatorial = 1
contador = n

while contador > 0:
    fatorial *= contador
    contador -= 1

print(f"{n}! = {fatorial}")
