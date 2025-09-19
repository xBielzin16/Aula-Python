import os
os.system("cls")

# Inicializa as variáveis para contar pares, ímpares e somar os números
quantidade_pares = 0
quantidade_impares = 0
soma_pares = 0
soma_total = 0
quantidade_total = 0

while True:
    # Lê um número inteiro
    numero = int(input("Digite um número positivo (0 para encerrar): "))
    
    # Se o número for zero, termina a leitura
    if numero == 0:
        break
    
    # Soma o número total
    soma_total += numero
    quantidade_total += 1
    
    # Verifica se o número é par ou ímpar
    if numero % 2 == 0:
        quantidade_pares += 1
        soma_pares += numero
    else:
        quantidade_impares += 1

# Calcula as médias
if quantidade_pares > 0:
    media_pares = soma_pares / quantidade_pares
else:
    media_pares = 0  # Se não houver números pares

if quantidade_total > 0:
    media_total = soma_total / quantidade_total
else:
    media_total = 0  # Se não houver números lidos

# Exibe os resultados
print(f"Quantidade de números pares: {quantidade_pares}")
print(f"Quantidade de números ímpares: {quantidade_impares}")
print(f"Média dos números pares: {media_pares:.2f}")
print(f"Média geral dos números lidos: {media_total:.2f}")
