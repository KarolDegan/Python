import pandas as pd
from math import sqrt
dados = pd.read_csv('dados.csv')

df = pd.DataFrame(data = {'Fulano':[8,10,4,8,6,10,8],
                          'Beltrano':[10,2,0.5,1,3,9.5,10],
                          'Sicrano': [7.5,8,7,8,8,8.5,7]},
                          index = ['Matemática',
                                   'Português',
                                   'Inglês',
                                   'Geografia',
                                   'História',
                                   'Física',
                                   'Química'])

df.rename_axis('Matérias', axis = 'columns', inplace = True)

## Mediadas de Disperção

## Desvio médio, soma das distancias do valor para a média, depois faz uma média encima disso


notas_fulano = df[['Fulano']]
nota_media_fulano = notas_fulano.mean()['Fulano']
print(nota_media_fulano)
notas_fulano['Desvio'] = notas_fulano['Fulano'] - nota_media_fulano
notas_fulano['|Desvio|'] = notas_fulano['Desvio'].abs()
desvio_medio_absoluto = notas_fulano['|Desvio|'].mean()

## Variancia - unidade de medida tbm elevada ao quadrado
variancia = notas_fulano['Fulano'].var()
print(variancia)

# Desvio padrão - raiz quadrada da variancia
desvio_padrao = sqrt(variancia)
print(desvio_padrao)

dataset = pd.DataFrame({
    'Sexo': ['H', 'M', 'M', 'M', 'M', 'H', 'H', 'H', 'M', 'M'],
    'Idade': [53, 72, 54, 27, 30, 40, 58, 32, 44, 51]
})

desvio_padrão_mulheres = dataset.groupby(['Sexo']).std().loc['M']
print(desvio_padrão_mulheres)