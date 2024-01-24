def lin():
    return 40*'-'

def titulo(msg):
    print(lin())
    print(msg.center(42)).upper()
    print(lin())

def menu(lista):
    titulo('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[0;33m{c}\033[m - \033[0;34m{item}\033[m')
        c += 1
    print(lin())
    opc = erro('\033[0;32m Sua Opção: \033[m')
    return opc

def erro (msg):
    while True:
        try:
            n = int(input(msg))
        except (TypeError, ValueError):
            print('\033[0;34m Erro Valor invalido: \033[m')
            continue
        else:
            return n
