#municoes_por_pais_empilhadas.py
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral3
output_file('tipos_de_municoes.html')

df = pd.read_csv('thor_wwii.csv')

filtro = df['COUNTRY_FLYING_MISSION'].isin(('USA','GREAT BRITAIN'))
df = df[filtro]

agrupado = df.groupby('COUNTRY_FLYING_MISSION')['TONS_IC', 'TONS_FRAG', 'TONS_HE'].sum()

#convertemos para quilotons novamente
agrupado = agrupado / 1000

fonte = ColumnDataSource(agrupado)
paises = fonte.data['COUNTRY_FLYING_MISSION'].tolist()
p = figure(x_range=paises)

p.vbar_stack(stackers=['TONS_HE', 'TONS_FRAG', 'TONS_IC'],
             x='COUNTRY_FLYING_MISSION', source=fonte,
             legend = ['Explosivo', 'Fragmentação', 'Incendiário'],
             width=0.5, color=Spectral3)

p.title.text ='Tipos de Munições Lançadas por País Aliado'
p.legend.location = 'top_left'

p.xaxis.axis_label = 'País'
p.xgrid.grid_line_color = None	#remove as linhas de grade de x

p.yaxis.axis_label = 'Quilotons de Munição'

show(p)