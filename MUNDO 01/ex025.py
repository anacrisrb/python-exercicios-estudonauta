"Crie um programa que leia o nome de uma pessoa e diga se ela tema 'Silva' no nome."

nome = str(input("Informe seu nome completo: ")).strip()

print("Seu nome tem Silva? {}".format("SILVA" in nome.upper()))
