from random import randint
computador = randint(0,5)
n = int(input('Qual número de zero a 5 eu estou pensando?'))
if computador == n:
    print('Parabens! Pensamos no número {}'.format(computador))
else:
    print('Errouuuu! Penei no número {}, não no {}'.format(computador,n))