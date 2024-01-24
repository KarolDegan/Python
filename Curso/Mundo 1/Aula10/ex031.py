d = float(input('Qual a distância da viagem?'))
p = 0
if d<= 200:
    p = d*0.5
    print('O preço da viagem é {}R$'.format(p))
else:
    p = d*0.45
    print('O preço da viagem é {}R$'.format(p))