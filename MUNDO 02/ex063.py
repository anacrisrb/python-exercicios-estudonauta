# Escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.

# Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

# A sequência de Fibonacci é uma sequência de números em que cada termo (a partir do terceiro) é a soma dos dois anteriores.

n = int(input(f"Informe um número: "))

contador = 1
t1 = 0
t2 = 1

print(f"Os {n} primeiros termos de Fibonacci são:")

while contador <= n:
    print(t1, end=" ")
    t3 = t1 + t2  # T3 é a soma dos dois elementos anteriores
    t1 = t2
    t2 = t3
    contador += 1
