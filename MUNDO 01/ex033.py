# Faça um programa que leia três números e mostre qual é o menor e qual é o maior.

n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o segundo número: "))
n3 = int(input("Informe o terceiro número: "))

# Verificando o número menor:
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

# Verificando o número maior:
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print("O menor valor digitado foi:", menor)
print("O maior valor digitado foi:", maior)

# Usando outras funções:

print("O menor valor digitado foi:", min(n1,n2,n3))
print("O menor valor digitado foi:", max(n1,n2,n3))


