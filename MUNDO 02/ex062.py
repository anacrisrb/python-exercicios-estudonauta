# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando  ele disser que quer mostrar 0 termos.

primeiro_termo = int(input("Digite o primeiro termo: "))
razao = int(input("Informe a razao: "))

termo = primeiro_termo
contador = 1
total = 10

print(
    "Os 10 primeiros termos da PA são: "
)  # Termo digitado mais a razao // iniciando no primeiro

while contador <= 10:
    print(termo, end=" ")  # end para imprimir tudo na mesma linha (separado por espaço)
    termo += razao
    contador += 1  # Vai finalizar quando chegar no décimo

print()
mais = int(input(f"Quantos termos mais deseja mostrar? "))

while mais != 0:
    total += mais  # aumenta o total de termos

    while contador <= total:
        print(termo, end=" ")
        termo += razao
        contador += 1

    print()
    mais = int(input("Quantos termos mais deseja mostrar? "))

print("\033[1;31;40mPrograma encerrado.\033[m")
