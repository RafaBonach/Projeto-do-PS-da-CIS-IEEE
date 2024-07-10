# ------------------------------ Questão 1, tratando dados -------------------------------

import pandas as pd

"""data = pd.read_csv('./Drugs.csv')
data_pre = data.copy()
del data_pre['ID']
del data_pre['Income (USD)']
data_pre['Impulsive'] = pd.to_numeric(data_pre['Impulsive'], errors='coerce')
# Alterando os valores nulos para 0
data_pre_fill = data_pre.fillna(value={
    'Nscore': 0,
    'Escore': 0,
    'Oscore':0,
    'AScore':0,
    'Cscore':0,
    'Impulsive':0,
    'SS':0
})
#print(data_pre_fill) # valores que antes eram NaN agora são 0
data_pre_fill = data_pre.fillna(value={
    'Nscore': 0,
    'Escore': 0,
    'Oscore':0,
    'AScore':0,
    'Cscore':0,
    'Impulsive':0,
    'SS':0
})
#remove no prprio dataframe, todas as linhas com valores NaN em quaisquer colunas/atributos
data_pre_fill.dropna(inplace=True)
#print(data_pre.info())
#print(data_pre_fill.info())
#data_pre_fill.to_csv('./Drugs_preprocessado.csv', index=False)
"""
# --------------------- Questão 3, relação entre educacao e substancias -------------------------
data = pd.read_csv('./Drugs_preprocessado.csv')
data_cp = data.copy()
consumo = ['Alcohol', 'Amphet', 'Amyl', 'Benzos', 'Caff', 'Cannabis', 'Choc', 'Coke', 'Crack', 'Ecstasy','Heroin', 'Ketamine', 'Legalh', 'LSD', 'Meth', 'Mushrooms', 'Nicotine']
cl = []
nrows, ncols = data_cp.shape
for k in range(7):
    for i in range(nrows):
        cl.append(0)
        for j in consumo:
            if data_cp.loc(i, consumo) == [f'CL{k}']:
                cl[i] += 1
    


print(data_cp["CL0"])

#print(data_cp['CL6'])


#education_group = data_pre_fill.groupby('Education')
#print(education_grouped.indices)