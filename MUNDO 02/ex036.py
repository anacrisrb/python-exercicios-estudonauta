# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar.

# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então  o empréstimo será negado.


financiamento = float(input("Qual o valor da casa a ser financiada? R$"))
salario = float(input("Qual o salário do comprador? R$"))
anos = int(input("Quantos anos de financiamento? "))

if anos <= 0:
    print("O prazo de financiamento deve ser maior que zero.")
    exit()
else:
    meses = anos * 12
    prestacao = financiamento / meses
    limite_prestacao = salario * 0.3

if prestacao <= limite_prestacao:
    print(
        f"Empréstimo \033[1;32mCONCEDIDO.\033[m Para pagar uma casa de R$ {financiamento:.2f} em {anos} anos",
        end="",
    )
    print(f" a prestação será de R${prestacao:.2f}")
else:
    print(
        f"Empréstimo \033[1;31mNEGADO.\033[m Para pagar uma casa de R$ {financiamento:.2f} em {anos} anos,",
        end="",
    )
    print(f" a prestação será de R${prestacao:.2f}")
