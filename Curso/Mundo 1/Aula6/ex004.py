v = input('Digite algo: ')
print('O tipo primitivo desse valor é: ', type(v))
print('Só tem espaços?', v.isspace())
print('É alfabético?', v.isalpha())
print('É numérico?', v.isnumeric())
print('É alfanumérico?', v.isalnum())
print(v.isascii())
print(v.isdecimal())
print(v.isdigit())
#print(v.isidentifier(), v.isdigit(), v.islower(), v.isprintable(), v.isnumeric(), v.istitle(), v.isupper())