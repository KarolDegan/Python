a = {}
a['nome'] = input('Nome: ')
a['media'] = float(input('Média: '))
if a['media'] >= 6:
    a['situação'] = 'Aprovado'
else:
    a['situação'] = 'Reprovado'
for k, v in a.items():
    print(f'{k}: {v}')