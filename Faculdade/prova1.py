def pin(n):
    soma = 0
    sinal = 1
    for i in range (1,n+1, 2):
        soma += 4/(i*sinal)
        sinal = sinal * -1
    return soma

numero = int(input("Número natural maior que 0 e ímpar: "))
if numero%2 == 0:
    numero = int(input("Número natural maior que 0 e ímpar: "))
else:
   print(pin (numero))
