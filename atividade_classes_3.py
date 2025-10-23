import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Pessoa:
    nome: str
    email: str
    endereco: str

    def dados_entrega(self):
        print("\n= Dados de entrega =")
        print(f"Nome: {self.nome}")
        print(f"Endereço: {self.endereco}")

    def dados_email_marketing(self):
        print("\n= Dados de e-mail e marketing =")
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")

print("Solicitando os dados da pessoa.")
pessoa1 = Pessoa(nome=input("Digite seu nome: "), 
                 email=input("Digite seu e-mail: "), 
                 endereco=input("Digite seu endereço: ")) 

print("\n= Exibindo dados. =")
pessoa1.dados_entrega()
pessoa1.dados_email_marketing()