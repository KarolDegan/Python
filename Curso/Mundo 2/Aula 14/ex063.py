print(30*"-")
print("Sequencia de Fibonacci")
print(30*"-")
termos = int(input("Quantos termos deseja: "))
c = 1
n1 = 0
n2 = 0
n3 = 1
print(n1)
while c < termos:
    print(n3)
    n1 = n2
    n2 = n3
    n3 = n2 + n1
    c += 1