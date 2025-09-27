def valido(a):
    ok = False
    valor = 0
    while True:
        n = input(a).replace(',','.')
        if n.isalpha():
            print(f'\033[0;31m Erro! {n} Valor invalido! \033[m')
        else:
            valor = float(n)
            ok = True
        if ok:
            break
    return valor