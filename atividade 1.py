import os
os.system ("cls")

login_cadastrado = "bielzinofc"
senha_cadastrada = "biel2805"


login = (input("Digite seu login: "))
senha = (input("Digite sua senha: "))

if login == login_cadastrado and senha == senha_cadastrada:
     print("Bem-vindo!")
else:
     print("Login ou senha inválidos.")
