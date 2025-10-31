import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Autor:
    nome: str
    biografia: str

@dataclass
class Livro:
    titulo: str
    ano: int
    autor: Autor

def exibir_detalhes(self):
    print("")