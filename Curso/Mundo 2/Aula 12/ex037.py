n = int(input('Número decimal: '))
e = int(input('escolha base de conversão\n[1]binário\n[2]octal\n[3]hexadecimal'))
if e == 1:
    soma = 0
    exp = 0
    r = n%2
    while n>0:
        soma = soma + r * (10**exp)
        n = n//2
        r = n%2
        exp = exp +1
    print(soma)
elif e == 2:
    soma = 0
    exp = 0
    r = n%8
    while n>0:
        soma = soma + r * (8**exp)
        n = n//2
        r = n%2
        exp = exp +1
    print(soma)
elif e == 3:
    soma = 0
    exp = 0
    r = n%8
    while n>0:
        soma = soma + r * (16**exp)
        n = n//2
        r = n%2
        exp = exp +1
    print(soma)
else:
    print('Nenhuma opção válida selecionada')