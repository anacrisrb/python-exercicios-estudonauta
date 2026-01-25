# Crie um programa que faça o computador jogar JOKENPÔ com você. (Pedra, papel, tesoura)

from random import randint  # Biblioteca para sortear um número

from time import sleep

print("-=-==" * 3)
print("\033[4;30;41mJOKENPÔ GAMING\033[m")
print("-=-==" * 3)

print(
    """OPÇÕES DE JOGO: 
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA"""
)

while True:
    usuario = int(input("Qual é a sua jogada? "))

    if usuario == 1:
        print("PEDRA")
        break
    elif usuario == 2:
        print("PAPEL")
        break
    elif usuario == 3:
        print("TESOURA")
        break
    else:
        print("❌ Jogada inválida. Tente novamente.\n")

print("O computador jogou: ")

computador = randint(1, 3)

if computador == 1:
    print("PEDRA")
elif computador == 2:
    print("PAPEL")
else:
    print("TESOURA")

print("\033[1;34;40mJO...\033[m")
sleep(1)  # Tempo para o procesamento em segundos
print("\033[1;34;40mKEN...\033[m")
sleep(1)
print("\033[1;34;40mPÔ!!\033[m")
sleep(1)

if usuario == computador:
    print("\033[1;33mEmpate\033[m")
elif (
    (usuario == 1 and computador == 3)
    or (usuario == 2 and computador == 1)
    or (usuario == 3 and computador == 2)
):
    print("VITORIA DO \033[1;33mUSUÁRIO\033[m")
else:
    print("VITORIA DO \033[1;33mCOMPUTADOR\033[m")
