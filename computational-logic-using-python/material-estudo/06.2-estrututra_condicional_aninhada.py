nota = float(input("Digite sua nota: "))
frequencia = int(input("Digite sua frequencia: "))

if nota >= 5 and frequencia >= 75:
    situação = "aprovado"
elif nota >= 5 or frequencia >= 75:
    situação = "na recuperação"
else:
    situação = "reprovado"

print (f"Você está {situação}!")
