# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

for num_pares in range(
    2, 51, 2
):  # Fazendo as iterações de 2 em 2 para diminuir a qtde de laços
    if num_pares % 2 == 0:
        print(num_pares, end=" ")
print("Acabou")
