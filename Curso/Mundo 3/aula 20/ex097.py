def escreva(msg):
    print((len(msg)+4)*'~')
    print(f'  {msg}')
    print((len(msg)+4)*'~')

texto = input('Escreva: ').strip()
escreva(texto)