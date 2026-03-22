valores = [100, 30, 45, 33, 99]

def mensagem():
    print("Olá mundo!")

def calcular_desconto(preco):
    return preco * 0.8

def soma(a, b):
    return a + b


mensagem()

valor_pagar = calcular_desconto(100)
print(f"Valor com desconto: R$ {valor_pagar:.2f}")

total = soma(4, 90)
print(f"Soma total: {total}")

print("\n### Valores com desconto ###")
for valor in valores:
    valor_desconto = calcular_desconto(valor)
    print(f"Original: R$ {valor:.2f} | Com desconto: R$ {valor_desconto:.2f}")
