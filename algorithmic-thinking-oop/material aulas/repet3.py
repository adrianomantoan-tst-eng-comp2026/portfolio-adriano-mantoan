print("--- Menu ---")
print("1. Ação 1")
print("2. Ação 2")
print("3. Ação 3")
print("4. Sair")
while True:
    print("\n")
    op = int(input("Entre com a sua opção:"))
    if op == 1:
        print("Rotina 1")
    elif op == 2:
        print("Rotina 2")
    elif op == 3:
        print("Rotina 3")
    elif op == 4:
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")
