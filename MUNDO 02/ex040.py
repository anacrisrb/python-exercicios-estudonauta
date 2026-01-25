# Crie um programa que leia duas notas de um aluno e calcule a sua média, mostrando uma mensagem no final, de acordo com a média atingida:

# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
media = (nota1 + nota2) / 2

print(f"A sua primeira nota foi {nota1} média foi {media:.2f}")

if media < 5.0:
    print(f"Aluno \033[1;31mREPROVADO\033[m")
elif 5.0 <= media <= 6.9:
    print(f"Aluno de \033[1;33mRECUPERAÇÃO\033[m")
elif media >= 7:
    print(f"Aluno \033[1;36mAPROVADO\033[m")
