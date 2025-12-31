# Faça um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

# Para salários superiores a R$ 1250,00 calcule um aumento de 10%.

# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Informe o salário do colaborador: "))

print("O seu salário atual é R$ {:.2f}".format(salario))

if salario > 1250:
    aumento = (salario * 10 / 100) + salario
    print(
        "Com o aumento salarial de 10% você passará a receber R$ {:.2f}".format(aumento)
    )
else:
    aumento = (salario * 15 / 100) + salario
    print(
        "Com o aumento salarial de 15% você passará a receber R$ {:.2f}".format(aumento)
    )
