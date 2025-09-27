c = 0
soma = 0
teste = 'S'
maior = 0
menor = 0
while teste == 'S': 
    n = int(input('Digite um número:'))
    soma +=n
    c += 1
    teste = input('Deseja continuar?[S/N]').upper().strip()
    if c == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('Média: {}\nMaior: {}\nMenor: {}'.format(soma/c,maior,menor))