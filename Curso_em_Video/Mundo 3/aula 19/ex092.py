from datetime import datetime
dado = {}
dado['nome'] = input('Nome: ')
ano = int(input('data de nascimento: '))
dado['idade'] = datetime.now().year - ano
dado['trabalho'] = int(input('Carteira de trabalho (0 se não tiver): '))
if dado['trabalho'] != 0:
    dado['contratação'] = int(input('Ano de contratação: '))
    dado['salario'] = float(input('Salário'))
    dado['aposentadoria'] = (dado['contratação'] + 35) - ano
for k, v in dado.items():
    print(f'{k} tem valor {v}')