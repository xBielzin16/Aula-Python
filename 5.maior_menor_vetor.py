import os
os.system("cls")

lista_numeros = []

QUANTIDADE_NUMEROS = 5

for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite o {i + 1}º número: "))
    lista_numeros.append(numero)

menor_valor = min(lista_numeros)
maior_valor = max(lista_numeros)

for i in range(QUANTIDADE_NUMEROS):
    print(f"Número:  {lista_numeros[i]}")

print(f"O menor número é: {menor_valor}")
print(f"O maior número é: {max(lista_numeros)}")
