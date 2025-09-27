print(30*"-")
print("CALCULADORA IMC")
print(30*"-")
altura = float(input("Altura: "))
peso = float(input("Peso: "))
imc = peso/(altura**2)
print("IMC: ",imc)
if imc< 18.5:
    print("Abaixo do peso")
elif imc<25:
    print("Peso ideal")
elif imc<30:
    print("Sobrepeso")
elif imc<40:
    print("obesidade")
else:
    print("obesidade morbida")