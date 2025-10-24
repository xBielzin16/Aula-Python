import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Usuario:
    nome: str
    idade: int
    peso: float
    altura: float


    def mostrar_dados(self):
        print(f"\nNome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Peso: {self.peso}")
        print(f"Altura: {self.altura}\n")


lista_usuarios = []


for i in range(4):
    dados_usuario = Usuario(nome=input("Digite o seu nome: "), 
                            idade=int(input("Digite a sua idade: ")), 
                            peso=float(input("Digite o seu peso: ")), 
                            altura=float(input("Digite a sua altura: ")))  
    lista_usuarios.append(dados_usuario)
    os.system("cls")

for um_usuario in lista_usuarios:
    um_usuario.mostrar_dados()