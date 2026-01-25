# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o.

soma = 0
cont = 0
for num in range(1,7):
    num1 = int(input("Digite {} número: ".format(num)))
    if num1 % 2 == 0:
        soma += num1
        cont += 1
print(f"A soma dos {cont} números PARES digitados é {soma}.")


