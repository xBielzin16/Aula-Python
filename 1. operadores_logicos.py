import os
os.system ("cls")

nota = -2

#Se a nota menor que zero ou maior que 10.
# OR -> Fora do intervalo definido.
if nota < 0 or nota > 10:
    print("Nota inválida.")
else:
    print(f"Nota: {nota}")