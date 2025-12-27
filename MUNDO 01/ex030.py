# Crie um progrma que leia um número inteiro qualquer e mostre na tela se ele é par ou impar

numero = int(input("Informe um número inteiro qualquer: "))

if numero % 2 == 0:
    print("O número {} é PAR!".format(numero))
else:
    print("O número {} é IMPAR!".format(numero))