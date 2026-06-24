import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

dados = pd.read_csv('dados.csv')
# print(dados['Sexo'].value_counts())
# print(dados['Sexo'].value_counts(normalize = True) *100)

# frequencia = dados['Sexo'].value_counts()
# percentual = dados['Sexo'].value_counts(normalize = True) *100
# dist_freq_qualitativa = pd.DataFrame({'Frequencia': frequencia, 'Porcentagem (%)': percentual})

# print(dist_freq_qualitativa)

# dist_freq_qualitativa.rename(index = {0: 'Masculino', 1 : 'Feminino'}, inplace = True)
# dist_freq_qualitativa.rename_axis('Sexo', axis = 'columns', inplace = True)
# print(dist_freq_qualitativa)

# sexo = { 0 : 'Masculino',
#         1: 'Feminino'}

# cor = {0: 'Indígena',
#        2: 'Branca',
#        4: 'Preta',
#        6: 'Amarela',
#        8: 'Parda',
#        9: 'Sem declaração'}

# frequencia = pd.crosstab(dados.Sexo, dados.Cor)
# frequencia.rename(index = sexo, inplace = True)
# frequencia.rename(columns= cor, inplace = True)

# print(frequencia)

# percentual = pd.crosstab(dados.Sexo, dados.Cor, normalize = True)*100
# percentual.rename(index = sexo, inplace = True)
# percentual.rename(columns= cor, inplace = True)

# print(percentual)

# renda_media = pd.crosstab(dados.Sexo, dados.Cor, aggfunc = 'mean', values = dados.Renda)
# renda_media.rename(index = sexo, inplace = True)
# renda_media.rename(columns= cor, inplace = True)

# print(renda_media)

# print(dados.Renda.min())
# print(dados.Renda.max())

classes = [0,1576,3152,7880,15760,200000]
labels = ['E','D','C','B','A']

# # print(pd.cut(x=dados.Renda, bins = classes, labels = labels,include_lowest = True))
# # print(dados.head())

frequencia = pd.Series.value_counts(pd.cut(x=dados.Renda, bins = classes, labels = labels,include_lowest = True))

percentual = pd.Series.value_counts(pd.cut(x=dados.Renda, bins = classes, labels = labels,include_lowest = True),
                                    normalize= True)


# #normalize

dist_freq_qualitativas_personalizadas = pd.DataFrame({'Frequencia': frequencia, 'Porcentagem (%)': percentual})
# print(dist_freq_qualitativas_personalizadas)

# print(dist_freq_qualitativas_personalizadas.sort_index(ascending = False))

# ##FAZER SUAS PROPRIA DIVISÃO DE LIMITES

# n = dados.shape[0] #[76840 rows x 7 columns]
# k = 1 +(10/3) * np.log10(n)
# k = int(k.round(0))

# frequencia = pd.Series.value_counts(pd.cut(x = dados.Renda,
#                                            bins = k,
#                                            include_lowest= True),
#                                            sort = False)

# percentual = pd.Series.value_counts(pd.cut(x = dados.Renda,
#                                            bins = k,
#                                            include_lowest= True),
#                                            sort = False,
#                                            normalize= True)

# dist_freq_quantitativas_amplitude_fixa = pd.DataFrame(
#     {'Frequencia': frequencia, 'Porcentagem (%)': percentual}
# )

# print(dist_freq_quantitativas_amplitude_fixa)

## GRÀFICO

# g = sns.displot(dados.Altura, kde = False)

# g.figure.set_size_inches(12, 6)
# g.ax.set_title('Distribuição de Frequências - Altura', fontsize=18)
# g.ax.set_xlabel('Metros', fontsize=14)

# plt.show()

ax = dist_freq_qualitativas_personalizadas['Frequencia'].plot.bar(width= 1, color= 'blue', alpha = 0.2, figsize= (12, 6))

plt.show()
