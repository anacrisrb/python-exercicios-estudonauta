# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

cont = 0
soma = 0
num = 0
resp = "S"

while resp == "S":
    n = int(input(f"Digite um número: "))
    cont += 1 # Cont + 1...
    soma += n #Soma + n...

    if cont == 1:  # Comparação
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n

    resp = input("Quer continuar? [S/N] ").strip().upper()
    while resp not in "SN": # Caso o usuário digite a opçao incorreta
        resp = input(f"Opção inválida. Deseja continuar? [S/N] ").strip().upper()

media = soma / cont

print("A média é igual a: {:.0f}".format(media))
print("O MAIOR valor digitado foi {}".format(maior), end=" ") # End para não ter salto de linha, apenas quebra e continuação
print("e o MENOR valor digitado foi {}.".format(menor))
