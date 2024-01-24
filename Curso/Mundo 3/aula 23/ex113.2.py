def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;33m Erro! Valor invalido \033[m')
        except KeyboardInterrupt:
            print('\033[0;33m Entrada de dados interrompida pelo usuário \033[m')
            return 0
        else:
            break
    return n

def leiaReal(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;33m Erro! Valor inválido \033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;33m O usuario preferiu não digitar esse valor \033[m')
            return 0
        else:
            return n


print(leiaInt('Numero Inteiro: '))