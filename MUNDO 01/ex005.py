"""Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor"""

n1 = int(input("Digite um numero: "))
sucessor = n1 + 1
antecessor = n1 - 1
print("Analisando o valor {}, seu antecessor é {} e seu sucessor é {}".format(n1, antecessor, sucessor))


n2 = int(input("Digite um numero: "))
print("Analisando o valor {}, seu antecessor é {} e seu sucessor é {}".format(n2, (n2-1), (n2+1)))

