import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Endereco:
    logradouro: str
    numero: int
    cidade: str

@dataclass
class Cliente:
    nome: str
    email: str
    endereco: Endereco

    def mostrar_dados(self):
        print(f"\nNome: {self.nome}")
        print(f"Logradouro: {self.endereco.logradouro}")
        print(f"Número: {self.endereco.numero}")
        print(f"Email: {self.email}")
        print(f"Cidade: {self.endereco.cidade}\n")

cliente1 = Cliente(nome=input("Digite o seu nome: "), 
                   email=input("Digite o seu e-mail: "), 
                   endereco=Endereco(logradouro=input("Digite o seu logradouro: "), 
                       numero=int(input("Digite o número de sua residência: ")), 
                       cidade= input("Digite a sua cidade: ")))

print("\nMostrando os dados do cliente.")
cliente1.mostrar_dados()