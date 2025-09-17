import os
os.system("cls")


login_correto = "biel"
senha_correta = "2805"

while True:
    for i in range(3):
        print(f"\nTentativa: {i+1}")
        login = input("Digite seu login: ")
        senha = input("Digite sua senha: ")

        if login == login_correto and senha == senha_correta:
            print("Acesso permitido.")
            break
        else:
            print("Login ou senha incorretos. Tente novamente. \n")
    break