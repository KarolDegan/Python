def sub (a, b, c, n):
    for i in range (0,n):
        d = a[i]-b[i]
        c.append(d)
    print(c)

lista1 = [2,4,5]
lista2 = [4,1,3]
lista3 = []
sub(lista1,lista2,lista3,3)