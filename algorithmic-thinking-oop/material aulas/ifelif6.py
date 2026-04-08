n1 = float(input('Entre com N1:'))
# +  -  x   /   ^
op = str(input('Entre com o operador + - x / ^ :'))
n2 = float(input('Entre com N2:'))
if op == '+':
    print(n1+n2)
elif op == '-':
    print(n1-n2)
elif op == 'x':
    print(n1*n2)
elif op == '/' and n2 != 0: 
    print(n1/n2)
elif op == '/' and n2 == 0:
    print('Divisão por ZERO')
elif op == '^':
    print(n1**n2)
else:
    print('Operador inválido')
    

