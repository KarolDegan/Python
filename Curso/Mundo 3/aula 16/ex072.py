porex = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze','quinze','dezeceis','dezecete','dezoito','dezenove','vinte')
print(30*'-')
print('ESCREVA POR EXTENSO')
print(30*'-')
n = int(input('Numro entre 0 e 20: '))
while n > 20 or n < 0:
    n = int(input('Numro entre 0 e 20: '))
print(f'Você digitou o número: {porex[n]}')