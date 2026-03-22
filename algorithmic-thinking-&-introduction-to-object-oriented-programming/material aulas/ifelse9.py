#função e o salario
#função (ESTAGIÁRIO,PROFESSOR) 20%
#outras 10%

func = input("Função:")
sal = float(input("Salário R$:"))

if func == "ESTAG" or func == "PROF":
    sal = sal * 1.20
else:
    sal = sal * 1.10

print("Salário com aumento:",sal)  
