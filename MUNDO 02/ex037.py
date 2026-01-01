# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:

# 1 para binário
# 2 pra octal
# 3 para hexadecimal

num = int(input("Digite um número inteiro: "))

print("-=-==" * 8)
print(" ESCOLHA UMA DAS BASES PARA CONVERSÃO: ")
print("-=-==" * 8)

print(
    """
[ 1 ] Converter para binário
[ 2 ] Converter para octal
[ 3 ] Converter para hexadecimal
"""
)

while True:
    opcao = int(input("Informe opcao desejada: "))

    if opcao == 1:
        print(
            f"O número {num} convertido para BINÁRIO é igual a: \033[1;34m{bin(num)[2:]}\033[m"
        )
        # Fatiamento de strings (trabalhando em pedaços) removendo as duas primeiras casas (0b, 0c, 0x)
        break
    elif opcao == 2:
        print(
            f"O número {num} convertido para OCTAL é igual a: \033[1;34m{(oct(num))[2:]}\033[m"
        )
        break
    elif opcao == 3:
        print(
            f"O número {num} convertido pra HEXADECIMAL é igual a: \033[1;34m{hex(num)[2:]}\033[m"
        )
        break
    else:
        print("\033[1;31mA opção informada é INVÁLIDA! Tente novamente!\033[m")
