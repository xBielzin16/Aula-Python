import os
os.system ("cls")

soma_notas = 0
contador = 0

while True:
    nota = float(input("Digite a nota: "))

    soma_notas += nota
    contador += 1

    resposta = input("Deseja inserir mais uma nota? (S/N): ").strip().upper()
    if resposta == "N":
        media = soma_notas / contador
        print(f"A média aritmética das notas é: {media:.2f}")
        break