c = input('Digite um caracter: ')
e = 0
while c != '.':
    if c!= ' ' and e > 1:
        print(' ')
    if c == ' ':
        e = 1
    else:
        print(c)
    c = input('Digite outro caracter: ')
print('Fim!')