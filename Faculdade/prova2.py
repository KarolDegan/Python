def adjacentes(n):
    resto = n%10
    n = n//10
    while n > 0 :
        if resto == n%10:
            return True
        resto = n%10
        n = n//10
    return False

numero = int(input("Número inteiro maior ou igaul a 10: "))
if numero <=10:
    numero = int(input("Número inteiro maior ou igaul a 10: "))
else:
   adj = adjacentes(numero)
   if adj:
       print("Há número igauis adjacentes!")
   else:
       print("Não há números igauis adjacentes!")