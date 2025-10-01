import os
os.system("cls")

lista_notas= []

# Constante
QUANTIDADE_NOTAS = 4

for i in range(QUANTIDADE_NOTAS):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    lista_notas.append(nota)

    media = sum(lista_notas) / len(lista_notas)

if lista_notas [i] >= 7:
    resultado = "Aprovado."
elif lista_notas [i] >= 5:
    resultado = "Recuperação."
else:
    resultado = "Reprovado."

# Mostrar notas:
print("\nResultado:")
for i in range(QUANTIDADE_NOTAS):
    print(f"Nota: {lista_notas[i]}")

print(f"\nMédia: {media}")
print(f"Resultado: {resultado}")

print("FIM!")