n = int(input('Número natural maior que 0: '))
r = n%10
n = n//10
crescente = True
while n>0 and crescente:
    if r <= n%10:
        crescente = False
    r = n%10
    n = n//10
if crescente:
    print('Dígitos em ordem crescente!')
else:
    print('Dígitos NÃO estão em ordem crescente!')
