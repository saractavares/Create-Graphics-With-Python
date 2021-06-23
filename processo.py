#!/usr/bin/env python
# coding: utf-8

# # Análise de Dados com Python

# In[111]:


import pandas as pd

tabela = pd.read_excel(r'C:\Users\Samsung\Downloads\processo_seletivo.xlsx')

print(tabela.info())

display(tabela['Status'].value_counts())
display(tabela['Status'].value_counts(normalize=True).map('{:.1%}'.format))
for Disciplinas in tabela.index:
  display(tabela['Disciplinas'].value_counts())

import plotly.express as px
#importando a biblioteca plotly
for coluna in tabela:
#percorre a tabela e armazena na variável nomeada "coluna"
    grafico = px.histogram(tabela, x=coluna, color='Status')
    #chama o grafico do tipo histograma e atribui na variavel 'Status'
    grafico.show()


# In[ ]:





# In[ ]:





# In[ ]:





# ### Conclusões e Ações

# Escreva aqui suas conclusões:
