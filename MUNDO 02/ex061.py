# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro_termo = int(input("Digite o primeiro termo: "))
razao = int(input("Informe a razao: "))

termo = primeiro_termo
contador = 1

print("Os 10 primeiros termos da PA são: ")

while contador <= 10:
    print(termo, end=" ")  # end para imprimir tudo na mesma linha (separado por espaço)
    termo += razao
    contador += 1  # Vai finalizar quando chegar no décimo
