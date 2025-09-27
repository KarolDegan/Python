from datetime import date
ano = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - ano
if idade < 17:
    print('Ainda vai se alistar')
    x = 17 - idade 
    y = x + atual
    print('Vai se alistar daqui a {} anos, no ano de {}'.format(x,y))
elif idade >= 17 and idade <=18:
    print('Hora de se alistar')
else:
    x = idade - 18
    print('Passou do tempo de se alistar')
    print('Você deveria ter se alistado em ',x)