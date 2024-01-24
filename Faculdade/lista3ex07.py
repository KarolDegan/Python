n1 = int(input('Primeiro número inteiro positivo: '))
n2 = int(input('Segundo número inteiro positivo: '))
n3 = int(input('Terceiro número inteiro positivo: '))
if n2> n1:
    troca = n1
    n1 = n2
    n2 = troca
if n3> n1:
    troca = n1
    n1 = n3
    n3 = troca
x = n1**2
y = n2**2 + n3**2
if x == y:
    print('Triangulo Retângulo')
else:
    print('Não forma triangulo retangulo')