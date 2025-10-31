import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Usuario:
    nome: str
    idade: str
    email: str
    telefone: str

QUANTIDADE_USUARIOS = 2
lista_de_usuarios = []

for i in range(QUANTIDADE_USUARIOS):
    usuario = Usuario(
        nome= input("Digite seu nome: "),
        idade=int(input("Digite sua idade: ")),
        email= input("Digite seu e-mail: "),
        telefone= input("Digite seu telefone: ")
    )
    lista_de_usuarios.append(usuario)

print()
print("Exibindo dados.")
arquivo = "dados_usuario.txt"

with open(arquivo, "a") as arquivo_usuario:
    for usuario in lista_de_usuarios:
        arquivo_usuario.write(f"{usuario.nome},{usuario.idade},{usuario.email},{usuario.telefone}\n")
    print("Salvo com sucesso!")