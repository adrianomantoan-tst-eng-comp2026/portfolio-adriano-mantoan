nome = input('Entre com o nome:')
disc = input('Entre com a disciplina:')
nota1 = float(input('Entre com a nota1:'))
nota2 = float(input('Entre com a nota2:'))
faltas = int(input('Entre com a qtde de faltas:'))

media = (nota1+nota2)/2
print('Media:',media)

if media >=6 and faltas <=15:
    print('APROVADO')
else:
    print('REPROVADO')

