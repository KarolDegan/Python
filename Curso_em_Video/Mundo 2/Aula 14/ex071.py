print(30*'-')
print('CAIXA ELETRÔNICO!')
print(30*'-')
valor = int(input('Valor a ser sacado R$: '))
n50 = valor//50
valor = valor%50
n20 = valor//20
valor = valor%20
n10 = valor//10
valor = valor%10
n1 = valor//1
print(30*'-')
print(f'Total de {n50} cédulas de R$ 50')
print(f'Total de {n20} cédulas de R$ 20')
print(f'Total de {n10} cédulas de R$ 10')
print(f'Total de {n1} cédulas de R$ 1')
print(30*'-')