n = int(input('Digite um número natural: '))
i = 1
x = i * (i+1) * (i+2)
while x < n:
    i = i + 1
    x = i * (i+1) * (i+2)
if x == n:
    print('Forma Triangulo!')
else:
    print('Não Forma Triangulo!')