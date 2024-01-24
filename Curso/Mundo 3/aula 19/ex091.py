from random import randint
dado = {}
rank = {}
cont = 0
from operator import itemgetter
for c in range(4):
    comp = randint(1,6)
    print(f'O jogador {c+1} tirou {comp}')
    dado[c+1] = comp
rank = sorted(dado.items(), key=itemgetter(1), reverse = True)
for k, v in rank:
    cont+=1
    print(f'{cont}º O jogador{k} tirou {v}')