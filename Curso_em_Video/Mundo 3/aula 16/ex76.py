lista = ('maça','2,00','abacate','3,00','ameixa','2,50','torta','5,00')
print(40*'-')
print('LISTAGEM DE PREÇOS')
print(40*'-')
for c in range(0,len(lista), 2):
    print(f'{lista[c]:.<30} R$  {lista[c+1]}')