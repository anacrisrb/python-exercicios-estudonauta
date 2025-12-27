"Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo."

import math
from math import cos, tan, sin, radians

angulo = float(input("Digite o valor do ângulo: "))
# medida é lida em radianos, necessário fazer a conversão

seno = math.sin(radians(angulo))
print("O angulo de {} tem SENO de {:.2f}".format(angulo,seno))

cosseno = math.cos(radians(angulo))
print("O angulo de {} tem COSSENO de {:.2f}".format(angulo,cosseno))

tangente = math.tan(radians(angulo))
print("O angulo de {} tem TANGENTE de {:.2f}".format(angulo, tangente))
