# Desenvolva um programa que leia o primeiro termo e a razao de uma PA. No final, mostre os 10 primeiros termos dessa progressão

primeiro_termo = int(input("Informe o primeiro termo: "))
razao = int(input("Informe a razão: "))

print(f"Os 10 primeiros termos da PA são: ")

termo = primeiro_termo

for c in range(10):
    print(termo, end=" ")
    termo += razao
