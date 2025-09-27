cont = 0
soma = 0
while True:
    n = int(input("numero inteiro: "))
    if n == 999:
        break
    cont +=1
    soma += n
print(f'foram lidos {cont} numeros')
print(f'a soma dos numeros é {soma}')