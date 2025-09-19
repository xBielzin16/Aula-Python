import os
os.system("cls")

soma = 0
quantidade = 0

while True:
    numero = int(input("Digite um número inteiro positivo (ou negativo): "))

    if numero < 0:
        break

    soma += numero
    quantidade += 1

    if quantidade > 0:
        media = soma / quantidade
        print(f"A média aritmética dos números informados é: {media:.2f}")
    else:
        print("Nenhum número positivo foi informado.")