ex = input('Digite a expressão').upper().strip()
teste = []
for c in range(len(ex)):
    if ex[c] == '(':
        teste.append('(')
    elif ex[c] == ')':
        if len(teste) > 0:
            teste.pop()
        else:
            teste.append(')')
            break
print(teste)
if len(teste) == 0:
    print('Tudo certo')
else:
    print('Parenteses errados na expressão')