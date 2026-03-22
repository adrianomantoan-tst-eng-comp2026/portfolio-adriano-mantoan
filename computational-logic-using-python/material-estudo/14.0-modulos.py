import random
import operacoes
from colorama import Fore, init
init(autoreset=True)

def exibir_menu():
    print("### Menu de Operações ###")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Número aleatório")
    print("0. Sair")

def obter_numeros():
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    return [a, b]

while True:
    exibir_menu()

    opcao = input("Escolha uma opcao: ")
    if (opcao == "0"):
        print("Saindo do sistema!")
        break

    if (opcao == "1"):
        a, b = obter_numeros()
        resultado = operacoes.soma(a, b)
        print(f"Resultado da soma: {resultado}")
    elif (opcao == "2"):
        a, b = obter_numeros()
        resultado = operacoes.subtracao(a, b)
        print(f"Resultado da subtração: {resultado}")
    elif (opcao == "3"):
        a, b = obter_numeros()
        resultado = operacoes.multiplicacao(a, b)
        print(f"Resultado da multiplicação: {resultado}")
    elif (opcao == "4"):
        a, b = obter_numeros()
        if b != 0:
            resultado = operacoes.divisao(a, b)
            print(f"Resultado da divisão: {resultado}")
        else:
            print("Erro: Divisão por zero não é permitida.")
    elif (opcao == "5"):
        a, b = obter_numeros()
        resultado = random.numero(a, b)
        print(f"Resultado do número aleatório: {resultado}")

    else:
        print(f"{Fore.RED}"Opção inválida. Tente novamente.")