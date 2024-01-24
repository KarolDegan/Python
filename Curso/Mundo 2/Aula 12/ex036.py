print('-'*30)
print('EMPRESTIMO BANCÁRIO')
print('-'*30)
casa = float(input('Qual o valor da casa: '))
salario = float(input('Qual o seu salário: '))
tempo = int(input('em quantos anos pretende pagar: '))
tempo = tempo *12
x = casa/tempo
max = salario * 0.3
if x >= max:
    print('Emprentimo NEGADO')
else:
    print('Emprestimo APROVADO!\nA parcela será de {:.2f} por mês'.format(x))