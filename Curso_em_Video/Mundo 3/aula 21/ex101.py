def voto(ano):
    idade = datetime.now().year - ano
    if idade >= 18:
        return f'Com {idade} anos o voto é Obrigatório'
    elif idade >=16:
        return f'Com {idade} anos o voto é Opcional'
    else:
        return f'Com {idade} anos não vota'


from datetime import datetime
n = int(input('Ano de nascimento: '))
print(voto(n))