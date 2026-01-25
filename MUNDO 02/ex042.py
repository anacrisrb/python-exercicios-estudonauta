# Refaça o desafio 035 dos triângulos acrescentando o recurso para mostrar que tipo de triângulo será formado:

# Equilátero: todos os lados são iguais
# Isóceles: dois lados iguais
# Escaleno: todos os lados diferentes

"""Desafio 035:
Desevolva um programa que leia o comprimento de três retas e diga ao usuário se eles podem ou não formar um triângulo.
"""

seg1 = float(input("Primeiro segmento: "))
seg2 = float(input("Segundo segmento: "))
seg3 = float(input("Terceiro segmento: "))

if (seg1 + seg2) > seg3 and (seg2 + seg3) > seg1 and (seg3 + seg1) > seg2:
    print("Os segmentos PODEM formar um triângulo", end="")

    if seg1 == seg2 == seg3:
        print(" EQUILÁTERO: todos os lados são iguais")
    elif seg1 == seg2 or seg1 == seg3 or seg2 == seg3:
        print(" ISÓCELES: dois lados iguais")
    else:
        print(" ESCALENO: TODOS OS LADOS DIFERENTES")

else:
    print("Os segmentos NÃO PODEM formar um triângulo.")
