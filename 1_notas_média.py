import os
os.system("cls")

QUANTIDADES_NOTAS = 2
soma = 0

for i in range(QUANTIDADES_NOTAS):
    while True:
        nota = int(input("Digite sua nota: "))
        if nota < 0 or nota > 10:
            print("A nota inválida.")
        else:
            soma += nota
            break

media = soma / 2

print(f"Média: {media}")