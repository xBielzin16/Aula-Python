import os
os.system ("cls")

idade = int(input("Digite sua idade: "))

if idade >= 18 and idade <= 65:
    print("Obrigado a votar.")
elif idade >= 16 or idade > 65:
    print("Voto facultativo.")
else:
    print("Não é obrigado a votar!")