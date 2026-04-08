nota = float(input('Digite uma nota'))
if nota < 0:
    print('Nota inválida - NEGATIVA')
elif nota >= 0.0 and nota < 2.0:
    print('Conceito E')
elif nota >= 2.0 and nota < 5.0:
    print('Conceito D')
elif nota >= 5.0 and nota < 7.0:
    print('Conceito C')
elif nota >= 7.0 and nota < 9.0:
    print('Conceito B')
elif nota >= 9.0 and nota <= 10.0:
    print('Conceito A')
else:
    print('Nota inválida')
