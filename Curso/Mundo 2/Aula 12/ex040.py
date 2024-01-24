n1 = float(input('Nota 1: '))
n2= float(input('Nota 2: '))
media = (n1+n2)/2
if media < 5:
    print('REPROVADO!')
elif media >= 5 and media <= 6.9:
    print('RECUPERAÇÃO!')
else:
    print('APROVADO!')