import ex115a
from time import sleep

while True:
    resposta = ex115a.menu(['Ver Pessoas Cadastradas', 'Cadastrar Outra Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        print('Opção 1')
    elif resposta == 2:
        print('Opção 2')
    elif resposta == 3:
        print('Saindo do sistema...Até logo!')
        break
    else:
        print('\033[0;31m Erro Valor invalido: \033[m')
    sleep(2)