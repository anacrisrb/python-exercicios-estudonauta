# Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento:

# À vista no dinheiro ou cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

print("-=-==" * 4)
print("\033[1;30;43mMENU DE PRODUTOS:\033[m")
print("-=-==" * 4)

print("[ 1 ] Bicicleta")
print("[ 2 ] Iphone 16 pro max")
print("[ 3 ] Mochila Adidas")
print("[ 4 ] Chuteira")

while True:
    produto = int(input("\033[1;31mInforme o produto desejado: \033[m"))

    if produto == 1:
        print("Bicicleta")
        preco = 900.00
        break
    elif produto == 2:
        print("Iphone 16 Pro Max")
        preco = 1500.00
        break
    elif produto == 3:
        print("Mochila Adidas")
        preco = 300.00
        break
    elif produto == 4:
        print("Chuteira")
        preco = 450.00
        break
    else:
        print("❌ Produto inválido. Tente novamente.\n")


print("-=-==" * 5)
print("\033[1;30;43mCONDIÇOES DE PAGAMENTO: \033[m")
print("-=-==" * 5)

print("[ 1 ] A vista no dinheiro ou cheque: 10% de desconto")
print("[ 2 ] A vista no cartão: 5% de desconto")
print("[ 3 ] Em até 2x no cartão: preço normal")
print("[ 4 ] 3X ou mais no cartão: 20% de juros")

while True:
    pagamento = int(input("\033[1;31mComo o produto será pago? \033[m"))

    if pagamento == 1:
        print(f"Pagamento à vista (dinheiro/cheque). Total: R$ {preco * 0.90:.2f}")
        break
    elif pagamento == 2:
        print(f"Pagamento à vista no cartão. Total: R$ {preco * 0.95:.2f}")
        break
    elif pagamento == 3:
        print(f"Pagamento em até 2x no cartão. Total: R$ {preco:.2f}")
        break
    elif pagamento == 4:
        print(f"Pagamento em 3x ou mais no cartão. Total: R$ {preco * 1.20:.2f}")
        break
    else:
        print("❌ Forma de pagamento inválida. Tente novamente.\n")




