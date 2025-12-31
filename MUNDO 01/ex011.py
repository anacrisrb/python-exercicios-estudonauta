"""Faça um programa que leia a largura e a altura de uma parede em metros, e calcule a sua àrea e a quantidade de
tinta necessária para pinta-lá, sabendo que cada litro de tinta pinta uma àrea de 2m².
"""

largura = float(input("Digite a largura da parede (em metros): "))
altura = float(input("Digite a altura da parede (em metros): "))

area = largura * altura

tinta = area / 2

print(
    "Sua parede tem a dimensão de {}x{} e sua área é de {:.2f}m².".format(
        largura, altura, area
    )
)
print("Para pintar essa parede, você precisará de {:.2f}l de tinta.".format(tinta))
