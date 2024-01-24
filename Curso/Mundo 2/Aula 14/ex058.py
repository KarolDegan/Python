from random import randint
computador = randint(0,10)
soma = 1
print(30*"-")
print("Adivinhe o Número")
print(30*"-")
t = int(input("Qual número (0,10) o computador pensou?"))
while t != computador:
    soma += 1
    print("Não é esse número!")
    t = int(input("Qual número (0,10) o computador pensou?"))
print("Parabens! \nO número é {} \nVocê precisou de {} tentativas".format(computador,soma))