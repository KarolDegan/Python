n = int(input('Natural maior que 0: '))
primo = True
for i in range (n-1,1,-1):
    x = n%i
    if x==0:
        primo = False
if primo and n!=1:
    print('Número primo')
else:
    print('Não é número primo')