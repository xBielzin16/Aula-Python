import os
os.system("cls")

lista_numeros = []

positivo = []
negativo = []

QUANTIDADE_NUMEROS = 5

for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite o {i + 1}º número: "))
    lista_numeros.append(numero)

    if numero < 0:
        negativo.append(numero)
    else:
        positivo.append(numero)
        

print("\n= RESULTADO =")
print(f"A quantidade de números negativos é: {len(negativo)}")
print(f"A soma dos números positivos é: {sum(positivo)}")