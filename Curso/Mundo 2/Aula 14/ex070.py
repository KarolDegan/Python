print(30*'-')
print('SUPER MERCADO')
print(30*'-')
tot = 0
cont = 0
barato = ''
menor = 0
pont = 1
preco = 0
while True:
    print(30*'-')
    nome = input('Nome do produto: ')
    preco = int(input('Preço R$: '))
    print(30*'-')
    tot = tot + preco
    if preco > 1000:
        cont += 1
    if pont == 1:
        menor = preco
        barato = nome
    else:
        if preco < menor:
            barato = nome
    e = input("Deseja continuar [S/N]: ").upper().strip()
    while e != 'S' and e != 'N':
        e = input("Deseja continuar [S/N]: ").upper().strip()
    if e == 'N':
        break
    pont +=1
print(30*'-')
print(f'Total gasto: {tot}')
print(f'Produtos > 1000: {cont}')
print(f'Produto mais barato: {barato}')