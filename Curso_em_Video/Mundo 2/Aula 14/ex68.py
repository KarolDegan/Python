from random import randint
print(30*'-')
print('VAMOS JOGAR PAR OU IMPAR!')
print(30*'-')
soma = 0
cont = 0
while True:
    comp = randint(0,10)
    n = int(input('número de 0 a 10: '))
    if n > 10 or n < 0:
        n = int(input('número de 0 a 10: '))
    pi = input('Quer jogar Par[P] ou impar[I]').upper().strip()[0]
    soma = comp + n
    if pi == 'P':
        if soma%2 == 0:
            cont += 1
            print('PAR')
            print(f"você VENCEU o cumputador digitou {comp}, e você {n} dando {soma}")
        else:
            print('IMPAR')
            break
    else:
        if soma%2 != 0:
            cont += 1
            print('IMPAR')
            print(f"você VENCEU o cumputador digitou {comp}, e você {n} dando {soma}")
        else:
            print('PAR')
            break
    print("Vamos mais uma: ")
print(f"você PERDEU o cumputador jogou {comp}, e você {n} dando {soma}")
print(f'foram {cont} vitórias consecutivas!')
