import os
from dataclasses import dataclass
os.system("cls")

@dataclass
class Pessoa:
    nome: str
    idade: int
    peso: float
    altura: float

print("Solicitando os dados da pessoa.")
pessoa1 = Pessoa(nome=input("Digite seu nome: "), 
                 idade=int(input("Digite sua idade: ")), 
                 peso= float(input("Digite seu peso: ")), 
                 altura= float(input("Digite sua altura: ")))


print("\n= Exibindo dados da Pessoa. =")
print(f"Idade: {pessoa1.idade} anos.")
print(f"Peso: {pessoa1.peso} Kg.")
print(f"Altura: {pessoa1.altura} m.")
