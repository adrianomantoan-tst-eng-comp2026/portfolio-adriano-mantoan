#EXERCÍCIO: Carrinho de Compras
#IN (Nome produto / Preco unitário)
#OUT (Total de itens / Valor da compra /
#Subtotal da compra) 
#Laço indefinido (continua com "s")
cont = 0
soma = 0.0
c = 's'
while c == 's':
    prod = input('Produto:')
    preco = float(input('Preço R$:'))
    cont = cont + 1
    soma = soma + preco
    print('Subtotal R$',round(soma,2))
    c = input('Deseja continuar? <s>')
print('Total de itens:',cont)
print('Valor da compra R$:',round(soma,2))








