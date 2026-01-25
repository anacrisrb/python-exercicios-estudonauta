# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, so que agora utilizando um laço for.

num = int(input("Digite um numero para ver sua tabuada: "))
print()
for a in range(1,11):
    print("{} x {} = {}".format(num, a, a * num))
    print("-=-==" * 2)
print()
print("Fim")





