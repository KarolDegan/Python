altura = float(input('Altura da parede em metros: '))
largura = float(input('Largura da parede em metros: '))
area = altura*largura
print('Área: ', area, 'm²')
tinta = area/2
print('São necessario {} litros de tinta para pintar {}m²'.format(tinta,area))