import pandas as pd

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

# print(df)

## MÈDIA ponto de equilibrio, nem sempre representa bem o conjunto de dados

media = df['Fulano'].mean()
# print(media)

media_renda = dados.Renda.mean()
# print(media_renda)

#Retorna as quantidades de cada sexo para cada categoria
media_por_sexo =dados.groupby(['Sexo']).mean()

media_de_renda_por_sexo = dados.groupby(['Sexo'])['Renda'].mean()


# dataset.groupby('Sexo').mean().loc['H']

##MEDIANA divide a série exatamente ao meio
# 1.ordenar os dados
# 2.identificar o número de observações (n)
# 3. identificar o elemento mediano

notas_fulano = df.Fulano
notas_fulano = notas_fulano.sort_values()
notas_fulano = notas_fulano.reset_index()
n = notas_fulano.shape[0] #retorna a quantidade de elementos
elemento_md = (n +1)/2
mediana = notas_fulano.loc[elemento_md - 1]
# ou 
notas_fulano = df.Fulano
mediana_por_pandas = notas_fulano.median()
# print(mediana_por_pandas)

par = [6,4,9,1]
par.sort()
print(par)
numero_de_elementos = len(par)
if (numero_de_elementos%2 == 0):
    posicao_primeiro_elemento = int(numero_de_elementos/2)
    
    primeiro_elemento = par[posicao_primeiro_elemento -1]
    
    posicao_segundo_elemento = int(numero_de_elementos/2 + 1)
    segundo_elemento = par[posicao_segundo_elemento -1]
    
    mediana_par = (primeiro_elemento+segundo_elemento)/2
    # print(mediana_par)
# ou

par_pandas = pd.Series([6,4,9,1])
mediana_par_por_pandas = par_pandas.median()
# print(mediana_par_por_pandas)

## MODA o que mais repete, geralmente para valores qualitativos
moda = df.mode()