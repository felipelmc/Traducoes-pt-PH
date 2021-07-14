#carregando_dados.py

import pandas as pd

df = pd.read.csv('thor_wwii.csv')
print(df)

df.columns.tolist()