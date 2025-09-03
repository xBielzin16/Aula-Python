# Exercício 2

import os
os. system ("cls")

print("""
Código Prato  Valor
 1    Picanha    R$ 25,00
 2    Lasanha    R$ 20,00
 3    Strogonoff   R$ 18,00
 4    Bife Acebolado  R$ 15,00
 5    Pão com ovo   R$ 5,00  
""")

codigo = input("Digite o código do prato desejado: ")

match codigo:
    case "1":
        prato = "Picanha"
        preco = 25
    case "2":
        prato = "Lasanha"
        preco = 20
    case "3":
        prato = "Strogonoff"
        preco = 18
    case "4":
        prato = "Bife Acebolado"
        preco = 15
    case "5":
        prato = "Pão com ovo"
        preco = 5
    case _:
        prato = None
        preco = 0

if prato:
    print(f"Você escolheu o {prato}, que custa R$ {preco},00")
else:
    print("Código inválido! Escolha de 1 a 5.")


print("Volte sempre!")
