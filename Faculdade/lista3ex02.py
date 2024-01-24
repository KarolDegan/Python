n = int(input('Número natural: '))
soma = 0
for i in range (1,n+1):
    h = 1/i
    soma = soma + h
print('Harmônico de ', n, ' é ', soma)