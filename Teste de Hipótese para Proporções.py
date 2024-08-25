#!/usr/bin/env python
# coding: utf-8

# ## Desafio ONG
# 
# Instruções
# 
# Somos uma ong de animais e queremos incentivar a adoção de pets. Para isso, vamos mostrar um vídeo de animais para as pessoas. Porém, não sabemos o que é mais efetivo: um vídeo de cachorros ou um vídeo de gatos.
# 
# Por isso, resolvemos rodar um experimento: vamos criar 2 vídeos, um de cachorro e outro de gato. Depois, vamos perguntar as pessoas a probabilidade de que ela adote um animal.
# 
# As pessoas desse experimento só verão 1 vídeo cada
# Ao final do vídeo perguntamos a elas a probabilidade de que elas adotem um animal
# As amostras são aleatórias e sem viéses sistemáticos
# Objetivo: Avaliar qual animal (cachorro ou gato) deve estar em um vídeo de campanha de adoção
# 
# Experimento: 500 pessoas que não possuem animais de estimação assistem aos vídeos de campanha de adoção. Os vídeos são idênticos com exceção dos animais mostrados:
# 
# 250 pessoas aleatorizadas para o vídeo com gato
# 250 pessoas aleatorizadas para o vídeo com cachorro
# Resposta: "Qual a chance de adotar um pet? (0-100)" depois do vídeo
# 
# A média de probabilidade de quem ve o vídeo de gato é igual a de cachorro?

# ### Carregamento das bibliotecas

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns 
from matplotlib import pyplot as plt 


# ### Análise descritiva do dataframe

# In[2]:


# lendo o arquivo csv 
df = pd.read_csv(r'C:\Users\vivia\OneDrive\Área de Trabalho\DATA SCIENCE\EBA - Estatistica Avançada\09 - Teste de hipotese e intervalo de confiança para medias e proporçoes\cachorro_gato.csv')


# A coluna grupo refere-se a pessoa viu o video de cachorro ou de gato. 0 é cachorro e 1 é gato. </br>
# Escore é probabilidade da pessoa adotar um pet após ver o vídeo

# In[3]:


# visualizando o dataframe 

df


# Queremos entender como os grupos (0: cachorro e 1: gato) se comportam. Portanto vamos agrupar os dados de acordo com o grupo e calcular as principais estatísticas.

# In[4]:


# principais estatísticas agrupadas de acordo com o grupo.

df.groupby('grupo').describe()


# Vemos aqui que a média e mediana do escore de quem viu um vidéo de gato é ligeiramente maior do que quem viu video de cachorro.

# ### Histograma por grupo
# 
# Mostrando como está a distribuição de cada um dos grupos

# In[5]:


sns.histplot(df[df['grupo'] == 0]['escore'], label = 'Cachorro', color = "red") #histograma grupo que viu o video de cachorro
sns.histplot(df[df['grupo'] == 1]['escore'], label = 'Gato', color = "blue") # histograma grupo que viu o video de gato
plt.xlabel('Escore (0 a 100)')
plt.legend()
plt.show()


# O histograma acima mostra que as distribuições são muito semelhantes. Como ambas seguem aproximadamente uma normal, vamos fazer um teste de hipótese para ver qual média é maior. 
# 
# O Teste de hipótese escolhido deve ser para média, com 2 amostras independentes (quem viu vídeo de cachorro só viu cachorro e quem viu video de gato só viu de gato). Como não temos o desvio-padrão da população, podemos usar o teste t. 

# ## Comparação entre os grupos por teste-t independente 

# Vamos comparar as médias dos escores dos dois grupos. São estatisticamente diferentes?

# In[6]:


# Importando a função que realiza o teste-t para amostras independentes 

from scipy.stats import ttest_ind


# In[7]:


# a função retorna uma tupla. O primeiro valor é o valor do t e o segundo é o p-value 

ttest_ind(df[df['grupo'] == 0]['escore'], df[df['grupo'] == 1]['escore'])


# In[8]:


# organizando a tupla para denominar cada um dos valores 

t, pvalue = ttest_ind(df[df['grupo'] == 0]['escore'], df[df['grupo'] == 1]['escore'])


# In[9]:


print('stat=%.3f, p=%.3f' % (t, pvalue))


# O nosso p-valor aqui foi de aproximadamente 0.36 </br>
# 
# Estabelecendo o nível de significância como 5%, como p > 0,05, não temos evidências suficientes para rejeitar a hipótese nula. Logo, dizemos que estatisticamente as médias são iguais. 

# ## Sumário

# ### Testes de Hipóteses:
# 1. Teste T para amostras indepedentes e desvio padrão desconhecido:
# 
# - Cálculo do t-score e p_value (respectivamente): </br>
# t, pvalue = ttest_ind(valores_amostra_1, valores_amostra_1)
# 
# 
# 2. Formatação de String: </br>
# print('nome_1=%.3f, nome_2=%.3f' % (variavel_1, variavel_2)) </br>
# 
# - String de formatação: 'nome_1=%.3f, nome_2=%.3f' é uma string que contém texto literal e marcadores de posição para valores numéricos. Os marcadores de posição %.3f são substituidos pelos valores de t e pvalue. </br>
# 
# 
# - Operador %: O operador % é utilizado para formatar a string, substituindo os marcadores de posição pelos valores correspondentes de variavel_1 e variavel_2. </br>
# 
# 
# - .3f: determina a quantidade de casas decimais que queremos que apareça no resultado e que o valor será formatado como ponto flutuante (float).

# In[ ]:





# In[ ]:




