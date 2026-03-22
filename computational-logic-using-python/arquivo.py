# Sistema de Controle de Estoque - Loja R&A Eletrônicos
# Desenvolvido para entrega da disciplina Algoritmos e Lógica Computacional
# Menu: adicionar, atualizar, excluir, visualizar, sair

# Estoque inicial da loja
estoque = {}

# --------- Funções ---------

def mostrar_menu():
    print("\n===== LOJA R&A ELETRÔNICOS - CONTROLE DE ESTOQUE =====")
    print("1 - Adicionar produto")
    print("2 - Atualizar produto")
    print("3 - Excluir produto")
    print("4 - Visualizar estoque")
    print("0 - Sair")
    print("======================================================")

def adicionar_produto():
    nome = input("\nNome do produto: ")

    if nome in estoque:
        print("Produto já existe no estoque!")
        return

    try:
        preco = float(input("Preço do produto (R$): ").replace(",", "."))
        qtd = int(input("Quantidade em estoque: "))
    except ValueError:
        print("Erro: insira valores numéricos válidos.")
        return

    estoque[nome] = {"preco": preco, "quantidade": qtd}
    print("Produto adicionado com sucesso!")

def atualizar_produto():
    nome = input("\nDigite o nome do produto a atualizar: ")

    if nome not in estoque:
        print("Produto não encontrado!")
        return

    try:
        novo_preco = float(input("Novo preço (R$): ").replace(",", "."))
        nova_qtd = int(input("Nova quantidade: "))
    except ValueError:
        print("Erro: insira valores numéricos válidos.")
        return

    estoque[nome]["preco"] = novo_preco
    estoque[nome]["quantidade"] = nova_qtd
    print("Produto atualizado com sucesso!")

def excluir_produto():
    nome = input("\nDigite o nome do produto que deseja excluir: ")

    if nome in estoque:
        del estoque[nome]
        print("Produto removido do estoque!")
    else:
        print("Produto não encontrado!")

def visualizar_estoque():
    print("\n===== ESTOQUE ATUAL =====")
    if not estoque:
        print("Não há produtos cadastrados!")
    else:
        for produto, info in estoque.items():
            print(f"\nProduto: {produto}")
            print(f"Preço: R$ {info['preco']:.2f}")
            print(f"Quantidade: {info['quantidade']} unidades")
    print("=========================")

# --------- Execução do Programa ---------

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_produto()
    elif opcao == "2":
        atualizar_produto()
    elif opcao == "3":
        excluir_produto()
    elif opcao == "4":
        visualizar_estoque()
    elif opcao == "0":
        print("Sistema encerrado. Obrigado por utilizar!")
        break
    else:
        print("Opção inválida! Tente novamente.")
