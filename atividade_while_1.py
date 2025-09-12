import os
os.system("cls")


print("Nota do aluno")

while True:
    nota = int(input("Digite a nota: "))
    if nota < 0 or nota > 10:
        break

print(f"Sua nota é: {nota}")
print("FIM.")
        