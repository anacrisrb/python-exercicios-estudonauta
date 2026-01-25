# Faça um programa que calcule a soma de todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0
cont = 0
for num in range(1, 501, 2):  # Pulando de 2 em 2  (1,3,5...)
    if num % 2 != 0 and num % 3 == 0:
        cont += 1  # Contando a quantidade de números
        soma += num  # Acumulando os valores
print(f"A soma de todos os {cont} valores solicitados é {soma}")
print("Acabou")
