matriz = [[0,0,0],[0,0,0],[0,0,0]]
somapar = 0
soma3 = 0
maior2 = 0
for c in range(3):
    for j in range(3):
        matriz[c][j] = int(input(f'Numero para a posição {c} x {j}: '))
for c in range(3):
    for j in range(3):
        print(f'[{matriz[c][j]:^5}]', end ='')
        if matriz[c][j]%2 == 0:
            somapar += matriz[c][j]
        if j == 2:
            soma3 += matriz[c][j]
        if c == 1 and j == 0:
            maior2 = matriz[1][0]
        else:
            if matriz[1][j]> maior2:
                maior2 = matriz[1][j]
    print('')
print('Soma dos pares: ', somapar)
print('Soma coluna 3', soma3)
print('Maior da linha 2: ', maior2)
