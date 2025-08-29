import os
os.system ("cls")

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
op = input("Digite o operador (+, -, *, /): ")

match op:
    case "+":
        resultado = n1 + n2
    case "-":
        resultado = n1 - n2
    case "*":
        resultado = n1 * n2
    case "/":
        if n2 != 0:
            resultado = n1 / n2
        else:
            resultado = "Erro: divisão por zero!"
    case _:
        resultado = "Operador inválido!"

print(f"Números: {n1} e {n2}")
print(f"Operador escolhido: {op}")
print(f"Resultado: {resultado}")