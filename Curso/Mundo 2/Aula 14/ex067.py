print(30*'-')
print('TABUADA')
print(30*'-')
while True:
    n = int(input('Número:'))
    if n < 0:
        print('nosso programa acabou!')
        break
    cont = 1
    while cont <= 10:
        mult = n*cont
        print(f'{n} x {cont} = {mult}')
        cont += 1