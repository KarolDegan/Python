def ficha(nome = '<<Desconehcido>>',gols = 0):
    print(f'O jogador {nome} fez {gols} gols')


n = input('Nome do jogador: ')
g = input('Quantidade de Gols: ')
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols = g)
else:
    ficha(n,g)