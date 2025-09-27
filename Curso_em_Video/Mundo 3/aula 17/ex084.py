lista = []
dados = []
maior = 0
menor = 0
while True:
    dados.append(input('Nome: '))
    dados.append(input('Peso: '))
    print(30*'=')
    if len(lista) == 0:
        maior = dados[1]
        menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
            print(maior)
        if dados[1] < menor:
            menor = dados[1]
            print(menor)
    lista.append(dados[:])
    dados.clear()
    e = input('Deseja continuar[S/N]').upper().strip()[0]
    while e!='N' and e !='S':
        e = input('Deseja continuar[S/N]').upper().strip()[0]
    if e == 'N':
        break
print(30*'-=')
print('Número de pessoas: ', len(lista))
print(f'Pessoas mais pesadas {maior}: ', end=' ')
for c in lista:
    if c[1] == maior:
        print(c[0], end='')
print(f'\nPessoas mais leves {menor}', end=' ')
for c in lista:
    if c[1] == menor:
        print(c[0], end=' ')