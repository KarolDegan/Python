boletim = []
dados = []
media = 0
while True:
    dados.append(input('Nome: ').upper())
    dados.append(int(input('Nota1: ')))
    dados.append(int(input('Nota2: ')))
    media = (dados[1] + dados[2])/2
    dados.append(media)
    boletim.append(dados[:])
    dados.clear()
    e = input('Deseja continuar[S/N]: ').upper().strip()[0]
    while e != 'S' and e!='N':
        e = input('Deseja continuar[S/N]: ').upper().strip()[0]
    if e == 'N':
        break
print(boletim)
print(40*'=')
print(f'{"Nº":<9},{"NOME":<9},{"MEDIA":<9}')
print(40*'=')
for c in range(len(boletim)):
        print(f'{c:<9},{boletim[c][0]:<9},{boletim[c][3]:<9}')
while True:
    m = int(input('Mostrar notas de qual aluno [999 para sair!] '))
    if m == 999:
        break
    print(f'Nota {boletim[m][0]} são {boletim[m][1:3]}')
    