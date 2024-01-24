n = int(input('Entre com um número: '))
cont = 0
soma = 0
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um número'))
print('Quantidade de números digitados: {}\nsoma: {}'.format(cont,soma))