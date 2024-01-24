lista = [[],[]]
par = []
inpar = []
for c in range(7):
    n = int(input('numero: '))
    if n%2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
lista[1].sort()
lista[0].sort()
print(lista)