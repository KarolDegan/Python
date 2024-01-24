a = int(input("Número natural: "))
b = int(input("Outro Número natural: "))
contador = 0
c = b
while a>=b:
    b = b + c
    contador += 1
print(contador)