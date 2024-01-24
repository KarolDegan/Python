x = int(input('entre:'))
sinal = 1
soma = 0
for i in range (1,x+1):
    x = sinal * 1/i
    soma = soma + x
    sinal = - sinal
print(soma)