# Escreva um programa que leia dois números inteiros e compare-os mostrando na tela uma das seguintes mensagens:

# O primeiro valor é MAIOR
# O segundo valor é MAIOR
# Não existe valor maior, os dois são iguais.

num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))

if num1 > num2:
    print("O PRIMEIRO valor informado é \033[1;34;40mMAIOR\033[m")
elif num1 < num2:
    print("O SEGUNDO valor informado é \033[1;34;40mMAIOR\033[m")
else:
    print("Não existe valor maior, os dois são \033[1;34;40mIGUAIS\033[m")
