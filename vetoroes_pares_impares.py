import os
os.system("cls")

lista_numeros = []
pares = 0
impares = 0

QUANTIDADE_NUMEROS = 6

print(f"Solicitando {QUANTIDADE_NUMEROS} números.")
for i in range(6):
    numero = float(input(f"Digite o {i+1}º número: "))
    if numero % 2 == 0:
            pares += 1
    else:
        impares += 1
    lista_numeros.append(numero)

print("\nMostrando todos os números.")
# for i in range(QUANTIDADE_NUMEROS):
    # print(f"Número: {lista_numero[i]}")

# ForEach
for numero in lista_numeros:
     print(f"Número: {numero}")



print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")