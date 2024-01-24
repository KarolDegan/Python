n1 = int(input('Primeiro número'))
n2 = int(input('Segundo número: '))
if n2>n1:
    int = n1
    n1 = n2
    n2 = int
    print('maior número: ',n1)
    print('menor número: ',n2)
elif n1>n2:
    print('maior número: ',n1)
    print('menor número: ',n2)
elif n1 == n2 :
    print('Números iguais')
