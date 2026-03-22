horas_trabalhadas = float(input('Digite a quantidade de horas trabalhadas: '))
valor_hora = float(input('Digite o valor/hora: '))

if (horas_trabalhadas >= 100):
    bonus = 500.00
else:
    bonus = 0

salario = horas_trabalhadas * valor_hora + bonus

print(f"Seu salário é de {salario}")
