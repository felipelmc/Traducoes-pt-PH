#anotando_tendencias.py
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from datetime import datetime
from bokeh.palettes import Spectral3
output_file('eto_operacoes.html')

df = pd.read_csv('thor_wwii.csv')

#filtrar para o Teatro Europeu de Operações
filtro = df['THEATER']=='ETO'
df = df[filtro]

df['MSNDATE'] = pd.to_datetime(df['MSNDATE'], format='%m/%d/%Y')
agrupado = df.groupby(pd.Grouper(key='MSNDATE', freq='M'))['TOTAL_TONS', 'TONS_IC', 'TONS_FRAG'].sum()
agrupado = agrupado / 1000

source = ColumnDataSource(agrupado)

p = figure(x_axis_type="datetime")

p.line(x='MSNDATE', y='TOTAL_TONS', line_width=2, source=source, legend='Todas as Munições')
p.line(x='MSNDATE', y='TONS_FRAG', line_width=2, source=source, color=Spectral3[1], legend='Fragmentação')
p.line(x='MSNDATE', y='TONS_IC', line_width=2, source=source, color=Spectral3[2], legend='Incendiária')

p.title.text = 'Teatro Europeu de Operações'

p.yaxis.axis_label = 'Quilotons de Munições Lançadas'

show(p)
