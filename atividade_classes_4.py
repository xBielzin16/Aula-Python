import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Pessoa:
    nome: str
    email: str
    endereco: str

    def mostrar_dados(self):
        print("\n= Dados da pessoa =")
        print(f"Nome: {self.nome}")
        print(f"Endereço: {self.endereco}")
        print(f"Email: {self.email}")

    def mostrar_somente_nome(self):
        print("\n= Nome da pessoa =")
        print(f"Nome: {self.nome}")


print("Solicitando os dados da pessoa.")
pessoa1 = Pessoa(nome=input("Digite seu nome: "), 
                 email=input("Digite seu e-mail: "), 
                 endereco=input("Digite seu endereço: ")) 

pessoa2 = Pessoa(nome=input("Digite seu nome: "), 
                 email=input("Digite seu e-mail: "),
                 endereco=input("Digite seu endereço: "))


print("\n= Exibindo dados. =")
pessoa1.mostrar_dados()
pessoa1.mostrar_somente_nome()
pessoa2.mostrar_dados()
pessoa2.mostrar_somente_nome()