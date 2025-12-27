"Crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira."
import math
# trunc = truncate (parte inteira do número)

from math import trunc

num = float(input("Digite um numero real: "))

print(f"O numero {num} tem a porção inteira {trunc(num)}.")
