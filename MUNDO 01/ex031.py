# Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem, cobrando R$ 0.50 por km para viagens de até 200 km e
# R$ 0,45 para viagens mais longas.

distancia = float(input("Qual é a distância da sua viagem? "))

print("A sua viagem tem uma distância total de {:.2f} KM".format(distancia))

if distancia <= 200:
    print("O valor da sua passagem será de R$ {:.2f}".format(distancia * 0.5))
else:
    print("O valor da sua passagem será de R$ {:.2f}".format(distancia * 0.45))
