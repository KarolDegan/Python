peso = float(input("peso: "))
menor = peso
maior = peso
for c in range(4):
    peso = float(input("peso: "))
    if peso < menor:
        menor = peso
    if peso > maior:
        maior = peso
print("Maior{}  Menor{}".format(maior,menor))
#maior = 0
#menor = 0
#for c in range(4):
#   if c == 1:
#       maior = peso
#       menor = peso
#   else:
#       if peso > maior:
#           maior = peso
#       if peso < menor:
#           menor = peso