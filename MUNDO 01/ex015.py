"Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias que ele foi alugado."
"Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por KM rodado."

dias = int(input("Por quantos dias o carro foi alugado? "))
km = float(input("Quantos KM foram rodados? "))

total = (dias * 60.00) + (km * 0.15)

print("O total a pagar é de R$ {:.2f}".format(total))
