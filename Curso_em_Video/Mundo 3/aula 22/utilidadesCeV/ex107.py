import moeda

preço = float(input("Preço: "))
print(f'A metade de R${preço:.2f} é R${moeda.metade(preço):.2f}')
print(f'O dobro de {moeda.moeda(preço)} é {moeda.moeda(moeda.dobro(preço))}')
print(f'Acrescentando 10% temos: {moeda.aumentar(preço,10,True)}')
print(f'Reduzindo 13% temos: {(moeda.diminuir(preço, 13,True))}')