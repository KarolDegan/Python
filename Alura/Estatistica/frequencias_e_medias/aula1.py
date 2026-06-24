import pandas as pd

dados = pd.read_csv('dados.csv')
print(dados['Anos de Estudo'].unique())
print('De %s até %s anos' %(dados.Idade.min(),dados.Idade.max()))