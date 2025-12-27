""""Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar."""
# Considere: US$ = R$ 3,27

saldo = float(input("Qual o seu saldo atual? R$ "))

dolares = saldo/3.27

print("Com R${:.2f} você pode comprar ${:.2f} USD".format(saldo,dolares))
