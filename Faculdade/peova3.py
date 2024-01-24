def f(a, b, n):
    for i in range (n):
      if a[i] == b[i]:
         return False
    return True

lista1= []
lista2 = []
for i in range (2):
    lista1.append(int(input('Adicione número a lista: ')))
for i in range (2):
    lista2.append(int(input('Adicione número a lista: ')))
retorno = f(lista1,lista2,2)
if retorno:
   print("Verdade")
else:
   print("Falso")