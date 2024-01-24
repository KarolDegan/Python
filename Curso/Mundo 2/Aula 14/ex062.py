i = int(input("Primeiro termo PA: "))
r = int(input("Razão: "))
c = 1
s = i
while c <= 10:
    c +=1
    print(s)
    s += r
e = input("Deseja ler mais termos [S/N]").upper().strip()
while e == 'S':
    a = int(input("Mais quantos termos: "))
    c = 1
    while c <= a:
        c +=1
        print(s)
        s += r
    e = input("Deseja ler mais termos [S/N]").upper().strip()