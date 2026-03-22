# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar.
# Mostrando no final quantos palpites foram necessários para vencer o computador.

from random import randint  #Biblioteca para sortear um número

from time import sleep # Biblioteca para contagem de tempo

computador = randint(0, 10)

print("-=--=" * 12)
print("    Vou pensar em número entre 0 e 10. Tente adivinhar...    ")
print("-=--=" * 12)

sleep(0.5)

print()

numero = int(input("Em que número eu pensei? "))

cont = 0

while numero != computador:
    print("\033[1;31;40mPROCESSANDO...\033[m")

    sleep(1)  # Tempo de espera para o procesamento
    numero = int(input(f"Tente um novo palpite: "))
    cont += 1

print()

print(f"\033[2;33;40mParabéns!\033[m você acertou com {cont} palpites.")
