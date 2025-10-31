import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Endereco:
    logradouro: str
    numero: int

@dataclass
class Pessoa:
    nome: str
    idade: int
    endereco: Endereco

    def mostrar_dados(self):
        print(f"\nNome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Logradouro: {self.endereco.logradouro}")
        print(f"Número: {self.endereco.numero}\n")

lista_de_pessoas = []

for i in range(2):
    dados_pessoa = Pessoa(nome= input("Digite o seu nome: "), 
                          idade= int(input("Digite a sua idade: ")), 
                          endereco=Endereco(
                              logradouro= input("Digite o seu logradouro: "),
                              numero= int(input("Digite o númnero: "))
                          ))
    lista_de_pessoas.append(dados_pessoa)            
    os.system("cls")

for uma_pessoa in lista_de_pessoas:
    uma_pessoa.mostrar_dados()