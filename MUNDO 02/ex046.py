# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificios, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep

for cont in range(10, -1, -1):
    print(cont)
    sleep(0.5)
print("-==-"*5)
print("\033[33mBUM! BUM! BUM! POW!!\033[m\n")
print("\033[33mFELIZ ANO NOVO!!\033[m")
print("-==-"*5)