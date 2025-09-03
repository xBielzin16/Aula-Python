# Exercício 6

import os
os.system ("cls")

sexo = input("Digite o sexo (M para Masculino / F para Feminino): ").upper()
altura = float(input("Digite sua altura em metros (ex: 1.75): "))

match sexo:
    case "M":
        peso_ideal = (72.7 * altura) - 58
    case "F":
        peso_ideal = (62.1 * altura) - 44.7
    case _:
        peso_ideal = None

if peso_ideal is not None:
    print(f"O peso ideal é: {peso_ideal: .2f} kg")
else:
    print("Sexo inválido! Digite apenas 'M' ou 'F'. ")