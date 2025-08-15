import os
os.system("cls")

numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))


# Operações

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2

# Verificação para evitar divisão por zero

if numero2 != 0:
    divisao = numero1 / numero2
else:
    divisao = "Não é possível dividir por zero."

# Exibição dos dados iniciais e dos resultados
print("\n--- Resultados ---")
print(f"Número 1: {numero1}")
print(f"Número 2: {numero2}")
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")