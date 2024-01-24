matriz = [[0,0,0],[0,0,0],[0,0,0]]
for c in range(3):
    for j in range(3):
        matriz[c][j] = int(input(f'Numero na posição {c} x {j}: '))
for c in range(3):
    for j in range(3):
        print(f'[{matriz[c][j]:^5}]', end='')
    print('\n')