jogador = {}
tot = 0
jogador['nome'] = input('Nome: ')
partidas = int(input('Quantas partidas jogou?'))
for c in range(partidas):
    jogador[c+1] = int(input(f'Quantos gols na {c+1}ª partida? '))
print(40*'=-')
print(jogador)
print(40*'=-')
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print(40*'=-')
print(f'O jogador{jogador["nome"]} jogou {partidas} partidas')
for c in range(1,len(jogador)):
    print(f'Na partida {c}, fez {jogador[c]} gols')
    tot += jogador[c]
print(f'fez um total de {tot} gols')