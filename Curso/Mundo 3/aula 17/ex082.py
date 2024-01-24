lista = []
par = []
impar = []
while True:
    n = int(input('Valor para lista: '))
    lista.append(n)
    e = input('Adicionar valor[S/N]: ').upper().strip()[0]
    while e != 'S' and e != 'N':
        e = input('Adicionar valor[S/N]: ').upper().strip()[0]
    if e == 'N':
        break
for c in range(len(lista)):
    if lista[c]%2 == 0:
        par.append(lista[c])
    else:
        impar.append(lista[c])
print(lista)
print('Par: ', par)
print('Impar: ', impar)