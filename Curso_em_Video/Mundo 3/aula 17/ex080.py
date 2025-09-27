lista = []
n = int(input("Adicionar valor a lista: "))
lista.append(n)
print('Adicionado ao final da lista, na posição', lista.index(n))
for c in range(4):
    n = int(input("Adicionar valor a lista: "))
    if n > max(lista):
        lista.append(n)
        print('Adicionado ao final da lista, na posição', lista.index(n))
    elif n < min(lista):
        lista.insert(0,n)
        print('Valor adicionado ao começo da lista na posição 0')
    else:
        for c in range(len(lista)):
            if  n<= lista[c]:
                lista.insert(c,n)
                print('Valor adicionado na posição ',lista.index(n))
                break
print(lista)