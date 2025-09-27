from utilidadesCeV import dado, moeda

p = dado.valido(('Preço R$: ').strip())
moeda.resumo(p,35,22)
