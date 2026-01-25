# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:

# Se ele ainda vai ser alistar ao serviço militar.
# Se é a hora de se alistar
# Se já passou do tempo de alistamento

# Seu programa também deverá mostar o tempo que falta ou que passou do prazo.

from datetime import date

ano_nasc = int(input("Informe o ano de nascimento: "))

ano_atual = date.today().year
idade = ano_atual - ano_nasc

sexo = str(input("Informe o seu sexo [F/M]: ")).upper().strip()[0]

if sexo == "F":
    print("O alistamento é obrigatório somente para o sexo masculino")
else:
    print(f"Quem nasceu em {ano_nasc} tem {idade} anos em {ano_atual}.", end="")
    print(" A idade para o ALISTAMENTO OBRIGATÓRIO é: 18 anos.")

    if idade == 18:
        print("Você tem que se alistar IMEDIATAMENTE")
    elif idade < 18:
        saldo = 18 - idade
        print(f"O seu alistamento será daqui {saldo} ano(s).")
        ano = saldo + ano_atual
        print(f"O seu alistamento será em {ano}.")
    else:
        saldo = idade - 18
        print(f"Já se passaram {saldo} ano(s) do prazo para o alistamento obrigátorio.")
        ano = ano_atual - saldo
        print(f"Você deveria ter se alistado em {ano}.")
        print(
            "\033[1;31mProcure uma unidade de atendimento da JSM para regularizar a sua situação!\033[m"
        )
