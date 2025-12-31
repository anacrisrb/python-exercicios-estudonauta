# Desevolva um programa que leia o comprimento de três retas e diga ao usuário se eles podem ou não formar um triângulo.

# Soma de dois segmentos > que o terceiro segmento #

print("-=--=" * 5)
print("ANALISADOR DE TRIÂNGULOS")
print("-=--=" * 5)

seg1 = float(input("Digite o primeiro segmento: "))
seg2 = float(input("Digite o segundo segmento: "))
seg3 = float(input("Digite o terceiro segmento: "))

if seg1 + seg2 > seg3 and seg1 + seg3 > seg2 and seg3 + seg2 > seg1:
    print("A soma dos segmentos podem FORMAR um TRIÂNGULO")
else:
    print("A soma dos segmentos NÃO podem formar um TRIÂNGULO")
