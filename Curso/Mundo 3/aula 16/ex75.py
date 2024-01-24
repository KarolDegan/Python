n = (int(input('Número: ')),int(input('Número: ')),int(input('Número: ')),int(input('Número: ')))
if 9 in n:
    print(f'O valor "9" apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O valor "3" foi digitado na posição: {n.index(3)}')
else:
    print('O número 3 não foi encontrado em nenhuma posição')
print('Os números pares foram: ', end='')
for c in n:
    if c%2==0:
        print(c, end=' ')