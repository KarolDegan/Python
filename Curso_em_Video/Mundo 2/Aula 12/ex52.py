numero = int(input("Teste de número primo: "))
primo = True
for c in range (2,numero):
    if numero%c == 0:
        primo = False
if primo and numero != 1:
    print("Este é um número primo")
else:
    print("Este não é um núemro primo")    