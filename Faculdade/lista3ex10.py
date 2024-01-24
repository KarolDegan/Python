n = int(input('Número em binário: '))
soma = 0
exp = 0
while n>0:
    r = n%10
    x = r*(2**exp)
    soma += x
    n = n//10
    exp += 1
print(soma)
