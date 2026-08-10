
# Exercício 1: Leia a idade de uma pessoa e informe se ela é:
def idade_pessoa():
    idade = int(input("Digite sua idade: "))
    if idade < 18:
        print("Você é menor de idade.")
    elif idade < 60:
        print("Você é maior de idade.")
    else:
        print("Você é idoso.")

idade_pessoa()

# # Exercício 2: Leia três notas, calcule a média e informe se o aluno está:
# def nota(a, b, c):
#     media = (a + b + c) / 3
#     if media >= 7:
#         print(f"Aprovado com média {media:.2f}")
#     elif media >= 5:
#         print(f"Recuperação com média {media:.2f}")
#     else:
#         print(f"Reprovado com média {media:.2f}")

# nota(7, 8, 9)

# # Exercício 3: Crie um programa que leia um número e informe se ele é:
# def condicao():
#     numero = int(input("Digite um numero: "))
#     if numero > 0:
#         print("O numero é positivo")
#     elif numero < 0:
#         print("O numero é negativo")
#     else:
#         print("O numero é zero")

# condicao()



