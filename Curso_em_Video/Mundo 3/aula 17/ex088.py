from random import randint
import time
jogo = []
n = int(input('Número de jogos: '))
for c in range(n):
    for numero in range(6):
        comp = [randint(1,60)]
        while comp in jogo:
            comp = [randint(1,60)]
        jogo.append(comp)
    jogo.sort()
    print(f'Jogo{c+1}: {jogo}')
    jogo.clear()
    time.sleep(1)