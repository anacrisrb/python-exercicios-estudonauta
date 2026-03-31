# Crie um programa que leia dois valores e mostre um menu na tela:

# [1] Somar
# [2] Multiplicar
# [3] Maior
# [4] Novos números (Digitar novos números)
# [5] Sair do programa

# Seu programa deverá realizar a operação solicitada em cada caso.

print("—=-=" * 5)
print("MENU DE OPÇÕES")
print("[1] Somar")
print("[2] Multiplicar")
print("[3] Maior")
print("[4] Novos números")
print("[5] Sair")
print("—=-=" * 5)

n1 = int(input(f"Informe o primeiro valor: "))
n2 = int(input(f"Informe o segundo valor: "))

opcao = 0

while opcao != 5:
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print(f"Soma é igual: {n1 + n2}")
    elif opcao == 2:
        print(f"Multiplicação é igual a: {n1 * n2}")
    elif opcao == 3:
        if n1 > n2:
            print(f"Maior é igual a {n1}")
        elif n2 > n1:
            print(f"Maior é igual a {n2}")
        else:
            print(f"Os dois números são iguais!")
    elif opcao == 4:
        n1 = int(input(f"Informe o primeiro valor: "))
        n2 = int(input(f"Informe o segundo valor: "))
    elif opcao == 5:
        print(f"\033[1;36;40mSAINDO DO PROGRAMA...\033[m")
    else:
        print("Opção inválida! Tente novamente.")
