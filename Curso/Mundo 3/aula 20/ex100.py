def sorteia(n):
    for c in range(5):
        n.append(randint(0,90))
    print(f'Números sorteados: {n}')
def somapar(x):
    s = 0
    for c in range(len(x)):
        if x[c]%2 == 0:
            s+= x[c]
    print(f'A soma dos numeros pares: {s}')


from random import randint
numeros =[]
sorteia(numeros)
somapar(numeros)