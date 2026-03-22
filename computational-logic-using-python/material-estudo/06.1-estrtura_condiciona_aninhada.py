anos_experiencia = int(input("Digite os ano de experiência: "))

if anos_experiencia == 0:
    nivel = "estagiário"
elif anos_experiencia <= 3:
    nivel = "júnior"
elif anos_experiencia <= 8:
    nivel = "Pleno"
else:
    nivel = "sênior"

print (f"Você é um desenvolvedor no nível {nivel}")
