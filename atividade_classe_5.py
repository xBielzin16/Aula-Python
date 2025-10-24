import os
from dataclasses import dataclass

os.system("cls")

# Criando uma classe.
@dataclass
class Pessoa:
    nome: str
    cpf: str
    telefone: str

    # Função apenas desta classe.
    def mostrar_dados(self):
        print("\n = Exibindo os dados da pessoa. =")
        print(f"\nNome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Telefone: {self.telefone}\n")

    def dados_sms_marketing(self):
        print("\n Exibindo apenas o telefone da pessoa.")
        print(f"Telefone:{self.telefone}")

# Vetor
lista_de_pessoas = []

for i in range(3):
    dados_pessoa = Pessoa(nome=input("Digite seu nome: "), 
                 cpf=input("Digite seu CPF: "), 
                 telefone=input("Digite seu telefone: "))
    lista_de_pessoas.append(dados_pessoa)
    os.system("cls")

# Mostrando dados da pessoa.
print("Mostrando os dados da pessoa.")
for uma_pessoa in lista_de_pessoas:
    uma_pessoa.mostrar_dados()

print("Mostrando o telefone da pessoa.")
for uma_pessoa in lista_de_pessoas:
    uma_pessoa.dados_sms_marketing()