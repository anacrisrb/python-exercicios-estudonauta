# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

# A média de idade do grupo
# Qual é o nome do homem mais velho
# Quantas mulheres têm menos de 20 anos.

soma_idade = 0
homem_mais_velho = " "
maior_idade_homem = 0
mulheres_menor_20 = 0

for c in range (1,5):
    nome = str(input(f"Informe o nome da {c}ª pessoa: "))
    idade = int(input(f"Informe a idade da {c}ª pessoa: "))
    sexo = str(input(f"Informe o sexo (F/M) da {c}ª pessoa: ")).upper()

    soma_idade += idade

    if sexo == "M":
        if idade > maior_idade_homem: # Comparando a idade do homem atual com a maior já registrada
            maior_idade_homem = idade
            homem_mais_velho = nome

    if sexo == "F" and idade < 20: # Validando quantidade de mulheres com menos de 20 anos
        mulheres_menor_20 += 1

media_idade = soma_idade / 4
print()
print(f"Média de idade do grupo: {media_idade}")
print(f"Homem mais velho: {homem_mais_velho}")
print(f"Mulheres com menos de 20 anos: {mulheres_menor_20}")
