s = int(input('Quantos números na sequência: '))
n = int(input('Número inteiro: '))
cont = 1
maior = 0
for i in range(2,s+1):
    teste = n
    n = int(input('Número inteiro: '))
    if n == teste:
        cont += 1
    else:
        if cont > maior:
            maior = cont
        cont = 1
if cont > maior:
    maior = cont
print('Maior número da sequência: ', maior)
