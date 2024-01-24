teste = 0
s = 0
for c in range (7):
    ano = int(input("Ano de nascimento: "))
    teste = 2023 - ano
    if teste < 18:
        s += 1
print(s, " pessoas não são maiores de idade")
print (7-s, " são maiores de idade")