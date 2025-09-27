def maior(*num):
    print(40*'=')
    for c in num:
        print(f'{c}..', end = '', flush =True )
        sleep(0.3)
    print(len(num))
    print(max(num))
    print(40*'=')


from time import sleep
maior(2,7,4,9)
maior(5,3,7,2,1)
maior(0)
maior(1,2)