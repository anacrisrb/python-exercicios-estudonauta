# Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador."

# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint  # Biblioteca para "sortear" um número

from time import sleep  # Biblioteca para simular o procesamento do computador

computador = randint(0, 5)

print("-=--=" * 12)
print("    Vou pensar em número entre 0 e 5. Tente adivinhar...    ")
print("-=--=" * 12)

print()

numero = int(input("Em que número eu pensei? "))

print("\033[1;31;40mPROCESSANDO...\033[m")

sleep(2)  # Tempo de espera para o procesamento

print()

if numero == computador:
    print("\033[1;36;40mPARABÉÉÉÉNS!!\033[m Você VENCEU o desafio!!!")
else:
    print("Você \033[1;36;40mPERDEU\033[m o desafio!!!")

print()

print("-=--=" * 7)
print(
    "  O computador pensou no número {} ".format(computador)
)  # Teste para validar funcionamento
print("-=--=" * 7)
