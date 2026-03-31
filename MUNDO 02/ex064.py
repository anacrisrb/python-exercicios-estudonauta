# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.

# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

cont = 0
soma = 0

n = int(input("Digite um número: "))

while n != 999:
    cont += 1
    soma += n
    n = int(input("Digite um número: "))

print(f"Parando o programa.")
print(f"Foram digitados {cont} números", end=" ")
print(f"e  soma entre o números digitados é igual a: {soma}")
