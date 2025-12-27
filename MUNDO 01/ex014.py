"Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF"

temperatura = float(input("Informa a temperatura em ºC: "))

conversao = (temperatura * 1.8) + 32

print("A temperatura de {}ºC corresponde a {}ºF!".format(temperatura,conversao))
