senha = input("Digite sua senha: ")
senha_correta = "123"

while senha != senha_correta:
    print("Senha incorreta! Tente novamente")
    senha = input("Digite sua senha: ")

print ("Acesso permitido!")