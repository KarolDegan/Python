print('-=-'*30)
print('Analisador de Triangulo')
print('-=-'*30)
n1 = float(input('Primeiro Segumento'))
n2 = float(input('Segundo Segumento'))
n3 = float(input('Terceiro Segumento'))
v = 0
if n1<n2:
    n1 = v
    n1 = n2
    n2 = v
if n2<n3:
    n2 = v
    n2 = n3
    n3 = n2
if n1> n2 + n3 or n3< n2 - n1: # n1< n2+n3 and n2 < n1 + n3 and n3 < n1 + n2
    print('Não forma TRIANGULO!')
else:
    print('Forma TRIANGULO!')