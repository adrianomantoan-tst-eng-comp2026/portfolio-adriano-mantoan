# Manipulando tuplas - tuple

cores = ("vermelha", "azul", "amarelo", "verde")
print(f"Meu carro é {cores[2]}")

qtd = len(cores)
print(f"Tenho {qtd} de opções de cores")

cores = input("Digite uma cor: ")
qtd_cores = cores.count(cores)
print(f"Temos {qtd_cores} tipo de {cores}")

if cores in cores:
    print(f"A cor {cores} existe na loja")
else:
    print(f"A cor {cores} não existe na loja")