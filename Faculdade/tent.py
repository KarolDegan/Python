n = int(input('numeorp inteiro'))
x = 1
reg = 0
while x**2 <= n:
    reg = x**2
    x += 1
if x**2 == n:
    print(x**2)
else:
    print(reg)