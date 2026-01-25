# Desenvolva uma lógica  que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
from sys import float_repr_style

# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida

peso = float(input("Qual é seu peso? (Kg) "))
altura = float(input("Qual é sua altura: (m) "))

imc = peso / (altura**2)
print(f"O seu IMC é de {imc:.1f}")

if imc < 18.5:
    print("Você está ABAIXO DO PESO")
elif 18.5 <= imc < 25:
    print("Parabéns, você está na faixa de PESO IDEAL")
elif 25 <= imc < 30:
    print("Você está em SOBREPRESO")
elif 30 <= imc < 40:
    print("Você está em OBESIDADE")
else:
    print("Você está em OBESIDADE MÓRBITA, cuidado")
