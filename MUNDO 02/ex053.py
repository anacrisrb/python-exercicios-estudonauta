# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsidere os espaços.

# Frase que pode ser lida de frente pra trás e de trás pra frente

# Ex: Apos a sopa // A sacada da casa // A torre da derrota // Anotaram a data da maratona // O lobo a ama o bolo

frase = (str(input("Digite uma frase: ")).strip().upper())  # Desconsiderar os espaços e colocando letras maiusculas
palavras = frase.split()  # Separando a frase em listas de palavras
junto = ''.join(palavras)  # Eliminado os espaços
inverso = ''
for letra in range(len(junto) -1, -1, -1):  # Puxando da ultima letra até a primeira (Len - qtde de caracteres)
    inverso += junto[letra]
print("O inverso de {} é {}".format(junto, inverso))
if inverso == junto:
    print("A frase digitada é um PALÍNDROMO")
else:
    print("A frase digitada NÃO é um PALÍNDROMO")
