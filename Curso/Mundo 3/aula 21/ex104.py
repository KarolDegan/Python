def leiaInt(a):
    ok = False
    valor = 0
    while True:
        n = str(input(a))
        if n.isnumeric():
            valor = n
            ok = True
        else:
            print('\033[0;31m Erro! Digite um número inteiro \033[0;30m')
        if ok:
            break
    return valor

n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')