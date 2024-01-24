def contador(inicio,fim,passo):
    print(f'Início: {inicio}, Fim: {fim}, Passo: {passo}')
    
    for c in range(inicio,fim,passo):
        print(f'{c} ', end='')
        
    print()

from time import sleep
contador(1,10,1)
contador(10,0,-2)
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
if i < f:
    if p == 0:
        p = 1
    if p < 0:
        p = - p
if i > f:
    if p > 0:
        p = -p
    if p == 0:
        p = 1
contador(i,f,p)