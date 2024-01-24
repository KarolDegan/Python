def fatorial(num, show=False):
    r = 1
    for c in range(num,0,-1):
        r = r * c
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end ='')
            else:
                print('= ', end ='')
    print(r)

n = int(input('Fatorial: '))
fatorial(n,show=False)