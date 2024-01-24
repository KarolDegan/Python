n = int(input("Número fatorial: "))
soma = 0
aux = 1
junto = ''
for c in range(n,0,-1):
    aux = aux * c
    junto += str(c) + 'x'
print(n,'! = ', junto, ' = ', aux)