peso = float(input('Entre com seu peso:'))
altura = float(input('Entre com a altura em mt:'))
imc = peso / (altura**2)
print('IMC = ',round(imc,2))
if imc < 18.5:
    situacao = 'Abaixo do peso'
elif imc >= 18.5 and imc < 25:
    situacao = 'Peso normal'
elif imc >= 25 and imc < 30:
    situacao = 'Sobrepeso'
elif imc >= 30 and imc < 35:
    situacao = 'Obesidade Grau 1'
elif imc >= 35 and imc < 40:
    situacao = 'Obesidade Grau 2'
else:
    situacao = 'Obesidade Grau 3'
print(situacao)
