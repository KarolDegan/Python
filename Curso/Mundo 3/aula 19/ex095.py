dados = {}
principal = []
partidas = 0
while True:
    total = 0
    dados['nome'] = input('Nome: ')
    partidas = int(input('Quantas partidas: '))
    for c in range(partidas):
        dados['gols'][c+1] = int(input(f'Quantos gols na {c+1}ª partida: '))
        total += dados['gols'][c+1]
    dados['total'] = total
    principal.append(dados.copy())
    
    dados.clear()
    e = input('Deseja continuar[S/N]').upper().strip()[0]
    while e != 'S' and e != 'N':
        e = input('Deseja continuar[S/N]').upper().strip()[0]
    if e == 'N':
        break
print(principal)
print(f'{"cod nome":<9}{"Gols":<9}{"Total":<9}')
#for c in range(len(principal)):
#    print(c, principal[c]['nome'],'   ',principal[c][1:len(principal[c])], principal[c]['total'])