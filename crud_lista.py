import os
os.system("cls")

lista_clientes = []

nome = input("Informe o seu nome: ")
lista_clientes.append(nome)
print(f"O Nome: {nome} foi inserido com sucesso!")

print("\nRead - Ler / Mostrar")
print(lista_clientes)

print("\nUpdate - Atualizar / Alterar")
nome_para_atualizar = nome
if nome_para_atualizar in lista_clientes:
    novo_nome = "Marta Silva"
    indice = lista_clientes.index(nome_para_atualizar)
    print(f"O nome: {nome_para_atualizar} foi atualizado para: {novo_nome}.")
else:
    print(f"O nome: {nome_para_atualizar} não foi encontrado")

print(lista_clientes)

print("\nDelete - Excluir / Remover")
nome_para_excluir = "Marta Silva"
if nome_para_excluir in lista_clientes:
    lista_clientes.remove(nome_para_excluir)
    print(f"{nome_para_excluir} foi excluído com sucesso!")
else:
    print(f"O nome {nome_para_excluir} não foi encontrado.")

print(lista_clientes)