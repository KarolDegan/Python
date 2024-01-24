sexo = input("Qual o sexo [M/F]: ").upper().strip()
while sexo != 'M' and sexo != 'F':
    print('Valor incorreto!')
    sexo = input("Qual o sexo [M/F]").upper().strip()