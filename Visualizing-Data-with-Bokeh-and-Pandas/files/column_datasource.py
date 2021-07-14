#column_datasource.py
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool

output_file('column_datasource_exemplo.html')

df = pd.read_csv('thor_wwii.csv')

amostra = df.sample(50)
fonte = ColumnDataSource(amostra)

p = figure()
p.circle(x='TOTAL_TONS', y='AC_ATTACKING',
         source=fonte,
         size=10, color='green')

p.title.text = 'Aeronave de Ataque e Munições Lançadas'
p.xaxis.axis_label = 'Toneladas de Munições Lançadas'
p.yaxis.axis_label = 'Número de Aeronaves de Ataque'

hover = HoverTool()
hover.tooltips=[
    ('Attack Date', '@MSNDATE'),
    ('Attacking Aircraft', '@AC_ATTACKING'),
    ('Tons of Munitions', '@TOTAL_TONS'),
    ('Type of Aircraft', '@AIRCRAFT_NAME')
]

p.add_tools(hover)

show(p)