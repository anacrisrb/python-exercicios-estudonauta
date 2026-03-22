# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input("Informe o sexo da pessoa [F/M]: ")).upper()

while sexo != "F" and sexo != "M":
    sexo = input(f"Valor inválido. Infomre novamente [F/M]: ")

print(f"Sexo informado: {sexo}")
