"Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'Santo"

cidade = str(input('Informe o nome da cidade: ')).strip()

print("A cidade começa com a palavra 'Santo'? {}".format(cidade[:5].upper() == 'SANTO'))

