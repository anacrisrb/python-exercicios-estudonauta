# Faça o programa que leia o peso de cinco pessoas. No final mostre qual foi o maior e o menor peso lido.

maior = 0
menor = 0

for p in range (1,6):
    peso = float(input(f"Informe o peso da {p}ª pessoa: "))

    if p == 1: # Para comparar com os próximos pesos que serão digitados
        maior = peso
        menor = peso

    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print("-" * 30)
print(f"O maior peso foi {maior} kg.")
print(f"O menor peso foi {menor} kg.")


