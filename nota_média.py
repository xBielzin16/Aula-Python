import os
os.system("cls")


soma= 0
quantidade_notas = 0

while True:
    nota = float(input("Digite uma nota: "))
    # quantidade_notas = quantidade_notas + 1
    # soma = soma + nota
    quantidade_notas += 1
    soma += nota
    resposta = input("Deseja inserir mais uma nota? \nUse S ou N: ").lower()
    if resposta == "n":
        break

media = soma / quantidade_notas

print(f"\nMédia: {media}")
