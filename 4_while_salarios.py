import os
os.system ("cls")

# Definindo variaveis
total_familias = 0
media_salario = 0
media_filhos = 0
maior_salario = 0
menor_salario = 0


while True:
    os.system("cls")
    print("""
Código  |   Descrição
    1   | Adicionar familia
    2   | Sair e exibir resultados
""")

    opcao = int(input("Digite a opção desejada: "))
    match opcao:
        case 1:
            # Solicitando dados.
            salario = float(input("Informe o salário da família: "))
            filhos = int(input("Informe o número de filhos da família: "))

            total_familias += 1
            media_salario += salario
            media_filhos += filhos

            if salario > maior_salario:
                maior_salario = salario

            if salario < menor_salario:
                menor_salario = salario

        case 2:
            if total_familias == 0:
                print("Nenhuma família foi cadastrada.")
            else:
                media_salario = media_salario / total_familias
                media_filhos = media_filhos / total_familias

                print("\nResultados da Pesquisa: ")
                print(f"a) Total de famílias: {total_familias}")
                print(f"b) Média de salário: R$ {media_filhos:.2f}")
                print(f"c) Média de número de filhos: {media_filhos:.2f}")
                print(f"d) Maior salário: R$ {maior_salario:2f}")
                print(f"e) Menor salário: R$ {menor_salario:2f}")
            break

        case _:
            print("Opção inválida. Digite 1 ou 2.")