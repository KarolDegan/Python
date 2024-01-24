lista = ('abacate','maça','batata','amendoim','economia','mercado','trabalho','loja','almofada','eletrodomestico','azeitona','jaca')
for p in lista:
    print(f'\nNa palavra {p} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')