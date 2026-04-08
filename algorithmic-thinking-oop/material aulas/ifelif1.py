cargo = str(input('Cargo:'))
salario = float(input('Salário R$'))
if cargo == 'GER':
    aumento = 0.10
elif cargo == 'ENG':
    aumento = 0.20
elif cargo == 'TEC':
    aumento = 0.30
else:
    aumento = 0.40
print('Salario antigo R$',salario)
novosal = salario + salario * aumento
print('Novo salario R$',novosal)
print('Diferença R$',novosal-salario)
    
