# Crie um programa que leia o ano de nascimento de 7 pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas são maiores.

# Considere a maioridade com 21 anos.

# Crie um programa que leia o ano de nascimento de 7 pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas são maiores.

# Considere a maioridade com 21 anos.

from datetime import date

ano_atual = date.today().year
cont_maior = 0
cont_menor = 0

for c in range(1, 8):
    ano_nasc = int(input(f"Informe o ano de nascimento da {c}ª pessoa: "))
    idade = ano_atual - ano_nasc

    if idade >= 21:
        cont_maior += 1
    else:
        cont_menor += 1

print("-" * 30)
print(f"{cont_maior} pessoas são maiores de idade.")
print(f"{cont_menor} pessoas são menores de idade.")
