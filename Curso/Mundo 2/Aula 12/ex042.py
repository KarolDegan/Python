l1 = float(input('Primeiro lado: '))
l2 = float(input('Segundo lado: '))
l3 = float(input('Terceiro lado: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 <= l1 + l2:
    print('Forma Triangulo!')
    if l1 != l2 and l2 != l3 and l1 != l3:
        print('TRINAGULO ESCALENO')
    elif l1 == l2 and l1 == l3 and l2 == l3:
        print('TRINAGULO EQUILÁTERO')
    else:
        print('TRINAGULO ISÓCELES')
else:
    print('não forma triângulo')
