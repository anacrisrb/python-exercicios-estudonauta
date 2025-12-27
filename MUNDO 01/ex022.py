"Crie um programa que leia o nome completo de uma pessoa e mostre:"
from itertools import count
from os.path import split

" - O nome com todas as letras maiúsculas"
" - O nome com todas as letras minúsculas"
" - Quantas letras ao todo (sem considerar os espaços)"
" - Quantas letras tem o primeiro nome"

nome = str(input("Digite seu nome completo: ")).strip()
print("Seu nome em maiúsculas é {}".format(nome.upper()))
print("Seu nome em minúsculas é", nome.lower())
print("O seu nome tem ao todo {} letras".format(len(nome.replace(" ", ""))))
print("O seu nome tem ao todo {} letras".format(len(nome) - nome.count(" "))) # Alternativo
print("Seu primeiro nome tem {} letras".format(len(nome.split()[0])))
print("Seu primeiro nome tem {} letras".format(nome.find(" "))) # Alternativo



