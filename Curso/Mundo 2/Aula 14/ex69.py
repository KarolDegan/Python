print(30*'-')
print('CADASTROS')
print(30*'-')
cont = 0
cont2 = 0
cont3 = 0
while True:
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]").upper().strip()
    while sexo != 'M' and sexo != "F":
        sexo = input("Sexo [M/F]").upper().strip()
    e = input('Deseja continuar [S/N]: ').upper().strip()
    while e != 'S' and e!='N':
        e = input('Deseja continuar [S/N]: ').upper().strip()
    if idade > 18:
        cont +=1
    if sexo == 'M':
        cont2 += 1
    if sexo == 'F' and idade>20:
        cont3 += 1
    if e == 'N':
        break
print(f'Tem {cont} pessoas com mais de 18 anos')
print(f'Há {cont2} homens cadastrados')
print(f'Há {cont3} mulheres cadastradas com mais de 20 anos')