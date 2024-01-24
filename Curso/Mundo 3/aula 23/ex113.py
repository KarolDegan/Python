def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = input(msg)
        if n.isnumeric():
            n = int(n)
            valor = n
            ok = True
        else:
            print('Erro! Valor invalido')
        if ok:
            break
    return valor

def leiaReal(msg):
    ok = False
    valor = 0
    while True:
        n = input(msg)
        if n.isalpha():
            print('Erro! Valor invalido')
        else:
            n = float(n)
            valor = n
            ok = True
        if ok:
            break
    return valor

print(leiaInt('Valor Inteiro: '))
print(leiaReal('Valor Real: '))
