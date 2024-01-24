from random import randint
comp = (randint(-999,999),randint(-999,999),randint(-999,999),randint(-999,999),randint(-999,999))
print('Eu sorteei os valores: ', comp)
print('Maior: ', sorted(comp)[-1])
print('Menor:', sorted(comp)[0])