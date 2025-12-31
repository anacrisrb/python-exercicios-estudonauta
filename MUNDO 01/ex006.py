"""Crie um algoritmo que leia um número e mostre o seu dobro, tripo e raiz quadrada."""

# O dobro de x vale x
# O triplo de x vale x
# A raiz quadrada de x é igual a x

n = int(input("Digite um número: "))
dobro = n * 2
triplo = n * 3
raiz = n ** (1 / 2)
print("O dobro de {} vale {}".format(n, dobro))
print("O triplo de {} vale {}".format(n, triplo))
print("A raiz quadrada de {} vale {:.2f}".format(n, raiz))
