def aumentar(p, a, format=False):
    p = p + p*a/100
    return p if format is False else moeda(p)

def diminuir(p, b, format = False):
    p = p - p*b/100
    return p if format is False else moeda(p)

def dobro(p, format = False):
    p = 2*p
    return p if not format else moeda(p)

def metade(p, format = False):
    p = p/2
    return p if not format else moeda(p)

def moeda(mo):
    f = f'R$: {mo:.2f}'.replace('.',',')
    return f

def resumo(res, au, di):
    print(40*'-')
    print('RESUMO DO VALOR'.center(40))
    print(40*'-')
    print(f'Preço analisado: \t{moeda(res)}')
    print(f'Dobro do preço: \t{dobro(res,True)}')
    print(f'Metade do preço: \t{metade(res,True)}')
    print(f'{au}% de aumento: \t{aumentar(res, au, True)}')
    print(f'{di}% de redução: \t{diminuir(res, di, True)}')