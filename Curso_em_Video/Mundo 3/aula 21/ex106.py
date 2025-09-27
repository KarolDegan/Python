def pesquisa(com):
    help(com)
def cabeçalho(d):
    print(50*'\033[0;30;40m ~')
    print(f'Acessando manual do comando {d}')
    print(50*'~\033[0;30 m')

while True:
    def cabeçalho():
    print('\033[0;33;42m ~ '*50)
    print('SISREMA DE AJUDA PyHELP')
    print(50*'~\033[0;30;40 m')
    duv = input('Função ou Biblioteca')
    if duv.upper() == 'FIM':
        break
    else:
        pesquisa(duv)
    cabeçalho(duv)

