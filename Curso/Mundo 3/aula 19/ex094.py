dado = {}
principal = []
mulheres = []
cont = 0
totid = 0
while True:
    cont += 1
    dado['nome'] = input('Nome: ')
   
    dado['sexo'] = input('Sexo[M/F]').upper().strip()[0]
    while dado['sexo'] != 'M' and dado['sexo'] != 'F':
        dado['sexo'] = input('Sexo[M/F]').upper().strip()[0]
    if dado['sexo'] == 'F':
        mulheres.append(dado['nome'])
    
    dado['idade'] = int(input('Idade: '))
    totid += dado['idade']
    
    principal.append(dado.copy())
    dado.clear()
    
    e = input('Deseja continuar [S/N]').upper().strip()[0]
    while e != 'S' and e!= "N":
        e = input('Deseja continuar [S/N]').upper().strip()[0]
    if e == 'N':
        break

print(f'A) Ao todo temos {cont} pessoas cadastradas')
print(f'B) A média das idades é {totid/cont}')
print(f'C) AS mulheres cadastradas foram: {mulheres}')
print(f'D) lista de pessoas que estão acima da média: ')
for c in principal:
    if c['idade'] > totid/cont:
        for k, v in c.items():
            print(f'{k} = {v}', end=' ')
        print('')
print('<<<<<ENCERRADO>>>>>>')