import pandas as pd
from math import comb
from scipy.stats import binom

dados = pd.read_csv('../dados.csv')

## Distribuição Binomial

# #combinção
# combina = comb(25,20)
# print(1/combina)

"""
Em um concurso para preencher uma vaga de cientista de dados temos um total de 10 questões de múltipla escolha com 3 alternativas possíveis em cada questão. Cada questão tem o mesmo valor. Suponha que um candidato resolva se aventurar sem ter estudado absolutamente nada. Ele resolve fazer a prova de olhos vendados e chutar todas as resposta. Assumindo que a prova vale 10 pontos e a nota de corte seja 5, obtenha a probabilidade deste candidato acertar 5 questões e também a probabilidade deste candidato passar para a próxima etapa do processo seletivo.
"""
numero_de_alternativas_por_questao = 3
p = 1 / numero_de_alternativas_por_questao # probabilidade de sucesso
q = 1 - p # probabilidade de fracasso
k = 5 # eventos com sucesso
n = 10 #numero de ensaios
# probabilidade_binomial = (comb(n, k)) * (p ** k) * (q ** (n - k))
# print(probabilidade_binomial)
# probabilidade = binom.pmf(k,n,p)
# print(probabilidade)

# passar =binom.pmf([5, 6, 7, 8, 9, 10], n, p).sum()
# print(passar)

probabilidade = (comb(10,3)*((1/6)**3)*((5/6)**7))
n = 10
p = 1/6
passar =binom.pmf([3,4,5, 6, 7, 8, 9, 10], n, p).sum()
print('%0.8f' % passar)