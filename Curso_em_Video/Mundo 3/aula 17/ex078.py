lista = []
for c in range(5):
    n = int(input('Número: '))
    lista.append(n)
maior = []
menor = []
for c in range(len(lista)):
    if lista[c] == max(lista):
        maior.append(c)
for c in range(len(lista)):
    if lista[c] == min(lista):
        menor.append(c)
if len(maior) == 1:
    print('Maior: ',max(lista),'na posição',maior)
else:
    print('Maior: ',max(lista),'nas posições',maior)
if len(menor) ==1:
    print('Menor: ', min(lista),'na posição',menor)
else:
    print('Menor: ', min(lista),'nas posições',menor)