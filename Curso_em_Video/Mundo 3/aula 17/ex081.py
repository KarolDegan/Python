lista = []
while True:
    n = int(input('número para lista: '))
    lista.append(n)
    e = input('Inserir outro valor[S/N]: ').upper().strip()[0]
    if e == 'N':
        break
print('Quantidade de números digitados: ', len(lista))
lista.sort(reverse = True)
print('Lista em ordem decrescente: ', lista)
if 5 in lista:
    print('Valor 5 está na lista')
else:
    print('Valor 5 não está na lista')