lista = []
for c in range(5):
    n = int(input('Valor da lista: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        cont = 0
        while cont <= len(lista):
            if n <= lista[cont]:
                lista.insert(cont,n)
                break
            cont += 1
print(lista)