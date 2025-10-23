import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Pessoa:
    nome: str
    email: str
    telefone: str
    endereco: str

    def mostrar_dados(self):
        
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
        print(f"Telefone: {self.telefone}")
        print(f"Endereço: {self.endereco}")


print("Solicitando os dados da pessoa.")
pessoa1 = Pessoa(nome=input("Digite seu nome: "),
                 email=input("Digite seu email: "), 
                 telefone=input("Digite seu telefone: "),
                 endereco=input("Digite seu endereço: "))


print("\n= Exibindo dados da Pessoa. =")
pessoa1.mostrar_dados()