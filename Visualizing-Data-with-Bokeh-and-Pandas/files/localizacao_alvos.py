#localizacao_alvos.py
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, Range1d
from bokeh.layouts import layout
from bokeh.palettes import Spectral3
from bokeh.tile_providers import CARTODBPOSITRON
from pyproj import Proj, transform
output_file('mapeando_alvos.html')

#função auxiliar para converter latitude/longitude para easting/northing para mapeamento
#isso depende de funções da biblioteca pyproj
def LongLat_to_EN(long, lat):
    try:
      easting, northing = transform(
        Proj(init='epsg:4326'), Proj(init='epsg:3857'), long, lat)
      return easting, northing
    except:
      return None, None

df = pd.read_csv('thor_wwii.csv')
#auxiliar para converter todas as latitudes e longitudes para webmercator e armazenar numa nova coluna
df['E'], df['N'] = zip(*df.apply(lambda x: LongLat_to_EN(x['TGT_LONGITUDE'], x['TGT_LATITUDE']), axis=1))

agrupado = df.groupby(['E', 'N'])['TONS_IC',
'TONS_FRAG'].sum().reset_index()

filter = agrupado['TONS_FRAG']!=0
agrupado = agrupado[filter]

fonte = ColumnDataSource(agrupado)

esquerda = -2150000
direita = 18000000
inferior = -5300000
superior = 11000000

p = figure(x_range=Range1d(esquerda, direita), y_range=Range1d(inferior, superior))

provedor = get_provider('CARTODBPOSITRON')
p.add_tile(provedor)
p.circle(x='E', y='N', source=fonte, line_color='grey', fill_color='yellow')

p.axis.visible = False

show(p)