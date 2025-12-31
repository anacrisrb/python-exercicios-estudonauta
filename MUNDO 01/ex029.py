# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa de deve custar R$ 7,00 por cada KM acima do limite.

velocidade = float(input("Qual é a velocidade atual do carro? "))

multa = (velocidade - 80) * 7

if velocidade > 80:
    print("MULTADO! Você excedeu o limite permitido que é de 80 Km/h.")
    print()
    print("-=--=" * 8)
    print("Você deve pagar uma multa de R$ {:.2f}".format(multa))
    print("-=--=" * 8)
else:
    print()
    print("Tenha um bom dia! Dirija com segurança!")
