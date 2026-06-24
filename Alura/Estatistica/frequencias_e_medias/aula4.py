import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dados = pd.read_csv('dados.csv')

# particionamento
quartil = dados.Renda.quantile([0.25,0.5,0.75])

decil = dados.Renda.quantile([i/10 for i in range(1,10)])

# g = sns.histplot(dados.Idade,
#                 cumulative= True,
#                 kde = True,
#                   kde_kws = {'cumulative': True},
#                   bins = 10)

# g.figure.set_size_inches(14, 6)
# g.set_title('Distribuição de Frequências - Altura', fontsize=18)
# g.set_ylabel('Acumulado', fontsize=14)
# g.set_xlabel('Anos', fontsize=14)

# plt.show()

## BOXPLOT

ax = sns.boxplot( x = 'Altura', data = dados, orient = 'h')
ax = sns.boxplot( x = 'Renda', y='Sexo', data = dados.query('Renda<10000'), orient = 'h')
ax.figure.set_size_inches(12, 4)
ax.set_title('Altura', fontsize=18)
ax.set_xlabel('Metros', fontsize=14)

plt.show()