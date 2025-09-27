from datetime import date
ano = int(input('Qual ano quer analisar? \n Para ano atual digite 0 \n' ))
ex = ano % 100 == 0
if ano == 0:
    ano = date.today().year
if ano % 4 == 0:
    if ano % 100 == 0 and ano % 400 != 0:
        print('{} não é BISSEXTO'.format(ano))
    else:
        print('{} é um ano BISSEXTO!'.format(ano))
else:
    print('{} não é um ano BISSEXTO!'.format(ano))
#if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0