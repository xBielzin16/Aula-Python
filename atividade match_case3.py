# Exercício 5

import os
os.system ("cls")

# Solicita o valor do produto
valor_produto = float(input("Informe o valor do produto: R$ "))

# Solicita a forma de pagamento
print("Forma de pagamento:")
print("1 - Pagamento à vista")
print("2 - Pagamento à prazo")
forma_pagamento = int(input("Escolha a forma de pagamento (1 ou 2): "))

match forma_pagamento:
    case 1:
        # Aplicar desconto de 10%
        desconto = valor_produto * 0.10
        total_a_pagar = valor_produto - desconto
        print("\nPagamento à vista:")
        print(f"Valor do produto: R$ {valor_produto:.2f}")
        print(f"Forma de pagamento: à vista")
        print(f"Valor do desconto: R$ {desconto:.2f}")
        print(f"Total a pagar: R$ {total_a_pagar:.2f}")

    case 2:
        parcelas = int(input("Digite a quantidade de parcelas (até 6): "))
        if parcelas < 1 or parcelas > 6:
            print("Número de parcelas inválido! Deve ser entre 1 e 6.")
        else:
            valor_parcela = valor_produto / parcelas
            print("\nPagamento à prazo:")
            print(f"Valor do produto: R$ {valor_produto:.2f}")
            print(f"Forma de pagamento: à prazo")
            print(f"Quantidade de parcelas: {parcelas}")
            print(f"Valor por parcela: R$ {valor_parcela:.2f}")
            print(f"Total à prazo: R$ {valor_produto:.2f}")

    case _:
        print("Forma de pagamento inválida!")
