import os
from dataclasses import dataclass
import os

@dataclass
class Funcionario:
    nome: str
    data: int
    matricula: str
    endereco: str


    def exibir_dados (self):
        print(f"Nome: {self.nome}, Data de Admissão: {self.data}, Matrícula: {self.matricula}, Endereço: {self.endereco}")

@dataclass
class Cliente:
    nome: str
    data: int
    endereco: str

    def exibir_dados(self):
        print(f"Nome: {self.nome}, Data de Nascimento: {self.data}, Endereço: {self.endereco}")

lista_de_funcionarios = []
lista_de_clientes = []
QUANTIDADE_FUNCIONARIOS = 3
QUANTIDADE_CLIENTES = 3

for i in range (QUANTIDADE_FUNCIONARIOS):
    funcionario = Funcionario(
        nome= input("Digite seu nome: "),
        data= int(input("Digite a data de admissão: ")),
        matricula= input("Digite sua matrícula: "),
        endereco= input("Digite seu endereço: "),
    )
    lista_de_funcionarios.append(funcionario)
    print()
    os.system("cls")

for i in range (QUANTIDADE_CLIENTES):
    cliente = Cliente(
        nome= input("Digite seu nome: "),
        data= int(input("Digite sua data de nascimento: ")),
        endereco= input("Digite seu endereço: ")
    )
    lista_de_clientes.append(cliente)
    print()
    os.system("cls")

nome_do_arquivo = "dados_funcionários.txt"
with open(nome_do_arquivo, "a", encoding="UTF-8") as arquivo_funcionarios:
    for funcionario in lista_de_funcionarios:
        arquivo_funcionarios.write(f"{funcionario.nome}, {funcionario.data}, {funcionario.matricula}, {funcionario.endereco}\n")
    print("Dados salvos com sucesso.")

print("\nExibindo todos os funcionários")
try:
    # "r" - read - leitura
    with open(nome_do_arquivo, "r") as arquivo:
        # Recebe todos os dados do arquivo de uma só vez.
        lista_de_funcionarios = arquivo.readlines()
        for funcionario in lista_de_funcionarios:
            print(f"-{funcionario.strip()}")
except FileNotFoundError:
    print("O arquivo não foi encontrado.")


nome_do_arquivo = "dados_clientes.txt"
with open(nome_do_arquivo, "a", encoding="UTF-8") as arquivo_clientes:
    for cliente in lista_de_clientes:
        arquivo_clientes.write(f"{cliente.nome}, {cliente.data}, {cliente.endereco}\n")
    print("Dados salvos com sucesso.")

print("\nExibindo todos os clientes.")
try:
    with open(nome_do_arquivo, "r") as arquivo:
        lista_de_clientes = arquivo.readlines()
        for cliente in lista_de_clientes:
            print(f"-{cliente.strip()}")
except FileNotFoundError:
    print("O arquivo não foi encontrado.")