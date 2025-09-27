n = int(input('Digite um número Inteiro positivo'))
r = n % 2
if r == 1:
    print('{} é IMPAR'.format(n))
else:
    print('{} é PAR!'.format(n))