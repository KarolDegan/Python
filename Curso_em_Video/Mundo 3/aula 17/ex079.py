lista = []
while True:
    n = int(input('Número para adicionar a lista: '))
    if n in lista:
        print("Valor já adicionado")
    else:
        lista.append(n)
        print('valor adicionado com sucesso!')
    e = input('Deseja adicionar outro valor a lista [S/N]: ').upper().strip()[0]
    while e != 'S' and e != 'N':
        e = input('Deseja adicionar outro valor a lista [S/N]: ').upper().strip()[0]
    if e == 'N':
        break
lista.sort()
print(f'Valores da lista {lista}')