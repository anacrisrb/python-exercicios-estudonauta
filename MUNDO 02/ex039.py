# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:

# Se ele ainda vai ser alistar ao serviço militar.
# Se é a hora de se alistar
# Se já passou do tempo de alistamento

# Seu programa também deverá mostar o tempo que falta ou que passou do prazo.

from datetime import date

ano_nasc = int(input("Informe o ano de nascimento: "))
ano_atual = date.today().year
idade = ano_atual - ano_nasc

if idade < 18:
    tempo_restante = 18 - idade
    print(f"A idade mínima para o ALISTAMENTO é 18 anos.")
    print(
        f"A sua idade atual é {idade} anos. "
        f"O seu alistamento obrigatório será daqui {tempo_restante} ano(s)."
    )
elif idade == 18:
    print("A hora de se alistar chegou.")
elif idade > 18:
    tempo_ultrapassado = idade - 18
    print("Você já passou do tempo de alistamento.")
    print(
        f"A sua idade atual é {idade} anos. "
        f"Já se passaram {tempo_ultrapassado} ano(s) do prazo para o alistamento obrigátorio."
    )
    print(
        "\033[1;33mProcure uma unidade de atendimento da JSM para regularizar a sua situação!\033[m"
    )
