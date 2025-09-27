frase = str(input("Teste palindromo: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
print(junto)
for c in range (len(junto)-1,-1,-1):
    inverso += junto[c]
print(inverso)
if inverso == junto:
    print("Palindromo")
else:
    print("Não é palindromo")