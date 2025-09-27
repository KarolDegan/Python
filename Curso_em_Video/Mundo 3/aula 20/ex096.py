def area(c,l):
    a = c * l
    print(f'A área de um terreno de {c}*{l} é {a}')
def mensagem(msg):
    print(40*'=')
    print(msg.upper().strip())
    print(40*'=')

mensagem('area terreno')
largura = float(input('Largura (m):'))
comprimento = float(input('Comprimento (m): '))
area(comprimento,largura)