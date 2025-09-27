nome = input("Nome: ")
idade = int(input("Idade: "))
sexo = input("sexo [f]Feminino, [m]Fasculino: ")
si = 0
sf = 0
velho = idade
nomev = nome
for c in range(3):
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("sexo [f]Feminino, [m]Fasculino: ")
    si += idade
    if idade > velho:
        velho = idade
        nomev = nome
    if sexo == 'f' and idade < 20:
        sf +=1
print("Média idades: ",si/4)
print("Mais velho: ", nomev)
print("Mulheres com menos de 20 anos: ", sf)

