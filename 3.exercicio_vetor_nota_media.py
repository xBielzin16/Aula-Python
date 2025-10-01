import os
os.system("cls")

# Criando um vetor (lista).
lista_notas = []

QUANTIDADE_NOTAS = 3

# Inserindo notas.
for i in range(QUANTIDADE_NOTAS):
   nota = int(input(f"Digite a {i+1}ª nota:"))
   lista_notas.append(nota)

# soma += nota
media = sum(lista_notas) / len(lista_notas)

# Mostrar notas:
# print(f"Nota: {lista_notas}")
# print(f"Nota: {lista_notas[0]}")
# print(f"Nota: {lista_notas[1]}")
# print(f"Nota: {lista_notas[2]}")
print("\nResultado:")
for i in range(QUANTIDADE_NOTAS):
   print(f"Nota: {lista_notas[i]}")

print(f"Média: {media}")

print("FIM")