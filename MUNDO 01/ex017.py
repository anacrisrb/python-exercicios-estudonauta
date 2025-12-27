"Faça um porgrama que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retangulo, cacule e mostre o comprimento da hipotenusa."

from math import hypot

cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))

cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

hipotenusa = hypot(cateto_oposto, cateto_adjacente)

print("O valor da hipotenusa é igual a: {:.2f}".format(hipotenusa))
