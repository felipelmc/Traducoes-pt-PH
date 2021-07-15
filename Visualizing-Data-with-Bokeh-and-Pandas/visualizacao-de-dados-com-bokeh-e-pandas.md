---
title: Visualização de dados com Bokeh e Pandas
layout: lesson
slug: visualizacao-de-dados-com-bokeh-e-pandas
date: 2012-07-17
translation_date: 2018-07-27
authors:
- Charlie Harper
reviewers:
- Zoe LeBlanc
- Ben Schmidt
editors:
- James Baker
- Ian Milligan
translator:
- Felipe Lamarca
translation-editor:
- 
translation-reviewer:
- 
difficulty: 2
review-ticket: 
activity: análise
topics: [python, data-manipulation, mapping]
abstract: "Nesta lição você aprenderá a explorar e apresentar dados visualmente em Python utilizando as bibliotecas Bokeh e Pandas."
redirect_from: 
original: visualizing-with-bokeh
avatar_alt: Men with torches in an antique tomb
---

# Devo lembrar que existe um notebook a ser traduzido nesta lição

# Sumário

{% include toc.html %}

# Visão Geral

A capacidade de carregar dados brutos, amostrá-los e, em seguida, explorar e apresentá-los visualmente é uma habilidade valiosa entre as disciplinas. Neste tutorial, você aprenderá como fazer isso em Python utilizando as bibliotecas Bokeh e Pandas. Mais especificamente, trabalharemos visualizando e explorando aspectos dos bombardeiros da Segunda Guerra Mundial conduzidos por potências Aliadas.

Ao final dessa lição, você será capaz de:

- Carregar dados tabulares do formato CSV;
- Performar o básico de manipulação de dados, tal como agregar e sub-amostrar dados brutos;
- Visualizar dados quantitativos, categóricos e geográficos para exibição na web;
- Adicionar diversos tipos de interação às suas visualizações;

Para alcançar esses objetivos, trabalharemos com uma variedade de exemplos de visualização usando THOR, dataset (conjunto de dados) que descreve as operações históricas de bombardeio.

## O Dataset WWII THOR 

O Theatre History of Operations (THOR) lista as operações de bombardeio aéreo durante a Primeira Guerra Mundial, a Segunda Guerra Mundial, a Guerra da Coréia e a Guerra do Vietnã realizadas pelos Estados Unidos e pelas potências aliadas. Os registros foram compilados a partir de documentos liberados pelo tenente-coronel Jenns Robertson. O THOR é disponibilizado ao público por meio de uma parceria entre o Departamento de Defesa dos Estados Unidos e o [data.world](https://data.world/datamil).

Cada linha do dataset THOR contém informações sobre uma única missão ou operação de bombardeio. Essas informações podem incluir a data da missão, decolagem e localização do alvo, o tipo de alvo, aeronave envolvida e os tipos e pesos das bombas lançadas no alvo. A [documentação do THOR](https://data.world/datamil/thor-data-dictionary) oferece informações detalhadas sobre a estrutura do dataset.

Para esse tutorial, utilizaremos uma versão modificada do dataset THOR sobre a Segunda Guerra Mundial. A versão original consiste em 62 colunas de informações digitalizadas a partir dos formulários. Para tornar esse dataset mais manejável para os nossos propósitos, a versão que utilizaremos foi reduzida a 19 colunas que incluem as informações principais sobre as missões e os dados de bombardeio. Essas colunas são discutidas abaixo quando carregarmos os dados pela primeira vez. O conjunto de dados completo está disponível para download [aqui](https://data.world/datamil/world-war-ii-thor-data).

O dataset utilizado nesse tutorial pode ser encontrado em [thor_wwii.csv](https://raw.githubusercontent.com/programminghistorian/ph-submissions/gh-pages/assets/visualizing-with-bokeh/thor_wwii.csv). Este ficheiro é necessário para completar a maioria dos exemplos abaixo.

Utilizaremos Bokeh e Pandas para responder algumas das perguntas a seguir:

- Quais os tipos e pesos das munições que foram lançadas durante a Segunda Guerra Mundial? Quais padrões podemos discernir no uso de diferentes tipos de munições?
- De que modo os tipos e pesos das munições lançadas mudam no decorrer da Segunda Guerra Mundial? Como essas mudanças correspondem a eventos militares mais gerais?
- Em quais alvos as munições foram lançadas durante a guerra? Foram determinados tipos de munições limitados a certos teatros de operações ou alvos?

## Outros Datasets Possíveis

Caso este dataset não se adeque aos seus interesses ou caso queira praticar mais após completar este tutorial, estes são alguns outros datasets interessantes que você pode usar utilizar com Bokeh e Pandas:

- [Julgamentos de Feitiçaria na Escócia](https://data.world/history/scottish-witchcraft/): um conjunto de dados de várias tabelas sobre mais de 4.000 pessoas acusadas de bruxaria entre 1536 e 1736.

- [Eventos de Agitação Civil](https://data.world/history/civil-unrest-event-data): Uma única tabela que cataloga mais de 60.000 eventos de agitação civil em todo o mundo desde o fim da Segunda Guerra Mundial.

- [Comércio Transatlântico de Escravos](https://www.slavevoyages.org/voyage/database): Dados tabulares pesquisáveis e personalizáveis sobre 36.000 viagens de escravos que transporaram mais de 10 milhões de escravos dos séculos XVI a XIX.
  
Todos os três datasets contêm dados quantitativos, qualitativos e temporais comparáveis aos encontrados no dataset THOR. Os datasets de Eventos de Agitação Civil e Comércio Transatlântico de Escravos possue dados espaciais, embora isso esteja faltando nos dados sobre Julgamento de Feitiçaria na Escócia.

# Iniciando

## Pré-requisitos

Esse tutorial pode ser completado utilizando qualquer sistema operacional. Ele requer o Python 3 e um navegador web. Você pode utilizar qualquer editor de texto para escrever seu código. 

Esse tutorial assume que você possui conhecimentos básicos da linguagem Python e suas estruturas de dados, particularmente listas.

Caso você trabalhe no Python 2, será necessário criar um ambiente virtual para o Python 3; e, mesmo que você trabalhe no Python 3, criar um ambiente virtual para este tutorial é uma boa prática.

## Criando um Ambiente Virtual de Python 3

Um ambiente virtual Python é um ambiente isolado no qual você pode instalar bibliotecas e executar código. Vários ambientes virtuais diferentes podem ser criados para trabalhar com diferentes versões de Python e bibliotecas Python. Ambientes virtuais são úteis porque garantem que você tenha instaladas somente as bibliotecas necessárias e que você não precise lidar com conflitos de versão. Um benefício adicional dos ambientes virtuais é que você pode compartilhá-los com outras pessoas de modo que você saiba que seu código poderá ser executado em outra máquina.

[Miniconda](https://conda.io/miniconda.html) é uma forma fácil de criar ambientes virtuais que é simples de instalar em qualquer sistema operacional. Você deve instalar o Miniconda e seguir as instruções para [Windows](https://conda.io/projects/conda/en/latest/user-guide/install/windows.html), [Mac](https://conda.io/projects/conda/en/latest/user-guide/install/macos.html), ou [Linux](https://conda.io/projects/conda/en/latest/user-guide/install/linux.html) conforme apropriado para seu sistema operacional.

Uma vez que tenha feito o download e instalado o Miniconda em seu sistema operacional, é possível verificar se ele está instalado corretamente abrindo uma linha de comando e digitando:

```python
conda info
```

Se você visualizar uma informação de versão similar a que se segue, então Miniconda foi instalado corretamente.

```python
Current conda install:
               platform : linux-64
          conda version : 4.3.29
          ...
```

Utilizaremos o Miniconda para criar um ambiente virtual de Python 3 chamado *bokeh-amb* para esse tutorial. Na linha de comando, digite o seguinte:

```python
conda create --name bokeh-amb python=3.6
```

Diga 'yes' quando for solicitado a instalar novos pacotes.

Para ativar o ambiente virtual *bokeh-amb*, o comando é um pouco diferente dependendo do sistema operacional.

```python
source activate bokeh-amb #For Linux/MacOS
activate bokeh-amb #For Windows
```

Sua linha de comando deve agora mostrar que você está no ambiente virtual *bokeh-amb*. 

Quando quiser deixar o ambiente virtual, basta digitar o comando apropriado para o seu sistema operacional.

```python
source deactivate #For Linux/MacOS
deactivate #For Windows
```

## Instalando pacotes

No seu ambiente virtual *bokeh-amb*, já ativado, emita o seguinte comando para instalar os pacotes Python para este tutorial.

```python
pip install pandas bokeh pyproj
```

Para obter as versões exatas utilizadas para escrever esse tutorial (nota: essas podem não ser as versões mais recentes de cada um dos pacotes do Python) você pode passar os seguintes números de versão ao `pip`.

```python
pip install pandas==0.23.1 bokeh==0.13.0 pyproj==1.9.5.1
```

## Executando Exemplos de Código

É mais fácil criar primeiro um único diretório e salvar cada exemplo de código como *.py* dentro dele. Quando estiver pronto para executar o arquivo de código, navegue até esse diretório no prompt de comando e certifique-se de que seu ambiente virtual esteja ativado. Lembre-se de que você sempre pode ativar o ambiente com o seguinte comando apropriado para o seu sistema operacional.

```python
source activate bokeh-amb #For Linux/MacOS
activate bokeh-amb #For Windows
```

Dentro do ambiente virtual, você pode executar o código digitando:

```python
python nome-do-arquivo.py
```

Um Jupyter Notebook contendo o código utilizado neste tutorial também está [disponível](https://raw.githubusercontent.com/programminghistorian/ph-submissions/gh-pages/assets/visualizing-with-bokeh/visualizing-with-bokeh.ipynb) no caso de você preferir trabalhar ao longo do tutorial sem instalar um ambiente virtual. Você pode aprender mais sobre Jupyter Notebook [aqui](http://jupyter.org). Caso tenha criado um ambiente virtual utilizando Miniconda, como discutido acima, você pode instalar Jupyter Notebook no ambiente digitando `conda install jupyter`.

# O Básico de Bokeh

## O que é Bokeh?

Bokeh é uma biblioteca que serve para criar visualizações de dados interativas num navegador web. Ele oferece uma sintaxe concisa e legível, que permite a apresentação de  de uma maneira rápida e esteticamente agradável. Caso você já tenha trabalhado com visualização em Python antes, é provável que tenha usado o Matplotlib. Vale a pena mencionar brevemente as diferenças entre Bokeh e Matplotlib e quando se deve dar preferência à utilização de um em detrimento de outro.

Matplotlib existe desde 2002 e há muito tempo tem sido uma biblioteca padrão para visualização de dados em Python. Bokeh surgiu em 2013. Essa diferença de idade significa que o Matplotlib amadureceu muito antes do lançamento do Bokeh; ainda assim, Bokeh alcançou um alto nível de maturidade em um curto período de tempo. 

As intenções de uso do Matplotlib e do Bokeh são bastante diferentes. Matplotlib cria gráficos estáticos que são úteis para visualizações rápidas e simples, ou para a criação de imagens com qualidade para publicação. Bokeh cria visualizações para exibição na web (tanto localmente quanto incorporados numa página web) e, mais importante, as visualizações são idealizadas para serem altamente interativas. Matplotlib não oferece nenhum desses recursos.

Caso deseje interagir visualmente com os seus dados de maneira exploratória ou queira oferecer visualizações de dados interativas para um público na web, Bokeh é a biblioteca para você! Se seu interesse principal é produzir visualizações voltadas à publicação, Matplotlib deve ser melhor, embora o Bokeh também oferece modos de criar gráficos estáticos.

Com essas diferenças em mente, enfatizarei ao longo da lição os aspectos interativos que tornam o Bokeh útil para explorar e disseminar dados históricos e que o diferenciam de outras bibliotecas, como o próprio Matplotlib.

## Seu primeiro plot

Primeiro, crie um novo arquivo chamado `meu_primeiro_plot.py` no mesmo diretório que `wwii_thor.csv` e depois abra-o num editor de texto. Adicionaremos linhas a esse arquivo para executá-lo.

```python
#meu_primeiro_plot.py
from bokeh.plotting import figure, output_file, show
```

Para implementar e utilizar o Bokeh, primeiro importamos alguns recursos básicos que serão necessários do módulo `bokeh.plotting`.

`figure` é o objeto principal que utilizaremos para criar plots. `figure` lida com a estilização dos plots, incluindo título, rótulos (*labels*), eixos e **grades ((*grids*) REVISAR ISSO AQUI)**, e expõe métodos par adicionar dados ao gráfico. A função `output_file` define como a visualização será renderizada (ou seja, para um arquivo html) e a função `show` será chamada quando o plot estiver pronta para ser apresentada. `show` informa ao Bokeh que todos os dados foram adicionados ao gráfico e que é hora de renderizá-lo.

```python
output_file('meu_primeiro_grafico.html')
```

Bokeh recomenda que a função `output_file`, para a qual passamos um nome de arquivo, seja chamada no início de seu script, imediatamente após as importações. Uma função de saída alternativa é a `output_notebook`, que é utilizada para mostrar gráficos em linha em um Jupyter Notebook. Para saber mais sobre como instalar e usar notebooks Jupyter, veja a [documentação do Jupyter](https://jupyter.readthedocs.io/en/latest/).

```python
x = [1, 3, 5, 7]
y = [2, 4, 6, 8]
```

Em seguida criaremos alguns dados para o gráfico. Dados no Bokeh podem assumir diferentes formatos, mas na sua forma mais simples, os dados são apenas uma lista de valores. Criamos uma lista para o nosso eixo x e outra para nosso eixo y.

Com o formato e os dados da nossa saída fixados, podemos instanciar uma `figure` e adicionar os dados a ela.

```python
p = figure()

p.circle(x, y, size=10, color='red', legend='círculo')
p.line(x, y, color='blue', legend='linha')
p.triangle(y, x, color='gold', size=10, legend='triângulo')
``` 

{% include alert.html text="`p` é um nome de variável comum para um objeto `figure`, uma vez que uma figura é um tipo de plot." %}

Após instanciar a figura, chamamos os métodos `circle`, `line` e `triangle` para plotar nossos dados. Esses tipos de métodos são conhecidos como *métodos de glifo* (*glyph method*). O termo *glifo* no Bokeh se refere às linhas, círculos, barras e outros formatos que são adicionados aos plots para apresentar dados.

Se quiséssemos, poderíamos continuar adicionando glifos ao plot! Há muitos outros glifos além de `circle`, `line` e `triangle`, incluindo `asterisk`, `circle_cross`, `circle_x`, `cross`, `diamond`, `diamond_cross`, `inverted_triangle`, `square`, `square_cross`, `square_x` e `x`.

Ao chamar por um método de glifo, o mínimo que deve ser feito é passar os dados que gostaríamos de plotar, mas frequentemente podemos adicionar argumentos de estilo. Aqui, definimos um tamanho, uma cor e um nome de legenda para cada glifo.

```python
p.legend.click_policy='hide'
``` 

Também adicionaremos nosso primeiro trecho de código que traz alguma interatividade ao plot. Ao definir uma `click_policy` na nossa legenda, um usuário pode agora clicar em cada entrada de legenda (por exemplo, círculo, linha, triângulo) para mostrar/ocultar esses dados! O `click_policy` também pode ser configurado para `mute` ao invés de `hide`. Isso diminuiria a saturação da cor daqueles dados ao clicar, em vez de ocultá-los completamente.

```python
show(p)
```

Chamar pelo `show` e passar a `figure` instanciada produzirá os resultados em nosso arquivo html. Agora vamos executar este código! 

Na sua linha de comando, tenha certeza de que está no diretório onde você salvou o arquivo e depois execute este arquivo com o comando `python`.

```
python meu_primeiro_plot.py
``` 
{% include figure.html filename="visualizando-com-bokeh-1.png" caption="Plotando um Único Glifo" %}

Um navegador web surgirá mostrando o arquivo html com a sua visualização. Os círculos vermelhos, linha azul e triângulos amarelos são resultado dos métodos de glifo que chamamos. Clicar na legenda no canto superior direito mostrará/ocultará cada tipo de glifo. Observe que o Bokeh controlou automaticamente a criação das **linhas de grade (REVISAR ISSO AQUI)** e rótulos de escala.

No lado direito, a barra de ferramentas padrão também é exibida. As ferramentas incluem arrastar, zoom de caixa, zoom de roda, salvar, redefinir e ajuda. Usando essas ferramentas, um usuário pode fazer deslocamentos ao longo do gráfico ou ampliar porções interessantes dos dados. Como esta é uma página HTML independente, que inclui uma referência a BokehJS, ela pode ser imediatamente passada para um colega de trabalho para exploração ou postada na web. 

# Bokeh e Pandas: Explorando o Dataset WWII THOR 

No exemplo anterior, criamos manualmente duas listas curtas de Python para os nossos dados de x e y. O que acontece quando temos dados do mundo real com dezenas de milhares de linhas e dezenas de colunas armazenadas em um formato externo? Pandas, uma biblioteca de ciência de dados amplamente utilizada, é ideal para esse tipo de dado e se integra perfeitamente ao Bokeh para criar visualizações de dados interativas.

## Visão Geral de Pandas

Para os propósitos deste tutorial, serão abordadas apenas as funções básicas do Pandas que são necessárias para produzir nossas visualizações. [10 Minutes to Pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html) e [Lessons for New Pandas Users](https://pandas.pydata.org/pandas-docs/stable/getting_started/tutorials.html) são excelentes introduções que eu recomendaria para expandir seu conhecimento além do básico abordado aqui.

Pandas rapidamente se tornou a biblioteca Python *de facto* para fluxos de trabalhos de dados e ciência de dados; a integração com outras bibliotecas importantes de ciência de dados e aprendizado e máquinas só aumentou sua popularidade.[^1]. Pandas oferece funcionalidades para, de forma rápida e eficiente, ler, escrever e modificar conjuntos de dados para análise. Para fazer isso, Pandas oferece estruturas de dados que contêm diferentes dimensionalidades de dados. O `DataFrame` contém dados bidimensionais na forma de uma planilha com linhas e colunas. É por meio desse objeto que interagiremos com nosso conjunto de dados THOR sobre a Segunda Guerra Mundial. Vamos primeiro examinar o `DataFrame` do Pandas carregando nosso ficheiro .csv em uma estrutura desse tipo.

## Carregando Dados no Pandas

Para começar, crie um novo arquivo chamado `carregando_dados.py`.

```python
#carregando_dados.py
import pandas as pd

df = pd.read.csv('thor_wwii.csv')
print(df)
```

Começamos importando a biblioteca Pandas e depois chamando o `read_csv()` e passando um nome de ficheiro a ele. Note que a biblioteca Pandas é apelidada de *pd*. Esse apelido é uma convenção seguida na [documentação oficial do Pandas](https://pandas.pydata.org/pandas-docs/stable/) e é amplamente utilizada pela comunidade Pandas. Por essa razão, utilizarei o apelido *pd* ao longo do tutorial.

Nesse código, `read_csv()` cria um `DataFrame` que contém as linhas e colunas de nossos dados em csv. Por convenção, o nome de variável *df* é usado para representar o dataframe carregado em tutoriais e códigos básicos de exemplo. Há [muitos outros métodos](https://pandas.pydata.org/pandas-docs/stable/api.html#input-output) no Pandas para ler formatos de dados além de csv, como JSON, tabelas SQL, ficheiros Excel e HTML.

Ao executar o código, `print(df)` retornará uma representação resumida dos dados carregados.

```python
MSNDATE      THEATER    COUNTRY_FLYING_MISSION    ...     TONS_IC TONS_FRAG TOTAL_TONS
03/30/1941          ETO          GREAT BRITAIN    ...         0.0       0.0        0.0
11/24/1940          ETO          GREAT BRITAIN    ...         0.0       0.0        0.0
12/04/1940          ETO          GREAT BRITAIN    ...         0.0       0.0        0.0
12/31/1940          ETO          GREAT BRITAIN    ...         0.0       0.0        0.0

[178281 rows x 19 columns]
```
Isso mostra que temos 178.281 registros de missões com 19 colunas por registro. Para ver o que são as 19 colunas completas, podemos acessar o objeto `columns` do dataframe substituindo `print(df)` no código acima por:

```python
df.columns.tolist()
```

A saída deve ser semelhante a:

```python
['MSNDATE', 'THEATER', 'COUNTRY_FLYING_MISSION', 'NAF', 'UNIT_ID', 'AIRCRAFT_NAME', 'AC_ATTACKING', 'TAKEOFF_BASE', 'TAKEOFF_COUNTRY', 'TAKEOFF_LATITUDE', 'TAKEOFF_LONGITUDE', 'TGT_COUNTRY', 'TGT_LOCATION', 'TGT_LATITUDE', 'TGT_LONGITUDE', 'TONS_HE', 'TONS_IC', 'TONS_FRAG', 'TOTAL_TONS']
```

Alguns desses nomes de coluna são autoexplicativos, mas vale a pena apontar o seguinte: MSNDATE (data da missão), NAF (número da força aérea responsável pela missão), AC_ATTACKING (número de aeronaves), TONS_HE (explosivos), TONS_IC (dispositivos incendiários), TONS_FRAG (bombas de fragmentação).

Quando se trata de acessar dados dentro de um `DataFrame`, neste tutorial usamos uma abordagem básica: indexação. Aqui, para acessar uma única coluna, passamos uma string para o indexador do nosso dataframe: por exemplo, `df['MSNDATE']`. Para acessar múltiplas colunas, passamos uma lista de nomes para o indexador do nosso dataframe: por exemplo, `df[['MSNDATE', 'THEATER']]`.

## O Bokeh ColumnDataSource

Agora que aprendemos como criar um gráfico Bokeh e como carregar dados tabulares no Pandas, é hora de aprendermos como conectar um `DataFrame` Pandas a visualizações Bokeh. O objeto Bokeh `ColumnDataSource` oferece essa integração.

O construtor de objetos aceita um `DataFrame` Pandas como argumento. Depois de criado, o `ColumnDataSource` pode ser passado a métodos de glifo através do parâmetro `source`, ao mesmo tempo que outros parâmetros, como os nossos dados x e y, podem então referenciar nomes de coluna em nossa fonte. Vamos ver um exemplo disso.

Usando o dataset THOR, criaremos um gráfico de dispersão do número de aeronaves de ataque versus as toneladas de munições lançadas. Usaremos um novo arquivo chamado `column_datasource.py` para fazer isso. Também aproveitaremos a oportunidade para aprender o recurso de foco interativo do Bokeh.

```python
#column_datasource.py
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool

output_file('columndatasource_example.html')

df = pd.read_csv('thor_wwii.csv')
```

Aqui, importamos o Pandas, o objeto `figure` e funções básicas do `bokeh.plotting`, e o objeto `ColumnDataSource` do `bokeh.models`. Também expandiremos nosso conhecimento sobre interações nesse exemplo adicionando um recurso de foco que é facilitado pelo `HoverTool`.

Em seguida, configuramos imediatamente nosso arquivo de saída seguindo as práticas recomendadas pelo Bokeh. Finalmente, chamamos o método `read_csv()` do Pandas para carregar nosso csv em um `DataFrame`.

```python
amostra = df.sample(50)
fonte = ColumnDataSource(amostra)
```

Uma vez que não queremos plotar as mais de 170.000 linhas no nosso gráfico de dispersão (o que iria requerer um tempo de processamento mais longo para ser gerado e criaria um plot confuso em função do volume de dados sobrepostos), pegamos uma amostra aleatória de 50 linhas usando o método `sample` de dataframes. Depois passamos essa amostra ao construtor `ColumnDataSource` e o armazenamos em uma variável chamada `fonte`.

```python
p = figure()
p.circle(x='TOTAL_TONS', y='AC_ATTACKING',
         source=fonte,
         size=10, color='green')
```

Em seguida, criamos nosso objeto `figure` e chamamos o método de glifo `circle` para plotar nossos dados. Aqui é onde a variável `fonte`, que armazena nosso `ColumnDataSource`, entra em jogo. Ela é passada como nosso argumento `source` ao método de glifo e os nomes de coluna contendo o número de aeronaves atacantes (AC_ATTACKING) e toneladas de munições lançadas (TOTAL_TONS) são passadas como nossos argumentos `x` e `y`.

Curiosamente, quando usamos um `ColumnDataSource` não estamos limitados a usar somente nomes de coluna para parâmetros `x` e `y`. Também podemos passar um nome de coluna para outros parâmetros como `size`, `line_color` ou `fill_color`. Isso permite que as opções de estilo sejam determinadas por colunas na própria fonte de dados! Caso queira ver isso em ação, no código acima, altere `size = 10` para `size = 'TONS_HE'`. O tamanho de cada ponto refletirá as toneladas de explosivos usados.

{% include alert.html text="Ao longo do tutorial, costumo passar argumentos por nome, onde eles poderiam ser transmitidos de forma mais sucinta por posição. Isso é útil, na minha opinião, para o leitor acompanhar quais argumentos estão sendo passados." %}

Em seguida, adicionamos um título e rotulamos nossos eixos.

```python
p.title.text = 'Aeronave de Ataque e Munições Lançadas'
p.xaxis.axis_label = 'Toneladas de Munições Lançadas'
p.yaxis.axis_label = 'Número de Aeronaves de Ataque'
```

Podemos também, neste estágio, aprender um pouco mais sobre a forte natureza interativa e personalizável dos gráficos Bokeh. Em nosso primeiro gráfico Bokeh, vimos a barra de ferramentas Bokeh padrão, mas o Bokeh nos permite personalizar nosso gráfico adicionando novas ferramentas interativas a ele.

```python
hover = HoverTool()
hover.tooltips=[
    ('Attack Date', '@MSNDATE'),
    ('Attacking Aircraft', '@AC_ATTACKING'),
    ('Tons of Munitions', '@TOTAL_TONS'),
    ('Type of Aircraft', '@AIRCRAFT_NAME')
]

p.add_tools(hover)

show(p)
```

Bokeh dá suporte a [várias ferramentas de plotagem](https://docs.bokeh.org/en/latest/docs/user_guide/tools.html), mas introduzo `HoverTool` aqui porque é particularmente útil para exploração e interação de dados. `HoverTool` permite que você defina uma propriedade `tooltipis` que recebe uma lista de [tuplas](https://www.w3schools.com/python/python_tuples.asp). A primeira parte da tupla é um nome de exibição e a segunda é um nome de coluna de seu `ColumnDataSource` precedido por `@`. Depois de instanciar essa ferramenta, nós a adicionamos ao gráfico usando o método `add_tool`. Logo veremos como isso se parece na prática.

Finalmente, nos certificamos de adicionar a linha para mostrar o gráfico, `show(p)`. Agora podemos executar `column_datasource.py` e interagir com nossos dados no navegador.

{% include figure.html filename="visualizando-com-bokeh-2.png" caption="Plotagem com ColumnDataSource e mais opções de estilização" %}

Note que, uma vez que estamos obtendo uma amostra aleatória dos dados, nosso plot será diferente a cada vez que o código for executado.

No topo e ao longo dos eixos do gráfico, vemos os rótulos que adicionamos. Também existe uma nova ferramenta na barra de ferramentas. Esta é a ferramenta de foco que adicionamos. Para vê-lo em ação, passe o mouse sobre qualquer ponto de dados no gráfico de dispersão. Uma janela aparecerá mostrando as colunas que definimos em nossa propriedade `tooltip`!

Antes de passar para a próxima seção da lição, tente retornar ao exemplo acima e adicionar/remover outras variáveis e alterar os nomes de exibição.

# Dados Categóricos e Gráficos de Barra: Munições Lançadas por País

No exemplo anterior, plotamos dados quantitativos. Frequentemente, porém, queremos representar graficamente dados categóricos. Dados categóricos, ao contrário dos quantitativos, são dados que podem ser divididos em grupos, mas que não têm necessariamente um aspecto numérico. Por exemplo, enquanto sua altura seja numérica, a cor do seu cabelo é categórica. No que diz respeito ao nosso dataset, elementos como o país atacante contêm dados categóricos, enquanto elementos como o peso das munições contêm dados quantitativos.

Nesta seção, aprenderemos como utilizar dados categóricos como nossos valores do eixo x no Bokeh e como usar o método de glifo `vbar` para criar um gráfico de barras verticais (o método de glifo `hbar` funciona de forma semelhante para criar um gráfico de barras horizontais). Além disso, aprenderemos como preparar dados categóricos no Pandas através do agrupamento de dados. Também expandiremos nosso conhecimento sobre estilização com Bokeh e sobre a ferramenta de foco.

Para trabalhar com essas informações, criaremos um gráfico de barras que mostra o total de toneladas de munições lançadas por cada país listado em nosso csv.

Começamos criando um novo arquivo chamado `municoes_por_pais.py` e adicionando algum código inicial.

```python
#municoes_por_pais.py
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.models.tools import HoverTool

from bokeh.palettes import Spectral5
from bokeh.transform import factor_cmap
output_file('municoes_por_pais.html')

df = pd.read_csv('thor_wwii.csv')
```
Primeiro, importamos a biblioteca Pandas e os elementos básicos do Bokeh (por exemplo, `figure`, `output_file`, `show` e `ColumnDataSource`). Também fazemos duas novas importações: `Spectral5` é uma paleta de cinco cores pré-fabricada, uma das muitas [paletas de cores pré-fabricadas]((https://bokeh.pydata.org/en/latest/docs/reference/palettes.html)) do Bokeh, e `factor_cmap` é um método auxiliar para mapear cores para barras em gráficos de barras.

Após as importações, definimos nosso `output_file` e carregamos o ficheiro thor_wwii.csv em um `DataFrame`.

Agora precisamos ir dos mais de 170.000 registros de missões individuais para um registro por país atacante com o total de munições lançadas.

```python
agrupado = df.groupby('COUNTRY_FLYING_MISSION')['TOTAL_TONS', 'TONS_HE', 'TONS_IC', 'TONS_FRAG'].sum()
```

Pandas nos permite fazer isso numa única linha de código utilizando o método de dataframe `groupby`. Esse método aceita uma coluna para agrupar os dados e um ou mais métodos de agregação que informam ao Pandas como agrupar os dados. O resultado é um novo dataframe.

Vamos pegar um pedaço de cada vez. O `groupby('COUYTRY_FLYING_MISSION')` define a coluna que estamos agrupando. Em outras palavras, isso diz que queremos que o dataframe resultante tenha uma linha por entrada única na coluna `COUNTRY_FLYING_MISSION`. Como não nos importamos em agregar todas as 19 colunas do dataframe, escolhemos apenas as colunas que dizem respeito às toneladas de munição através do indexador `['TOTAL_TONS', 'TONS_HE', 'TONS_IC', 'TONS_FRAG']`. Por fim, usamos o método `sum` para permitir que o Pandas saiba como agregar todas as diferentes linhas. Existem outros métodos de agregação, como `count`, `mean`, `max` e `min`.

Se você executar `print(agrupado)`, verá que o Pandas agrupou pelos cinco países em nosso dataset e somou o total de toneladas lançadas por cada um. Também é possível perceber que o dataset tem alguns problemas: A África do Sul e a Nova Zelândia lançaram mais explosivos do que a coluna do total de toneladas. Problemas como esse são típicos de ggrandes conjuntos de dados criados manualmente e esse é um ótimo lembrete da importância explorar e visualizar seus dados antes de criar resultados de pesquisa.

```
                        TOTAL_TONS     TONS_HE     TONS_IC  TONS_FRAG
COUNTRY_FLYING_MISSION
AUSTRALIA                   479.89      453.90      13.600      18.64
GREAT BRITAIN           1112598.95   868277.23  209036.158    1208.00
NEW ZEALAND                2629.06     4263.70     166.500       0.00
SOUTH AFRICA                 11.69       15.00       0.000       0.00
USA                     1625487.68  1297955.65  205288.200  127655.98

```

Para plotar esses dados, vamos converter para quilotons dividindo por 1000.

```python
agrupado = agrupado / 1000
```

Essa é uma conveniência que continuaremos a usar em exemplos futuros.

```python
fonte = ColumnDataSource(agrupado)
paises = fonte.data['COUNTRY_FLYING_MISSION'].tolist()
p = figure(x_range=paises)
```

Agora, precisamos fazer um `ColumnDataSource` de nossos dados agrupados e criar uma `figure`. Como nosso eixo x listará os cinco países (em vez de dados numéricos), precisamos dizer à figura como lidar com o eixo x;

Para fazer isso, criaremos uma lista de países a partir do nosso objeto fonte, usando `fonte.data` e o nome da coluna como chave. A lista de países é passada como `x_range` ao nosso construtor `figure`. Já que esta é uma lista de dados textuais, a figura sabe que o eixo x é categórico e também sabe quais valores possíveis nosso intervalo de x pode assumir (ou seja, AUSTRALIA, GREAT BRITAIN, etc.).

```python
mapa_de_cores = factor_cmap(field_name='COUNTRY_FLYING_MISSION',
                    palette=Spectral5, factors=paises)

p.vbar(x='COUNTRY_FLYING_MISSION', top='TOTAL_TONS', source=source, width=0.70, color=mapa_de_cores)

p.title.text ='Munições Lançadas por País Aliado'
p.xaxis.axis_label = 'País'
p.yaxis.axis_label = 'Quilotons de Munição'
```

Agora, plotamos nossos dados como barras coloridas individualmente e adicionamos rótulos básicos. Para colorir nossas barras, usamos a função auxiliar `factor_cmap`. Isso cria um mapa de cores especial que corresponde a uma cor individual para cada categoria (ou seja, o que o Bokeh chama de *factor*). O mapa de cores é então passado como argumento de cores para o nosso método de glifo `vbar`.

Para os dados no nosso método de glifo, estamos passando a fonte e mais uma vez referenciando o nome das colunas. Ao invés de usar o parâmetro `y`, porém, o método `vbar` recebe um parâmetro `top`. Um parâmetro `bottom` pode igualmente ser especificado, mas, se deixado de fora, seu valor padrão é 0.

```python
hover = HoverTool()
hover.tooltips = [
    ("Totais", "@TONS_HE Explosivo / @TONS_IC Incendiário / @TONS_FRAG Fragmentação")]

hover.mode = 'vline'

p.add_tools(hover)

show(p)
```

Adicionamos uma ferramenta de foco novamente, mas agora vemos que poodemos usar várias variáveis de dados em uma única linha e adicionar nosso próprio texto para que o pop-up de foco liste os quilotons de cada tipo de explosivo. O `hover.mode` é novo. Existem três modos para a ferramenta hover: `mouse`, `vline` e `hline`. Eles informam à ferramenta de foco quando mostrar o pop-up. `mouse` é o valor padrão e mostra um pop-up quando diretamente sobre um glifo. `vline` e `hline` informam ao pop-up para surgir quando uma linha vertical ou horizontal cruza um glifo. Com `vline` definido aqui, sempre que o mouse passar por uma linha vertical imaginária que se estende a partir de cada barra, um pop-up será exibido.

{% include figure.html filename="visualizando-com-bokeh-3.png" caption="Um Gráfico de Barras com Dados Categóricos e Coloração" %}

{% include alert.html text="Caso tenha tempo, vale a pena explorar as [paletas de cores](https://bokeh.pydata.org/en/latest/docs/reference/palettes.html) do Bokeh. No exemplo acima, tente reescrever o código para usar algo diferente de `Spectral5`, como `Inferno5` ou `RdGy5`. Para dar um passo a diante, você pode tentar usar paletas integradas em qualquer exemplo que use cores." %}

# Gráficos de Barras Empilhadas e Dados de Subamostragem: Tipos de Munições Lançadas por País

Como o gráfico anterior mostra que os Estados Unidos e a Grã-Bretanha respondem pela esmagadora maioria dos bombardeios, agora nos concentramos nesses dois países e aprendemos como fazer um gráfico de barras empilhadas que mostra os tipos de munições que cada país usou.

Começaremos um novo arquivo chamado `municoes_por_pais_empilhadas.py`.

```python
#municoes_por_pais_empilhadas.py
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral3
output_file('types_of_munitions.html')

df = pd.read_csv('thor_wwii.csv')
```

Além das nossas importações padrão, dessa vez utilizaremos uma paleta Spectral de três cores, uma cor para cada tipo de explosivo (Explosivo, Incendiário e Fragmentação).

```python
filtro = df['COUNTRY_FLYING_MISSION'].isin(('USA','GREAT BRITAIN'))
df = df[filtro]
```

Uma vez que o eixo x é categórico mais uma vez, precisaremos agrupar e agregar nossos dados. Dessa vez, porém, precisamos excluir quaisquer registros que não tenham um COUNTRY_FLYING_MISSION como um valor de GREAT BRITAIN ou USA. Para fazer isso, filtramos nosso dataframe.

Para cada linha em `df`, a função `isin` verifica se COUNTRY_FLYING_MISSION possui um valor de USA ou GREAT BRITAIN. Caso tenha, o valor correspondente na variável `filtro` é `True` e, caso contrário, o valor é `False`.

Quando aplicado ao nosso dataframe através do `df[filtro]`, um novo dataframe é criado, no qual as linhas com valor `True` são mantidas e linhas com valor `False` são discartadas. Após a aplicação do filtro, a execução de `df.shape` mostra que há 125.526 linhas sobrando do valor original de 178.281.

```python
agrupado = df.groupby('COUNTRY_FLYING_MISSION')['TONS_IC', 'TONS_FRAG', 'TONS_HE'].sum()

#convertemos para quilotons novamente
agrupado = agrupado / 1000
```

Agora que já reduzimos nosso dataframe para mostrar somente os registros dos Estados Unidos e Grã-Bretanha, agrupamos nossos dados com o `groupy` e agregamos as três colunas que contêm tipos de bombas com o `sum`.

```python
fonte = ColumnDataSource(agrupado)
paises = fonte.data['COUNTRY_FLYING_MISSION'].tolist()
p = figure(x_range=paises)
```

Como no exemplo anterior, criamos um objeto fonte a partir dos nossos dados agrupados e garantimos que nossa figura use dados categóricos no eixo x definindo o `x_range` com a lista de países.

```python
p.vbar_stack(stackers=['TONS_HE', 'TONS_FRAG', 'TONS_IC'],
             x='COUNTRY_FLYING_MISSION', source=fonte,
             legend = ['Explosivo', 'Fragmentação', 'Incendiário'],
             width=0.5, color=Spectral3)
```

Para criar o gráfico de barras empilhadas, chamamos o método de glifo `vbar_stack`. Ao invés de passar um único nome de coluna ao parâmetro `y`, passamos uma lista de nomes de coluna como `stackers`. A ordem dessa lista determina a ordem pela qual as colunas serão empilhadas de baixo para cima (depois de trabalhar neste exemplo, tente mudar a ordem das colunas para ver o que acontece). O argumento `legend` fornece texto para cada empilhador e a paleta `Spectral3` fornece cores para cada um deles.

```python
p.title.text ='Tipos de Munições Lançadas por País Aliado'
p.legend.location = 'top_left'

p.xaxis.axis_label = 'País'
p.xgrid.grid_line_color = None	#remove as linhas de grade de x

p.yaxis.axis_label = 'Quilotons de Munição'

show(p)
```

Adicionamos um estilo básico e rotulagem e, em seguida, produzimos o gráfico.

{% include figure.html filename="visualizando-com-bokeh-4.png" caption="Um Gráfico de Barras Empilhadas com Dados Categóricos e Coloração" %}

# Séries Temporais e Anotações: Operações de Bombardeio ao longo do Tempo

Vamos agora explorar um pouco mais o uso de explosivos incendiários e de fragmentação, vendo se há alguma tendência em seu uso ao longo do tempo em comparação com o total de munições lançadas. Como você já teve algum tempo para se acostumar com a sintaxe do Bokeh, vamos mergulhar direto com um exemplo de código completo em um novo arquivo chamado `minha_primeira_serie_temporal.py`.

```python
#minha_primeira_serie_temporal.py
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.palettes import Spectral3
output_file('simple_timeseries_plot.html')

df = pd.read_csv('thor_wwii.csv')

#certifique-se de que MSNDATE tenha um formato de data
df['MSNDATE'] = pd.to_datetime(df['MSNDATE'], format='%m/%d/%Y')

agrupado = df.groupby('MSNDATE')['TOTAL_TONS', 'TONS_IC', 'TONS_FRAG'].sum()
agrupado = agrupado/1000

fonte = ColumnDataSource(agrupado)

p = figure(x_axis_type='datetime')

p.line(x='MSNDATE', y='TOTAL_TONS', line_width=2, source=fonte, legend='Todas as munições')
p.line(x='MSNDATE', y='TONS_FRAG', line_width=2, source=fonte, color=Spectral3[1], legend='Fragmentação')
p.line(x='MSNDATE', y='TONS_IC', line_width=2, source=fonte, color=Spectral3[2], legend='Incendiária')

p.yaxis.axis_label = 'Quilotons de Munições Lançadas'

show(p)
```

Reserve um minuto para examinar com atenção este código e ver o que você reconhece. Dois itens devem se destacar como novos.

Primeiro, a instrução `df['MSNDATE'] = pd.to_datetime(df['MSNDATE'], format='%m/%d/%Y')` garante que nossa coluna MSNDATE seja uma data. Isso é importante porque muitas vezes os dados carregados de um ficheiro csv não serão digitados corretamente como data. Fornecer um argumento `format` não é obrigatório, mas isso acelera significativamente o processo.

Em segundo lugar, passamos o argumento `x_axis_type='datetime'` ao nosso construtor `figure` para informá-lo que nossos dados do eixo x serão datas. Caso contrário, Bokeh funciona perfeitamente com os dados de tempo, como qualquer outro tipo de dados numéricos!

Olhando para a saída, porém, você pode notar um grande problema.

{% include figure.html filename="visualizando-com-bokeh-5.png" caption="Um Gráfico Básico de Série Temporal" %}

Esses dados são voláteis e difíceis de ler porque estão muito **desagregados (REVER ISSO AQUI)** para as nossas necessidades. Ter dados diários ao longo de cinco anos é ótimo, mas traçá-los dessa forma obscurece as tendências dos dados. Para plotar dados de série temporal com sucesso e procurar tendências de longo prazo, precisamos de uma maneira de mudar a escala de tempo que estamos olhando para que, por exemplo, possamos plotar dados resumidos por semanas, meses ou anos.

Felizmente, Pandas oferece uma maneira rápida e fácil de fazer isso. Ao modificar uma única linha de código no exemplo acima, podemos *reamostrar* nossos dados de série temporal para qualquer unidade de tempo válida.

## Reamostragem de Dados de Série Temporal

A reamostragem de dados de série temporal pode envolver upsampling (criar mais registros) ou downsampling (criando menos registros). Por exemplo, uma lista de temperaturas diárias pode ser aumentada para uma lista de temporaturas de hora em hora ou reduzida para uma lista de temperaturas semanais. Estaremos fazendo somente um downsampling neste tutorial, mas upsampling é muito útil quando você está tentando combinar um dataset medido esporadicamente com um que é medido mais periodicamente.

Para reamostrar nossos dados, usamos o objeto `Grouper` do Pandas, ao qual passaremos o nome da coluna que contém as nossas datas e um código representando a frequência desejada para a reamostragem. No caso dos nossos dados, o comando `pd.Grouper(key='MSNDATE', freq='M')` será utilizado para reamostrar nossa coluna MSNDATE por *M*onth (Mês). Da mesma forma, poderíamos reamostrar por *W*eek (Semana), *Y*ear (Ano), *H*our (hora) e [assim por diante](http://pandas.pydata.org/pandas-docs/stable/timeseries.html#offset-aliases). Essas designações de frequência também podem ser precedidas de números de forma que, por exemplo, `freq = '2W'` reamostra em intervalos de duas semanas!

Para completar o processo de reamostragem e plotar nossos dados, passamos o objeto `Grouper` acima para a nossa função `groupy` no lugar do nome bruto da coluna. A instrução `groupy` do exemplo de código anterior agora deve ter a seguinte aparência:

``` python
grouped = df.groupby(pd.Grouper(key='MSNDATE', freq='M'))['TOTAL_TONS', 'TONS_IC', 'TONS_FRAG'].sum()
```

Executando novamente o exemplo de código acima produzirá um gráfico muito mais limpo e com tendências óbvias. O gráfico agora mostra quatro pontos de interesse:

- Primeiro, tanto na primavera de 1944 quando na de 1945, a escala das operações de bombardeio dos Aliados atingiu maior intensidade;
- Segundo, há um pico menor no verão de 1945 durante a aceleração dos bombardeios contra os japoneses após a rendição da Alemanha;
- Terceiro, há quatro picos no uso de armas incendiárias aparecem que poderiam ser mais exploradas;
- Quarto e último, há alguns pequenos picos no uso de bombas de fragmentação, cujo uso para efetivamente após a rendição da Alemanha.

{% include figure.html filename="visualizando-com-bokeh-6.png" caption="Um Gráfico de Série Temporal com Dados Reamostrados para Meses" %}

## Anotando Tendências em Gráficos

Vamos examinar mais de perto agora os bombardeios na Europa em 1944 e 1945 para ver quais tendências existem com munições de fragmentação e incendiárias. Também apontaremos algumas dessas tendências em nosso gráfico com anotações. Para fazer isso, vamos filtrar nosso conjunto de dados para trabalharmos apenas com bombardeios no Teatro Europeu de Operações (*European Theater of Operations - ETO*), reamostrar os dados em intervalos de um mês e, em seguida, plotar os resultados da mesma maneira que antes.

```python
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
```

{% include figure.html filename="visualizando-com-bokeh-7.png" caption="Um Gráfico de Série Temporal do ETO com Dados Reamostrados para Meses" %}

Alguns padrões emergem dos dados do ETO. Em primeiro lugar, vemos uma escalada muito clara dos bombardeios gerais que levaram até 6 de junho de 1994 e uma queda notável durante o inverno de 1944/1945. Munições incendiárias mostram três picos e confirmam que o quarto pico visto no exemplo anterior foi direcionado ao bombardeio do Japão após a rendição da Alemanha. O padrão das bombas de fragmentação é mais difícil de ler, mas agora está claro que elas só foram usadas seriamente no Teatro Europeu após o Dia D.

{% include alert.html text="Tente reamostrar esses dados usando qualquer uma das [frequências de tempo do Pandas](http://pandas.pydata.org/pandas-docs/stable/timeseries.html#offset-aliases) para ver quais outras tendências podem surgir. Lembre-se de que você também pode prefaciar essas tendências com números (por exemplo, se você estiver trabalhando com dados históricos do mercado de ações, o 2Q fornecerá dados bimestrais." %}

Como estabelecemos que o 6 de junho de 1944 e o inverno de 1944/1945 marcam mudanças nos padrões de bombardeio no ETO, vamos destacar essas tendências usando os recursos de anotação do Bokeh.

Para fazer isso, criaremos um `BoxAnnotation` e, em seguida, adicioná-los à nossa figura antes de mostrá-la. Primeiro, precisamos adicionar uma instrução import adicional ao nosso código.


```python
from bokeh.models import BoxAnnotation
```

Para criar a caixa, primeiro precisamos determinar suas coordenadas. Coordenadas para anotações do Bokeh podem ser absolutas (ou seja, posicionadas usando unidades de tela), o que significa que elas podem sempre ficar em um lugar específico, ou podem ser posicionadas em relação aos dados. Nossas anotações serão todas posicionadas usando coordenadas de dados.

```python
caixa_esquerda = pd.to_datetime('6-6-1944')
caixa_direita = pd.to_datetime('16-12-1944')
```

A esquerda da caixa será 6 de junho de 1994 (Dia D) e à direita da caixa escolheremos o primeiro dia da Batalha de Bulge: 16 de dezembro de 1994. Neste caso, as datas seguem um formato mês-dia_ano, mas `to_datetime` também funciona com [os formatos dia-primeiro (day-first) e ano-primeiro (year-first)](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.to_datetime.html).

Passamos essas coordenadas ao construtor `BoxAnnotation` junto com alguns argumentos de estilização. Depois, o adicionamos à nossa figura usando o método `add_layout()`.

```python
caixa = BoxAnnotation(left=caixa_esquerda, right=caixa_direita,
                    line_width=1, line_color='black', line_dash='dashed',
                    fill_alpha=0.2, fill_color='orange')

p.add_layout(caixa)
```
{% include figure.html filename="visualizando-com-bokeh-8.png" caption="Um Gráfico de Série Temporal do ETO com Anotações Adicionadas" %}

{% include alert.html text="Tente criar um gráfico semelhante para o Teatro de Operações do Pacífico (*Pacific Theater os Operations - PTO*). Anote a invasão de Iwo Jima (19 de fevereiro de 1945) e o anúncio de rendição do Japão (15 de agosto de 1945)." %}

# Dados Espaciais: Mapeando Localização de Alvos

Nesta parte final da lição, veremos os componentes espaciais das bombas de fragmentação.

Bokeh oferece [provedores de blocos integrados (built-in tile providers)](https://bokeh.pydata.org/en/latest/docs/reference/tile_providers.html) que renderizam mapas básicos do mundo. Eles estão contidos no módulo `bokeh.tile_providers`. Para esse exemplo, usaremos o CartoDB Tile Service (CARTODBPOSITRON).

Também utilizaremos funções importadas da biblioteca `pyproj`. Já que nossas coordenadas estão armazenadas como latitude e longitude, definiremos uma função personalizada para convertê-las antes do mapeamento. Observe que, embora Bokeh seja neutro em relação ao sistema de coordenadas, ele usa a projeção Web Mercator para mapeamento, um padrão encontrado em provedores de web tiles. O assunto de sistemas de coordenadas e projeções está fora do escopo deste tutorial, mas o leitor interessado encontrará muitos recursos da web úteis sobre esses tópicos.

{% include alert.html text="Se o seu próprio dataset tiver nomes de lugares, mas não de latitude e longitude, não se preocupe! Você pode encontrar maneiras de obter facilmente coordenadas de nomes de lugares na lição do Programming Historian [Geocoding Historical Data using QGIS](/lessons/geocoding-qgis) ou [Web Mapping with Python and Leaflet](/lessons/mapping-with-python-leaflet#geocoding-with-python).." %}

```python
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
```

As importações padrão e nossa função e conversão estão definidas. Em seguida, carregamos nossos dados e aplicamos nossa função de conversão para criar novas colunas E e N que armazenam nosso We Mercator easting e northing.

```python
agrupado = df.groupby(['E', 'N'])['TONS_IC',
'TONS_FRAG'].sum().reset_index()

filter = agrupado['TONS_FRAG']!=0
agrupado = agrupado[filter]

fonte = ColumnDataSource(agrupado)
```

Considerando que um único alvo pode aparecer em vários registros, precisamos agrupar os dados por E e N para obter localizações únicas. Caso contrário, mapearíamos o mesmo destino sempre que ele aparecesse em um registro.

A função `reset_index` aplicada após a agregação é uma novidade. Por padrão, quando Pandas agrupa essas duas colunas, ele fará com que E e N sejam os índices de cada linha no novo dataframe. Uma vez que queremos que E e N permaneçam como colunas normais para mapeamento, chamamos `reset_index`.

```python
esquerda = -2150000
direita = 18000000
inferior = -5300000
superior = 11000000

p = figure(x_range=Range1d(esquerda, direita), y_range=Range1d(inferior, superior))
```
Para definir os limites do nosso mapa, definiremos um valor mínimo e máximo para o `x_range` e `y_range` do nosso gráfico. Usamos o objeto `Range1D`, que representa dados unidimensionais no Bokeh.

```python
provedor = get_provider('CARTODBPOSITRON')
p.add_tile(provedor)
p.circle(x='E', y='N', source=fonte, line_color='grey', fill_color='yellow')

p.axis.visible = False

show(p)
```

Por fim, chamamos `add_tile` e passamos o provedor de tile que importamos. Em seguida, usamos métodos de glifo como em qualquer outro gráfico. Aqui, chamamos `circle` e passamos as colunas easting e northing como nossos dados x e y.

{% include figure.html filename="visualizando-com-bokeh-9.png" caption="Um Mapa com Localização de Alvos" %}

Tendo plotado quais alvos na Europa e na Ásia foram bombardeados com bombas de fragmentação, podemos agora começar a examinar os padrões de destruição com mais detalhes. No código acima, também somamos bombas incendiárias. Tente alterar o código para criar um mapa desses alvos.

# Bokeh como uma Ferramenta de Visualização

A força do Bokeh como uma ferramenta de visualização está na sua capacidade de mostrar diferentes tipos de dados de maneira interativa e amigável para a web. Este tutorial apenas arranhou a superfície dos recursos do Bokeh e o leitor é encorajado a se aprofundar no funcionamento da biblioteca. Um ótimo lugar para começar é a [galeria do Bokeh](https://bokeh.pydata.org/en/latest/docs/gallery.html), onde você pode ver uma variedade de visualizações e decidir como aplicar essas técnicas a seus próprios dados. Se você estiver mais inclinado a mergulhar direto em outros exemplos de código, o [notebook online](https://mybinder.org/v2/gh/bokeh/bokeh-notebooks/master?filepath=tutorial%2F00%20-%20Introduction%20and%20Setup.ipynb) do Bokeh é um excelente lugar para começar!

# Recursos Adicionais

- [Guia de Usuário do Bokeh](https://bokeh.pydata.org/en/latest/docs/user_guide.html)
- [Galeria do Bokeh](https://bokeh.pydata.org/en/latest/docs/gallery.html)
- [Documentação do Pandas](https://pandas.pydata.org/pandas-docs/stable/index.html)
- [Cheat Sheet do Pandas](https://www.kdnuggets.com/2017/01/pandas-cheat-sheet.html)
- [Cheat Sheet do Bokeh](https://www.kdnuggets.com/2017/03/bokeh-cheat-sheet.html)


[^1]: David Robinson, 'Why is Python Growing so Quickly?', *Stack Overflow Blog*, 14 September 2017 [https://stackoverflow.blog/2017/09/14/python-growing-quickly/](https://stackoverflow.blog/2017/09/14/python-growing-quickly/)