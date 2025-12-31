"Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro o último nome separadamente"

"Ex: Ana Maria de Souza"
"Primeiro: Ana"
"Último: Souza"

nome = str(
    input("Digite seu nome completo: ")
).split()  # Cria uma divisão onde há espaços criando uma lista

print(
    "Muito prazer em te conhecer, {}!".format(" ".join(nome))
)  # Transforma a lista de volta em texto (exibição)

print("Seu primeiro nome é: {}".format(nome[0]))

print("Seu último nome é: {}".format(nome[-1]))
