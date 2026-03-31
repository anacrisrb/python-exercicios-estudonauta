# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

cont = 0
soma = 0
num = 0
resp = "S"

while resp == "S":
    n = int(input(f"Digite um número: "))
    cont += 1
    soma += n

    if cont == 1:  # Validar a comparação com um unico numero
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n

    resp = input("Quer continuar? [S/N] ").strip().upper()
    while resp not in "SN":
        resp = input(f"Opção inválida. Deseja continuar? [S/N]").strip().upper()

media = soma / cont

print("A média entre o números digitados foi {:.0f}".format(media))
print("O MAIOR valor digitado foi {}".format(maior), end=" ")
print("e o MENOR valor digitado foi {}.".format(menor))
