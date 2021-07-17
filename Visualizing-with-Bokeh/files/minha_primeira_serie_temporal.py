#minha_primeira_serie_temporal.py
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral3
output_file('serie_temporal_simples.html')

df = pd.read_csv('thor_wwii.csv')

#certifique-se de que MSNDATE tenha um formato de data
df['MSNDATE'] = pd.to_datetime(df['MSNDATE'], format='%m/%d/%Y')

#agrupado = df.groupby('MSNDATE')['TOTAL_TONS', 'TONS_IC', 'TONS_FRAG'].sum()
agrupado = df.groupby(pd.Grouper(key='MSNDATE', freq='M'))['TOTAL_TONS', 'TONS_IC', 'TONS_FRAG'].sum()
agrupado = agrupado/1000

fonte = ColumnDataSource(agrupado)

p = figure(x_axis_type='datetime')

p.line(x='MSNDATE', y='TOTAL_TONS', line_width=2, source=fonte, legend='Todas as munições')
p.line(x='MSNDATE', y='TONS_FRAG', line_width=2, source=fonte, color=Spectral3[1], legend='Fragmentação')
p.line(x='MSNDATE', y='TONS_IC', line_width=2, source=fonte, color=Spectral3[2], legend='Incendiária')

p.yaxis.axis_label = 'Quilotons de Munições Lançadas'

show(p)