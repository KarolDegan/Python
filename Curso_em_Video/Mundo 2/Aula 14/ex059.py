soma = 0
mult = 0
n1 = float(input("Primeiro valor: "))
n2 = float(input("Segundo valor: "))
print(30*'-')
print('MENU')
e= int(input('[1] somar \n[2] multiplicar\n[3] maior \n[4] novos números \n[5] sair do programa'))
print(30*'-')
while e != 5:
    if e == 1:
        soma = n1 + n2
        print(soma)
    elif e == 2:
        mult = n1 * n2
        print(mult)
    elif e == 3:
        if n2 > n1:
            aux = n1
            n1 = n2
            n2 = aux
        print(n1)
    else:
        n1 = float(input("Primeiro valor: "))
        n2 = float(input("Segundo valor: "))
    print(30*'-')
    print('MENU')
    e= int(input('[1] somar \n[2] multiplicar\n[3] maior \n[4] novos números \n[5] sair do programa'))
    print(30*'-')