#municoes_por_pais.py
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool

from bokeh.palettes import Spectral5
from bokeh.transform import factor_cmap
output_file('municoes_por_pais.html')

df = pd.read_csv('thor_wwii.csv')

agrupado = df.groupby('COUNTRY_FLYING_MISSION')['TOTAL_TONS', 'TONS_HE', 'TONS_IC', 'TONS_FRAG'].sum()

agrupado = agrupado / 1000

fonte = ColumnDataSource(agrupado)
paises = fonte.data['COUNTRY_FLYING_MISSION'].tolist()
p = figure(x_range=paises)

mapa_de_cores = factor_cmap(field_name='COUNTRY_FLYING_MISSION',
                    palette=Spectral5, factors=paises)

p.vbar(x='COUNTRY_FLYING_MISSION', top='TOTAL_TONS', source=fonte, width=0.70, color=mapa_de_cores)

p.title.text ='Munições Lançadas por País Aliado'
p.xaxis.axis_label = 'País'
p.yaxis.axis_label = 'Quilotons de Munição'

hover = HoverTool()
hover.tooltips = [
    ("Totais", "@TONS_HE Explosivo / @TONS_IC Incendiária / @TONS_FRAG Fragmentação")]

hover.mode = 'vline'

p.add_tools(hover)

show(p)