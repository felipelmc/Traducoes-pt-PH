# LEMBRAR DE REVISAR TUDO E TRADUZIR TAMBÉM O JUPYTER NOTEBOOK TAMBÉM

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


# Sumário

{% include toc.html %}

# Visão geral

A capacidade de carregar dados brutos, amostrá-los e, em seguida, explorar e apresentá-los visualmente é uma habilidade valiosa entre as disciplinas. Neste tutorial, você aprenderá como fazer isso em Python utilizando as bibliotecas Bokeh e Pandas. Mais especificamente, trabalharemos visualizando e explorando aspectos dos bombardeiros da Segunda Guerra Mundial conduzidos por potências Aliadas.

Ao final dessa lição, você será capaz de:

- Carregar dados tabulares do formato CSV;
- Performar o básico de manipulação de dados, tal como agregar e sub-amostrar dados brutos;
- Visualizar dados quantitativos, categóricos e geográficos para exibição na web;
- Adicionar diversos tipos de interação às suas visualizações;

Para alcançar esses objetivos, trabalharemos com uma variedade de exemplos de visualização usando THOR, dataset (conjunto de dados) que descreve as operações históricas de bombardeio.

## O Dataset THOR sobre a Segunda Guerra Mundial

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

    
         active environment : base
        active env location : /opt/anaconda3
                shell level : 1
           user config file : /Users/felipe/.condarc
     populated config files : /Users/felipe/.condarc
              conda version : 4.9.2
        conda-build version : 3.20.5
             python version : 3.8.5.final.0
           virtual packages : __osx=10.16=0
                              __unix=0=0
                              __archspec=1=x86_64
           base environment : /opt/anaconda3  (writable)
               channel URLs : https://repo.anaconda.com/pkgs/main/osx-64
                              https://repo.anaconda.com/pkgs/main/noarch
                              https://repo.anaconda.com/pkgs/r/osx-64
                              https://repo.anaconda.com/pkgs/r/noarch
              package cache : /opt/anaconda3/pkgs
                              /Users/felipe/.conda/pkgs
           envs directories : /opt/anaconda3/envs
                              /Users/felipe/.conda/envs
                   platform : osx-64
                 user-agent : conda/4.9.2 requests/2.24.0 CPython/3.8.5 Darwin/20.5.0 OSX/10.16
                    UID:GID : 501:20
                 netrc file : None
               offline mode : False
    
    
    Note: you may need to restart the kernel to use updated packages.


Se você visualizar uma informação de versão similar a que se segue, então Miniconda foi instalado corretamente.


```python
Current conda install:
               platform : linux-64
          conda version : 4.3.29
          ...
```


      File "<tokenize>", line 3
        conda version : 4.3.29
        ^
    IndentationError: unindent does not match any outer indentation level



Utilizaremos o Miniconda para criar um ambiente virtual de Python 3 chamado *bokeh-amb* para esse tutorial. Na linha de comando, digite o seguinte:


```python
conda create --name bokeh-env python=3.6
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

    Collecting pandas==0.23.1
      Downloading pandas-0.23.1.tar.gz (13.1 MB)
    [K     |████████████████████████████████| 13.1 MB 177 kB/s eta 0:00:01    |███▍                            | 1.4 MB 862 kB/s eta 0:00:14
    [?25hCollecting bokeh==0.13.0
      Downloading bokeh-0.13.0.tar.gz (16.0 MB)
    [K     |████████████████████████████████| 16.0 MB 422 kB/s eta 0:00:01    |█████▏                          | 2.6 MB 286 kB/s eta 0:00:47     |███████████████████▎            | 9.6 MB 234 kB/s eta 0:00:28
    [?25hCollecting pyproj==1.9.5.1
      Downloading pyproj-1.9.5.1.tar.gz (4.4 MB)
    [K     |████████████████████████████████| 4.4 MB 472 kB/s eta 0:00:01
    [?25hRequirement already satisfied: python-dateutil>=2.5.0 in /opt/anaconda3/lib/python3.8/site-packages (from pandas==0.23.1) (2.8.1)
    Requirement already satisfied: pytz>=2011k in /opt/anaconda3/lib/python3.8/site-packages (from pandas==0.23.1) (2020.1)
    Requirement already satisfied: numpy>=1.9.0 in /opt/anaconda3/lib/python3.8/site-packages (from pandas==0.23.1) (1.19.2)
    Requirement already satisfied: six>=1.5.2 in /opt/anaconda3/lib/python3.8/site-packages (from bokeh==0.13.0) (1.15.0)
    Requirement already satisfied: PyYAML>=3.10 in /opt/anaconda3/lib/python3.8/site-packages (from bokeh==0.13.0) (5.3.1)
    Requirement already satisfied: Jinja2>=2.7 in /opt/anaconda3/lib/python3.8/site-packages (from bokeh==0.13.0) (2.11.2)
    Requirement already satisfied: packaging>=16.8 in /opt/anaconda3/lib/python3.8/site-packages (from bokeh==0.13.0) (20.4)
    Requirement already satisfied: tornado>=4.3 in /opt/anaconda3/lib/python3.8/site-packages (from bokeh==0.13.0) (6.0.4)
    Requirement already satisfied: MarkupSafe>=0.23 in /opt/anaconda3/lib/python3.8/site-packages (from Jinja2>=2.7->bokeh==0.13.0) (1.1.1)
    Requirement already satisfied: pyparsing>=2.0.2 in /opt/anaconda3/lib/python3.8/site-packages (from packaging>=16.8->bokeh==0.13.0) (2.4.7)
    Building wheels for collected packages: pandas, bokeh, pyproj
      Building wheel for pandas (setup.py) ... [?25lerror
    [31m  ERROR: Command errored out with exit status 1:
       command: /opt/anaconda3/bin/python -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pandas/setup.py'"'"'; __file__='"'"'/private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pandas/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' bdist_wheel -d /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-wheel-3rqlpz40
           cwd: /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pandas/
      Complete output (1545 lines):
      running bdist_wheel
      running build
      running build_py
      creating build
      creating build/lib.macosx-10.9-x86_64-3.8
      creating build/lib.macosx-10.9-x86_64-3.8/pandas
      copying pandas/conftest.py -> build/lib.macosx-10.9-x86_64-3.8/pandas
      copying pandas/_version.py -> build/lib.macosx-10.9-x86_64-3.8/pandas
      copying pandas/lib.py -> build/lib.macosx-10.9-x86_64-3.8/pandas
      copying pandas/tslib.py -> build/lib.macosx-10.9-x86_64-3.8/pandas
      copying pandas/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas
      copying pandas/parser.py -> build/lib.macosx-10.9-x86_64-3.8/pandas
      copying pandas/testing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas
      copying pandas/json.py -> build/lib.macosx-10.9-x86_64-3.8/pandas
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tools
      copying pandas/tools/merge.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tools
      copying pandas/tools/plotting.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tools
      copying pandas/tools/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tools
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/compat
      copying pandas/compat/chainmap_impl.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/compat
      copying pandas/compat/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/compat
      copying pandas/compat/chainmap.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/compat
      copying pandas/compat/pickle_compat.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/compat
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/types
      copying pandas/types/concat.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/types
      copying pandas/types/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/types
      copying pandas/types/common.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/types
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/core
      copying pandas/core/accessor.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
      copying pandas/core/categorical.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
      copying pandas/core/nanops.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
      copying pandas/core/missing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
      copying pandas/core/internals.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
      copying pandas/core/algorithms.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
      copying pandas/core/config.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
      copying pandas/core/resample.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
      copying pandas/core/window.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
      copying pandas/core/index.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
      copying pandas/core/config_init.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
      copying pandas/core/generic.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
      copying pandas/core/series.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
      copying pandas/core/sorting.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
      copying pandas/core/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
      copying pandas/core/datetools.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
      copying pandas/core/api.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
      copying pandas/core/ops.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
      copying pandas/core/common.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
      copying pandas/core/frame.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
      copying pandas/core/indexing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
      copying pandas/core/panel.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
      copying pandas/core/base.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
      copying pandas/core/strings.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
      copying pandas/core/apply.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/formats
      copying pandas/formats/style.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/formats
      copying pandas/formats/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/formats
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/util
      copying pandas/util/_depr_module.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/util
      copying pandas/util/_test_decorators.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/util
      copying pandas/util/_validators.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/util
      copying pandas/util/_print_versions.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/util
      copying pandas/util/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/util
      copying pandas/util/_decorators.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/util
      copying pandas/util/_doctools.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/util
      copying pandas/util/testing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/util
      copying pandas/util/_tester.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/util
      copying pandas/util/decorators.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/util
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/io
      copying pandas/io/feather_format.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io
      copying pandas/io/parquet.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io
      copying pandas/io/pytables.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io
      copying pandas/io/html.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io
      copying pandas/io/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io
      copying pandas/io/clipboards.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io
      copying pandas/io/parsers.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io
      copying pandas/io/excel.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io
      copying pandas/io/api.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io
      copying pandas/io/common.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io
      copying pandas/io/date_converters.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io
      copying pandas/io/pickle.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io
      copying pandas/io/sql.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io
      copying pandas/io/s3.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io
      copying pandas/io/packers.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io
      copying pandas/io/stata.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io
      copying pandas/io/gbq.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tseries
      copying pandas/tseries/plotting.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tseries
      copying pandas/tseries/converter.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tseries
      copying pandas/tseries/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tseries
      copying pandas/tseries/api.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tseries
      copying pandas/tseries/offsets.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tseries
      copying pandas/tseries/frequencies.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tseries
      copying pandas/tseries/holiday.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tseries
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests
      copying pandas/tests/test_expressions.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests
      copying pandas/tests/test_register_accessor.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests
      copying pandas/tests/test_common.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests
      copying pandas/tests/test_downstream.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests
      copying pandas/tests/test_errors.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests
      copying pandas/tests/test_sorting.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests
      copying pandas/tests/test_join.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests
      copying pandas/tests/test_panel.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests
      copying pandas/tests/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests
      copying pandas/tests/test_lib.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests
      copying pandas/tests/test_resample.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests
      copying pandas/tests/test_nanops.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests
      copying pandas/tests/test_take.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests
      copying pandas/tests/test_algos.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests
      copying pandas/tests/test_multilevel.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests
      copying pandas/tests/test_compat.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests
      copying pandas/tests/test_config.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests
      copying pandas/tests/test_window.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests
      copying pandas/tests/test_strings.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests
      copying pandas/tests/test_base.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/computation
      copying pandas/computation/expressions.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/computation
      copying pandas/computation/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/computation
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/_libs
      copying pandas/_libs/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/_libs
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/plotting
      copying pandas/plotting/_converter.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/plotting
      copying pandas/plotting/_tools.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/plotting
      copying pandas/plotting/_style.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/plotting
      copying pandas/plotting/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/plotting
      copying pandas/plotting/_core.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/plotting
      copying pandas/plotting/_timeseries.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/plotting
      copying pandas/plotting/_compat.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/plotting
      copying pandas/plotting/_misc.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/plotting
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/api
      copying pandas/api/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/api
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/errors
      copying pandas/errors/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/errors
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/compat/numpy
      copying pandas/compat/numpy/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/compat/numpy
      copying pandas/compat/numpy/function.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/compat/numpy
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/core/reshape
      copying pandas/core/reshape/tile.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/reshape
      copying pandas/core/reshape/merge.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/reshape
      copying pandas/core/reshape/concat.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/reshape
      copying pandas/core/reshape/util.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/reshape
      copying pandas/core/reshape/reshape.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/reshape
      copying pandas/core/reshape/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/reshape
      copying pandas/core/reshape/api.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/reshape
      copying pandas/core/reshape/melt.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/reshape
      copying pandas/core/reshape/pivot.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/reshape
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/core/tools
      copying pandas/core/tools/timedeltas.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/tools
      copying pandas/core/tools/datetimes.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/tools
      copying pandas/core/tools/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/tools
      copying pandas/core/tools/numeric.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/tools
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/core/util
      copying pandas/core/util/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/util
      copying pandas/core/util/hashing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/util
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/core/dtypes
      copying pandas/core/dtypes/cast.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/dtypes
      copying pandas/core/dtypes/missing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/dtypes
      copying pandas/core/dtypes/concat.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/dtypes
      copying pandas/core/dtypes/generic.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/dtypes
      copying pandas/core/dtypes/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/dtypes
      copying pandas/core/dtypes/dtypes.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/dtypes
      copying pandas/core/dtypes/api.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/dtypes
      copying pandas/core/dtypes/common.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/dtypes
      copying pandas/core/dtypes/inference.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/dtypes
      copying pandas/core/dtypes/base.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/dtypes
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/core/groupby
      copying pandas/core/groupby/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/groupby
      copying pandas/core/groupby/groupby.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/groupby
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/core/computation
      copying pandas/core/computation/check.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/computation
      copying pandas/core/computation/align.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/computation
      copying pandas/core/computation/pytables.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/computation
      copying pandas/core/computation/engines.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/computation
      copying pandas/core/computation/expressions.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/computation
      copying pandas/core/computation/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/computation
      copying pandas/core/computation/api.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/computation
      copying pandas/core/computation/ops.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/computation
      copying pandas/core/computation/common.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/computation
      copying pandas/core/computation/eval.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/computation
      copying pandas/core/computation/scope.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/computation
      copying pandas/core/computation/expr.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/computation
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/core/arrays
      copying pandas/core/arrays/categorical.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/arrays
      copying pandas/core/arrays/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/arrays
      copying pandas/core/arrays/base.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/arrays
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/core/sparse
      copying pandas/core/sparse/scipy_sparse.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/sparse
      copying pandas/core/sparse/series.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/sparse
      copying pandas/core/sparse/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/sparse
      copying pandas/core/sparse/api.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/sparse
      copying pandas/core/sparse/frame.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/sparse
      copying pandas/core/sparse/array.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/sparse
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/core/indexes
      copying pandas/core/indexes/accessors.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/indexes
      copying pandas/core/indexes/interval.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/indexes
      copying pandas/core/indexes/timedeltas.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/indexes
      copying pandas/core/indexes/range.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/indexes
      copying pandas/core/indexes/datetimes.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/indexes
      copying pandas/core/indexes/multi.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/indexes
      copying pandas/core/indexes/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/indexes
      copying pandas/core/indexes/api.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/indexes
      copying pandas/core/indexes/period.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/indexes
      copying pandas/core/indexes/frozen.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/indexes
      copying pandas/core/indexes/numeric.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/indexes
      copying pandas/core/indexes/datetimelike.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/indexes
      copying pandas/core/indexes/base.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/indexes
      copying pandas/core/indexes/category.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/indexes
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/io/msgpack
      copying pandas/io/msgpack/_version.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/msgpack
      copying pandas/io/msgpack/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/msgpack
      copying pandas/io/msgpack/exceptions.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/msgpack
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/io/formats
      copying pandas/io/formats/console.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/formats
      copying pandas/io/formats/style.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/formats
      copying pandas/io/formats/terminal.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/formats
      copying pandas/io/formats/html.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/formats
      copying pandas/io/formats/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/formats
      copying pandas/io/formats/format.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/formats
      copying pandas/io/formats/excel.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/formats
      copying pandas/io/formats/css.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/formats
      copying pandas/io/formats/csvs.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/formats
      copying pandas/io/formats/latex.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/formats
      copying pandas/io/formats/printing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/formats
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/io/json
      copying pandas/io/json/normalize.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/json
      copying pandas/io/json/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/json
      copying pandas/io/json/table_schema.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/json
      copying pandas/io/json/json.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/json
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/io/sas
      copying pandas/io/sas/sas7bdat.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/sas
      copying pandas/io/sas/sas_constants.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/sas
      copying pandas/io/sas/sasreader.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/sas
      copying pandas/io/sas/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/sas
      copying pandas/io/sas/sas_xport.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/sas
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/io/clipboard
      copying pandas/io/clipboard/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/clipboard
      copying pandas/io/clipboard/clipboards.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/clipboard
      copying pandas/io/clipboard/exceptions.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/clipboard
      copying pandas/io/clipboard/windows.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/clipboard
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
      copying pandas/tests/series/test_alter_axes.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
      copying pandas/tests/series/test_period.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
      copying pandas/tests/series/test_timeseries.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
      copying pandas/tests/series/test_constructors.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
      copying pandas/tests/series/test_missing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
      copying pandas/tests/series/test_sorting.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
      copying pandas/tests/series/test_timezones.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
      copying pandas/tests/series/test_operators.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
      copying pandas/tests/series/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
      copying pandas/tests/series/test_subclass.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
      copying pandas/tests/series/test_analytics.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
      copying pandas/tests/series/test_io.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
      copying pandas/tests/series/test_apply.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
      copying pandas/tests/series/test_quantile.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
      copying pandas/tests/series/test_datetime_values.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
      copying pandas/tests/series/test_internals.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
      copying pandas/tests/series/common.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
      copying pandas/tests/series/test_repr.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
      copying pandas/tests/series/test_validate.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
      copying pandas/tests/series/test_asof.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
      copying pandas/tests/series/test_api.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
      copying pandas/tests/series/test_rank.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
      copying pandas/tests/series/test_arithmetic.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
      copying pandas/tests/series/test_replace.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
      copying pandas/tests/series/test_combine_concat.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
      copying pandas/tests/series/test_dtypes.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape
      copying pandas/tests/reshape/test_union_categoricals.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape
      copying pandas/tests/reshape/test_tile.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape
      copying pandas/tests/reshape/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape
      copying pandas/tests/reshape/test_pivot.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape
      copying pandas/tests/reshape/test_reshape.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape
      copying pandas/tests/reshape/test_util.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape
      copying pandas/tests/reshape/test_melt.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape
      copying pandas/tests/reshape/test_concat.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tools
      copying pandas/tests/tools/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tools
      copying pandas/tests/tools/test_numeric.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tools
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension
      copying pandas/tests/extension/test_external_block.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension
      copying pandas/tests/extension/conftest.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension
      copying pandas/tests/extension/test_common.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension
      copying pandas/tests/extension/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/util
      copying pandas/tests/util/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/util
      copying pandas/tests/util/test_util.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/util
      copying pandas/tests/util/test_hashing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/util
      copying pandas/tests/util/test_testing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/util
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io
      copying pandas/tests/io/test_parquet.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io
      copying pandas/tests/io/conftest.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io
      copying pandas/tests/io/test_common.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io
      copying pandas/tests/io/test_pickle.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io
      copying pandas/tests/io/test_clipboard.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io
      copying pandas/tests/io/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io
      copying pandas/tests/io/test_stata.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io
      copying pandas/tests/io/test_html.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io
      copying pandas/tests/io/test_pytables.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io
      copying pandas/tests/io/test_sql.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io
      copying pandas/tests/io/test_gbq.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io
      copying pandas/tests/io/test_feather.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io
      copying pandas/tests/io/generate_legacy_storage_files.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io
      copying pandas/tests/io/test_excel.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io
      copying pandas/tests/io/test_s3.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io
      copying pandas/tests/io/test_packers.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tseries
      copying pandas/tests/tseries/conftest.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tseries
      copying pandas/tests/tseries/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tseries
      copying pandas/tests/tseries/test_frequencies.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tseries
      copying pandas/tests/tseries/test_holiday.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tseries
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
      copying pandas/tests/frame/test_block_internals.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
      copying pandas/tests/frame/test_alter_axes.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
      copying pandas/tests/frame/test_period.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
      copying pandas/tests/frame/test_axis_select_reindex.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
      copying pandas/tests/frame/test_convert_to.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
      copying pandas/tests/frame/test_timeseries.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
      copying pandas/tests/frame/test_constructors.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
      copying pandas/tests/frame/test_mutate_columns.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
      copying pandas/tests/frame/test_missing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
      copying pandas/tests/frame/test_sorting.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
      copying pandas/tests/frame/test_query_eval.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
      copying pandas/tests/frame/test_join.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
      copying pandas/tests/frame/test_timezones.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
      copying pandas/tests/frame/test_sort_values_level_as_str.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
      copying pandas/tests/frame/test_operators.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
      copying pandas/tests/frame/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
      copying pandas/tests/frame/test_subclass.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
      copying pandas/tests/frame/test_reshape.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
      copying pandas/tests/frame/test_analytics.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
      copying pandas/tests/frame/test_apply.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
      copying pandas/tests/frame/test_quantile.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
      copying pandas/tests/frame/test_indexing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
      copying pandas/tests/frame/test_repr_info.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
      copying pandas/tests/frame/common.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
      copying pandas/tests/frame/test_nonunique_indexes.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
      copying pandas/tests/frame/test_validate.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
      copying pandas/tests/frame/test_asof.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
      copying pandas/tests/frame/test_api.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
      copying pandas/tests/frame/test_rank.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
      copying pandas/tests/frame/test_arithmetic.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
      copying pandas/tests/frame/test_replace.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
      copying pandas/tests/frame/test_combine_concat.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
      copying pandas/tests/frame/test_dtypes.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
      copying pandas/tests/frame/test_to_csv.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/dtypes
      copying pandas/tests/dtypes/test_inference.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/dtypes
      copying pandas/tests/dtypes/test_common.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/dtypes
      copying pandas/tests/dtypes/test_cast.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/dtypes
      copying pandas/tests/dtypes/test_missing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/dtypes
      copying pandas/tests/dtypes/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/dtypes
      copying pandas/tests/dtypes/test_generic.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/dtypes
      copying pandas/tests/dtypes/test_concat.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/dtypes
      copying pandas/tests/dtypes/test_dtypes.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/dtypes
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/categorical
      copying pandas/tests/categorical/conftest.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/categorical
      copying pandas/tests/categorical/test_warnings.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/categorical
      copying pandas/tests/categorical/test_constructors.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/categorical
      copying pandas/tests/categorical/test_missing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/categorical
      copying pandas/tests/categorical/test_sorting.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/categorical
      copying pandas/tests/categorical/test_operators.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/categorical
      copying pandas/tests/categorical/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/categorical
      copying pandas/tests/categorical/test_subclass.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/categorical
      copying pandas/tests/categorical/test_analytics.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/categorical
      copying pandas/tests/categorical/test_indexing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/categorical
      copying pandas/tests/categorical/test_algos.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/categorical
      copying pandas/tests/categorical/common.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/categorical
      copying pandas/tests/categorical/test_repr.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/categorical
      copying pandas/tests/categorical/test_api.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/categorical
      copying pandas/tests/categorical/test_dtypes.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/categorical
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/groupby
      copying pandas/tests/groupby/test_timegrouper.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/groupby
      copying pandas/tests/groupby/test_grouping.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/groupby
      copying pandas/tests/groupby/test_counting.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/groupby
      copying pandas/tests/groupby/test_value_counts.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/groupby
      copying pandas/tests/groupby/conftest.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/groupby
      copying pandas/tests/groupby/test_transform.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/groupby
      copying pandas/tests/groupby/test_nth.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/groupby
      copying pandas/tests/groupby/test_categorical.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/groupby
      copying pandas/tests/groupby/test_bin_groupby.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/groupby
      copying pandas/tests/groupby/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/groupby
      copying pandas/tests/groupby/test_apply.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/groupby
      copying pandas/tests/groupby/test_function.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/groupby
      copying pandas/tests/groupby/test_groupby.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/groupby
      copying pandas/tests/groupby/test_filters.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/groupby
      copying pandas/tests/groupby/test_rank.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/groupby
      copying pandas/tests/groupby/test_index_as_string.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/groupby
      copying pandas/tests/groupby/test_whitelist.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/groupby
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/internals
      copying pandas/tests/internals/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/internals
      copying pandas/tests/internals/test_internals.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/internals
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/computation
      copying pandas/tests/computation/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/computation
      copying pandas/tests/computation/test_compat.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/computation
      copying pandas/tests/computation/test_eval.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/computation
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/plotting
      copying pandas/tests/plotting/test_frame.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/plotting
      copying pandas/tests/plotting/test_misc.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/plotting
      copying pandas/tests/plotting/test_boxplot_method.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/plotting
      copying pandas/tests/plotting/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/plotting
      copying pandas/tests/plotting/test_datetimelike.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/plotting
      copying pandas/tests/plotting/test_deprecated.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/plotting
      copying pandas/tests/plotting/test_hist_method.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/plotting
      copying pandas/tests/plotting/common.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/plotting
      copying pandas/tests/plotting/test_groupby.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/plotting
      copying pandas/tests/plotting/test_converter.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/plotting
      copying pandas/tests/plotting/test_series.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/plotting
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/api
      copying pandas/tests/api/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/api
      copying pandas/tests/api/test_api.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/api
      copying pandas/tests/api/test_types.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/api
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/generic
      copying pandas/tests/generic/test_frame.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/generic
      copying pandas/tests/generic/test_panel.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/generic
      copying pandas/tests/generic/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/generic
      copying pandas/tests/generic/test_generic.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/generic
      copying pandas/tests/generic/test_label_or_level_utils.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/generic
      copying pandas/tests/generic/test_series.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/generic
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tslibs
      copying pandas/tests/tslibs/test_parsing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tslibs
      copying pandas/tests/tslibs/test_ccalendar.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tslibs
      copying pandas/tests/tslibs/test_timezones.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tslibs
      copying pandas/tests/tslibs/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tslibs
      copying pandas/tests/tslibs/test_conversion.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tslibs
      copying pandas/tests/tslibs/test_array_to_datetime.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tslibs
      copying pandas/tests/tslibs/test_liboffsets.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tslibs
      copying pandas/tests/tslibs/test_libfrequencies.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tslibs
      copying pandas/tests/tslibs/test_period_asfreq.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tslibs
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/sparse
      copying pandas/tests/sparse/test_libsparse.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/sparse
      copying pandas/tests/sparse/test_array.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/sparse
      copying pandas/tests/sparse/test_arithmetics.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/sparse
      copying pandas/tests/sparse/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/sparse
      copying pandas/tests/sparse/test_pivot.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/sparse
      copying pandas/tests/sparse/test_reshape.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/sparse
      copying pandas/tests/sparse/test_indexing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/sparse
      copying pandas/tests/sparse/common.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/sparse
      copying pandas/tests/sparse/test_groupby.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/sparse
      copying pandas/tests/sparse/test_combine_concat.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/sparse
      copying pandas/tests/sparse/test_format.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/sparse
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexing
      copying pandas/tests/indexing/test_indexing_slow.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexing
      copying pandas/tests/indexing/test_multiindex.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexing
      copying pandas/tests/indexing/test_ix.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexing
      copying pandas/tests/indexing/test_chaining_and_caching.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexing
      copying pandas/tests/indexing/test_callable.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexing
      copying pandas/tests/indexing/test_panel.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexing
      copying pandas/tests/indexing/test_categorical.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexing
      copying pandas/tests/indexing/test_iloc.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexing
      copying pandas/tests/indexing/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexing
      copying pandas/tests/indexing/test_loc.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexing
      copying pandas/tests/indexing/test_timedelta.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexing
      copying pandas/tests/indexing/test_indexing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexing
      copying pandas/tests/indexing/test_datetime.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexing
      copying pandas/tests/indexing/test_floats.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexing
      copying pandas/tests/indexing/common.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexing
      copying pandas/tests/indexing/test_coercion.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexing
      copying pandas/tests/indexing/test_scalar.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexing
      copying pandas/tests/indexing/test_partial.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexing
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/scalar
      copying pandas/tests/scalar/test_nat.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/scalar
      copying pandas/tests/scalar/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/scalar
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes
      copying pandas/tests/indexes/test_frozen.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes
      copying pandas/tests/indexes/conftest.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes
      copying pandas/tests/indexes/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes
      copying pandas/tests/indexes/test_numeric.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes
      copying pandas/tests/indexes/common.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes
      copying pandas/tests/indexes/datetimelike.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes
      copying pandas/tests/indexes/test_category.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes
      copying pandas/tests/indexes/test_multi.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes
      copying pandas/tests/indexes/test_range.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes
      copying pandas/tests/indexes/test_base.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series/indexing
      copying pandas/tests/series/indexing/test_alter_index.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series/indexing
      copying pandas/tests/series/indexing/conftest.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series/indexing
      copying pandas/tests/series/indexing/test_callable.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series/indexing
      copying pandas/tests/series/indexing/test_boolean.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series/indexing
      copying pandas/tests/series/indexing/test_iloc.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series/indexing
      copying pandas/tests/series/indexing/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series/indexing
      copying pandas/tests/series/indexing/test_loc.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series/indexing
      copying pandas/tests/series/indexing/test_indexing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series/indexing
      copying pandas/tests/series/indexing/test_numeric.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series/indexing
      copying pandas/tests/series/indexing/test_datetime.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series/indexing
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape/merge
      copying pandas/tests/reshape/merge/test_merge_index_as_string.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape/merge
      copying pandas/tests/reshape/merge/test_merge_asof.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape/merge
      copying pandas/tests/reshape/merge/test_join.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape/merge
      copying pandas/tests/reshape/merge/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape/merge
      copying pandas/tests/reshape/merge/test_merge.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape/merge
      copying pandas/tests/reshape/merge/test_merge_ordered.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape/merge
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension/decimal
      copying pandas/tests/extension/decimal/test_decimal.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension/decimal
      copying pandas/tests/extension/decimal/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension/decimal
      copying pandas/tests/extension/decimal/array.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension/decimal
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension/category
      copying pandas/tests/extension/category/test_categorical.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension/category
      copying pandas/tests/extension/category/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension/category
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension/json
      copying pandas/tests/extension/json/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension/json
      copying pandas/tests/extension/json/test_json.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension/json
      copying pandas/tests/extension/json/array.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension/json
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension/base
      copying pandas/tests/extension/base/missing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension/base
      copying pandas/tests/extension/base/reshaping.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension/base
      copying pandas/tests/extension/base/methods.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension/base
      copying pandas/tests/extension/base/setitem.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension/base
      copying pandas/tests/extension/base/dtype.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension/base
      copying pandas/tests/extension/base/interface.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension/base
      copying pandas/tests/extension/base/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension/base
      copying pandas/tests/extension/base/getitem.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension/base
      copying pandas/tests/extension/base/casting.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension/base
      copying pandas/tests/extension/base/groupby.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension/base
      copying pandas/tests/extension/base/base.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension/base
      copying pandas/tests/extension/base/constructors.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension/base
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/msgpack
      copying pandas/tests/io/msgpack/test_extension.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/msgpack
      copying pandas/tests/io/msgpack/test_subtype.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/msgpack
      copying pandas/tests/io/msgpack/test_buffer.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/msgpack
      copying pandas/tests/io/msgpack/test_unpack.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/msgpack
      copying pandas/tests/io/msgpack/test_pack.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/msgpack
      copying pandas/tests/io/msgpack/test_unpack_raw.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/msgpack
      copying pandas/tests/io/msgpack/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/msgpack
      copying pandas/tests/io/msgpack/test_except.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/msgpack
      copying pandas/tests/io/msgpack/test_case.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/msgpack
      copying pandas/tests/io/msgpack/test_read_size.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/msgpack
      copying pandas/tests/io/msgpack/common.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/msgpack
      copying pandas/tests/io/msgpack/test_seq.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/msgpack
      copying pandas/tests/io/msgpack/test_limits.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/msgpack
      copying pandas/tests/io/msgpack/test_obj.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/msgpack
      copying pandas/tests/io/msgpack/test_newspec.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/msgpack
      copying pandas/tests/io/msgpack/test_format.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/msgpack
      copying pandas/tests/io/msgpack/test_sequnpack.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/msgpack
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/formats
      copying pandas/tests/io/formats/test_to_latex.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/formats
      copying pandas/tests/io/formats/test_to_html.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/formats
      copying pandas/tests/io/formats/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/formats
      copying pandas/tests/io/formats/test_eng_formatting.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/formats
      copying pandas/tests/io/formats/test_printing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/formats
      copying pandas/tests/io/formats/test_style.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/formats
      copying pandas/tests/io/formats/test_css.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/formats
      copying pandas/tests/io/formats/test_to_excel.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/formats
      copying pandas/tests/io/formats/test_format.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/formats
      copying pandas/tests/io/formats/test_to_csv.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/formats
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser
      copying pandas/tests/io/parser/parse_dates.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser
      copying pandas/tests/io/parser/na_values.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser
      copying pandas/tests/io/parser/comment.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser
      copying pandas/tests/io/parser/skiprows.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser
      copying pandas/tests/io/parser/header.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser
      copying pandas/tests/io/parser/dialect.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser
      copying pandas/tests/io/parser/test_parsers.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser
      copying pandas/tests/io/parser/compression.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser
      copying pandas/tests/io/parser/python_parser_only.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser
      copying pandas/tests/io/parser/index_col.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser
      copying pandas/tests/io/parser/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser
      copying pandas/tests/io/parser/dtypes.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser
      copying pandas/tests/io/parser/test_read_fwf.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser
      copying pandas/tests/io/parser/c_parser_only.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser
      copying pandas/tests/io/parser/test_unsupported.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser
      copying pandas/tests/io/parser/test_textreader.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser
      copying pandas/tests/io/parser/usecols.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser
      copying pandas/tests/io/parser/test_network.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser
      copying pandas/tests/io/parser/quoting.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser
      copying pandas/tests/io/parser/common.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser
      copying pandas/tests/io/parser/mangle_dupes.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser
      copying pandas/tests/io/parser/multithread.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser
      copying pandas/tests/io/parser/converters.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/json
      copying pandas/tests/io/json/test_compression.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/json
      copying pandas/tests/io/json/test_json_table_schema.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/json
      copying pandas/tests/io/json/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/json
      copying pandas/tests/io/json/test_readlines.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/json
      copying pandas/tests/io/json/test_ujson.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/json
      copying pandas/tests/io/json/test_pandas.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/json
      copying pandas/tests/io/json/test_normalize.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/json
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas
      copying pandas/tests/io/sas/test_sas7bdat.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas
      copying pandas/tests/io/sas/test_sas.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas
      copying pandas/tests/io/sas/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas
      copying pandas/tests/io/sas/test_xport.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tseries/offsets
      copying pandas/tests/tseries/offsets/conftest.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tseries/offsets
      copying pandas/tests/tseries/offsets/test_fiscal.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tseries/offsets
      copying pandas/tests/tseries/offsets/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tseries/offsets
      copying pandas/tests/tseries/offsets/test_yqm_offsets.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tseries/offsets
      copying pandas/tests/tseries/offsets/common.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tseries/offsets
      copying pandas/tests/tseries/offsets/test_ticks.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tseries/offsets
      copying pandas/tests/tseries/offsets/test_offsets.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tseries/offsets
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/groupby/aggregate
      copying pandas/tests/groupby/aggregate/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/groupby/aggregate
      copying pandas/tests/groupby/aggregate/test_cython.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/groupby/aggregate
      copying pandas/tests/groupby/aggregate/test_aggregate.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/groupby/aggregate
      copying pandas/tests/groupby/aggregate/test_other.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/groupby/aggregate
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/sparse/series
      copying pandas/tests/sparse/series/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/sparse/series
      copying pandas/tests/sparse/series/test_indexing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/sparse/series
      copying pandas/tests/sparse/series/test_series.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/sparse/series
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/sparse/frame
      copying pandas/tests/sparse/frame/test_frame.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/sparse/frame
      copying pandas/tests/sparse/frame/test_to_from_scipy.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/sparse/frame
      copying pandas/tests/sparse/frame/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/sparse/frame
      copying pandas/tests/sparse/frame/test_analytics.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/sparse/frame
      copying pandas/tests/sparse/frame/test_apply.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/sparse/frame
      copying pandas/tests/sparse/frame/test_indexing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/sparse/frame
      copying pandas/tests/sparse/frame/test_to_csv.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/sparse/frame
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexing/interval
      copying pandas/tests/indexing/interval/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexing/interval
      copying pandas/tests/indexing/interval/test_interval.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexing/interval
      copying pandas/tests/indexing/interval/test_interval_new.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexing/interval
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/scalar/interval
      copying pandas/tests/scalar/interval/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/scalar/interval
      copying pandas/tests/scalar/interval/test_interval.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/scalar/interval
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/scalar/timedelta
      copying pandas/tests/scalar/timedelta/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/scalar/timedelta
      copying pandas/tests/scalar/timedelta/test_timedelta.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/scalar/timedelta
      copying pandas/tests/scalar/timedelta/test_formats.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/scalar/timedelta
      copying pandas/tests/scalar/timedelta/test_construction.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/scalar/timedelta
      copying pandas/tests/scalar/timedelta/test_arithmetic.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/scalar/timedelta
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/scalar/period
      copying pandas/tests/scalar/period/test_period.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/scalar/period
      copying pandas/tests/scalar/period/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/scalar/period
      copying pandas/tests/scalar/period/test_asfreq.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/scalar/period
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/scalar/timestamp
      copying pandas/tests/scalar/timestamp/test_timezones.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/scalar/timestamp
      copying pandas/tests/scalar/timestamp/test_timestamp.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/scalar/timestamp
      copying pandas/tests/scalar/timestamp/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/scalar/timestamp
      copying pandas/tests/scalar/timestamp/test_comparisons.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/scalar/timestamp
      copying pandas/tests/scalar/timestamp/test_rendering.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/scalar/timestamp
      copying pandas/tests/scalar/timestamp/test_unary_ops.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/scalar/timestamp
      copying pandas/tests/scalar/timestamp/test_arithmetic.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/scalar/timestamp
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/interval
      copying pandas/tests/indexes/interval/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/interval
      copying pandas/tests/indexes/interval/test_interval_range.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/interval
      copying pandas/tests/indexes/interval/test_interval.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/interval
      copying pandas/tests/indexes/interval/test_astype.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/interval
      copying pandas/tests/indexes/interval/test_construction.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/interval
      copying pandas/tests/indexes/interval/test_interval_new.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/interval
      copying pandas/tests/indexes/interval/test_interval_tree.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/interval
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/period
      copying pandas/tests/indexes/period/test_period.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/period
      copying pandas/tests/indexes/period/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/period
      copying pandas/tests/indexes/period/test_scalar_compat.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/period
      copying pandas/tests/indexes/period/test_indexing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/period
      copying pandas/tests/indexes/period/test_astype.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/period
      copying pandas/tests/indexes/period/test_formats.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/period
      copying pandas/tests/indexes/period/test_setops.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/period
      copying pandas/tests/indexes/period/test_construction.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/period
      copying pandas/tests/indexes/period/test_partial_slicing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/period
      copying pandas/tests/indexes/period/test_ops.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/period
      copying pandas/tests/indexes/period/test_arithmetic.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/period
      copying pandas/tests/indexes/period/test_tools.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/period
      copying pandas/tests/indexes/period/test_asfreq.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/period
      copying pandas/tests/indexes/period/test_period_range.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/period
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/datetimes
      copying pandas/tests/indexes/datetimes/test_misc.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/datetimes
      copying pandas/tests/indexes/datetimes/test_missing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/datetimes
      copying pandas/tests/indexes/datetimes/test_date_range.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/datetimes
      copying pandas/tests/indexes/datetimes/test_timezones.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/datetimes
      copying pandas/tests/indexes/datetimes/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/datetimes
      copying pandas/tests/indexes/datetimes/test_datetimelike.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/datetimes
      copying pandas/tests/indexes/datetimes/test_scalar_compat.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/datetimes
      copying pandas/tests/indexes/datetimes/test_indexing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/datetimes
      copying pandas/tests/indexes/datetimes/test_astype.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/datetimes
      copying pandas/tests/indexes/datetimes/test_formats.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/datetimes
      copying pandas/tests/indexes/datetimes/test_setops.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/datetimes
      copying pandas/tests/indexes/datetimes/test_datetime.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/datetimes
      copying pandas/tests/indexes/datetimes/test_construction.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/datetimes
      copying pandas/tests/indexes/datetimes/test_partial_slicing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/datetimes
      copying pandas/tests/indexes/datetimes/test_ops.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/datetimes
      copying pandas/tests/indexes/datetimes/test_arithmetic.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/datetimes
      copying pandas/tests/indexes/datetimes/test_tools.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/datetimes
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/timedeltas
      copying pandas/tests/indexes/timedeltas/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/timedeltas
      copying pandas/tests/indexes/timedeltas/test_timedelta.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/timedeltas
      copying pandas/tests/indexes/timedeltas/test_scalar_compat.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/timedeltas
      copying pandas/tests/indexes/timedeltas/test_indexing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/timedeltas
      copying pandas/tests/indexes/timedeltas/test_astype.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/timedeltas
      copying pandas/tests/indexes/timedeltas/test_formats.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/timedeltas
      copying pandas/tests/indexes/timedeltas/test_setops.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/timedeltas
      copying pandas/tests/indexes/timedeltas/test_construction.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/timedeltas
      copying pandas/tests/indexes/timedeltas/test_partial_slicing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/timedeltas
      copying pandas/tests/indexes/timedeltas/test_ops.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/timedeltas
      copying pandas/tests/indexes/timedeltas/test_arithmetic.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/timedeltas
      copying pandas/tests/indexes/timedeltas/test_timedelta_range.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/timedeltas
      copying pandas/tests/indexes/timedeltas/test_tools.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/timedeltas
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/_libs/tslibs
      copying pandas/_libs/tslibs/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/_libs/tslibs
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/api/types
      copying pandas/api/types/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/api/types
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/api/extensions
      copying pandas/api/extensions/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/api/extensions
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/data
      copying pandas/tests/data/tips.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/data
      copying pandas/tests/data/iris.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/data
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/io/formats/templates
      copying pandas/io/formats/templates/html.tpl -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/formats/templates
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape/data
      copying pandas/tests/reshape/data/cut_data.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape/data
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/test3.xlsx -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/test3.xls -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/stata6_114.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/testdtype.xlsx -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/stata7_111.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/testdtype.xlsm -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/stata15.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/stata6_115.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/test2.xls -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/test3.xlsm -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/stata6_117.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/spam.html -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/stata13_dates.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/test1.xls -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/gbq_fake_job.txt -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/test5.xls -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/stata7_117.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/stata6_113.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/test4.xls -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/blank.xls -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/banklist.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/test2.xlsm -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/test_types.xls -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/test_multisheet.xlsx -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/testdateoverflow.xls -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/stata7_115.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/test_multisheet.xlsm -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/valid_markup.html -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/test2.xlsx -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/blank_with_header.xlsm -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/stata5_117.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/test_converters.xls -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/times_1900.xls -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/blank_with_header.xlsx -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/stata6.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/stata4_113.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/test5.xlsx -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/stata5_114.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/nyse_wsj.html -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/wikipedia_states.html -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/stata5_115.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/test5.xlsm -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/stata5.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/times_1900.xlsx -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/stata4_114.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/test4.xlsm -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/test_index_name_pre17.xlsm -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/categorical_0_15_2.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/test_index_name_pre17.xlsx -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/times_1900.xlsm -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/stata4_115.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/test4.xlsx -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/testmultiindex.xlsx -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/tips.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/stata4_117.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/blank.xlsm -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/testskiprows.xlsx -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/times_1904.xls -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/testmultiindex.xls -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/stata5_113.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/testmultiindex.xlsm -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/blank.xlsx -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/stata3.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/testskiprows.xlsm -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/test_squeeze.xlsx -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/stata8_115.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/testdateoverflow.xlsx -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/testdateoverflow.xlsm -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/stata10_117.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/stata1_117.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/test_squeeze.xlsm -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/test_types.xlsx -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/iris.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/stata10_115.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/stata1_114.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/macau.html -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/stata8_117.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/test_types.xlsm -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/stata14_118.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/stata8_113.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/stata11_115.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/testdtype.xls -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/blank_with_header.xls -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/stata9_117.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/stata9_115.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/computer_sales_page.html -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/test1.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/stata11_117.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/test_index_name_pre17.xls -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/stata2_115.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/test1.xlsm -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/test_multisheet.xls -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/categorical_0_14_1.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/S4_EDUC1.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/test1.xlsx -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/stata2_114.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/stata3_113.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/test_mmap.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/stata2_117.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/stata2_113.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/test_squeeze.xls -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/test_converters.xlsm -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/banklist.html -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/stata1_encoding.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/feather-0_3_1.feather -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/testskiprows.xls -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/stata3_117.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/stata12_117.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/test_converters.xlsx -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/stata3_115.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/times_1904.xlsm -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/fixed_width_format.txt -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/stata3_114.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      copying pandas/tests/io/data/times_1904.xlsx -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_hdf
      copying pandas/tests/io/data/legacy_hdf/legacy_table.h5 -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_hdf
      copying pandas/tests/io/data/legacy_hdf/datetimetz_object.h5 -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_hdf
      copying pandas/tests/io/data/legacy_hdf/pytables_native.h5 -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_hdf
      copying pandas/tests/io/data/legacy_hdf/pytables_native2.h5 -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_hdf
      copying pandas/tests/io/data/legacy_hdf/periodindex_0.20.1_x86_64_darwin_2.7.13.h5 -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_hdf
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.11.0
      copying pandas/tests/io/data/legacy_pickle/0.11.0/x86_64_linux_2.7.3.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.11.0
      copying pandas/tests/io/data/legacy_pickle/0.11.0/x86_64_linux_3.3.0.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.11.0
      copying pandas/tests/io/data/legacy_pickle/0.11.0/0.11.0_x86_64_linux_3.3.0.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.11.0
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.15.0
      copying pandas/tests/io/data/legacy_pickle/0.15.0/0.15.0_x86_64_darwin_2.7.12.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.15.0
      copying pandas/tests/io/data/legacy_pickle/0.15.0/0.15.0_x86_64_linux_2.7.8.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.15.0
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.19.2
      copying pandas/tests/io/data/legacy_pickle/0.19.2/0.19.2_x86_64_darwin_2.7.12.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.19.2
      copying pandas/tests/io/data/legacy_pickle/0.19.2/0.19.2_x86_64_darwin_2.7.14.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.19.2
      copying pandas/tests/io/data/legacy_pickle/0.19.2/0.19.2_x86_64_darwin_3.6.1.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.19.2
      copying pandas/tests/io/data/legacy_pickle/0.19.2/0.19.2_AMD64_windows_2.7.14.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.19.2
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.18.0
      copying pandas/tests/io/data/legacy_pickle/0.18.0/0.18.0_x86_64_darwin_3.5.1.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.18.0
      copying pandas/tests/io/data/legacy_pickle/0.18.0/0.18.0_x86_64_darwin_2.7.11.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.18.0
      copying pandas/tests/io/data/legacy_pickle/0.18.0/0.18.0_AMD64_windows_3.5.1.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.18.0
      copying pandas/tests/io/data/legacy_pickle/0.18.0/0.18.0_AMD64_windows_2.7.11.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.18.0
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.12.0
      copying pandas/tests/io/data/legacy_pickle/0.12.0/0.12.0_AMD64_windows_2.7.3.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.12.0
      copying pandas/tests/io/data/legacy_pickle/0.12.0/0.12.0_x86_64_linux_2.7.3.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.12.0
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.18.1
      copying pandas/tests/io/data/legacy_pickle/0.18.1/0.18.1_x86_64_darwin_2.7.12.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.18.1
      copying pandas/tests/io/data/legacy_pickle/0.18.1/0.18.1_x86_64_darwin_3.5.2.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.18.1
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.16.0
      copying pandas/tests/io/data/legacy_pickle/0.16.0/0.16.0_x86_64_darwin_2.7.9.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.16.0
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.20.3
      copying pandas/tests/io/data/legacy_pickle/0.20.3/0.20.3_x86_64_darwin_2.7.14.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.20.3
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.13.0
      copying pandas/tests/io/data/legacy_pickle/0.13.0/0.13.0_x86_64_darwin_2.7.5.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.13.0
      copying pandas/tests/io/data/legacy_pickle/0.13.0/0.13.0_i686_linux_3.2.3.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.13.0
      copying pandas/tests/io/data/legacy_pickle/0.13.0/0.13.0_i686_linux_2.6.5.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.13.0
      copying pandas/tests/io/data/legacy_pickle/0.13.0/0.13.0_x86_64_linux_3.3.0.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.13.0
      copying pandas/tests/io/data/legacy_pickle/0.13.0/0.13.0_x86_64_linux_2.7.8.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.13.0
      copying pandas/tests/io/data/legacy_pickle/0.13.0/0.13.0_i686_linux_2.7.3.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.13.0
      copying pandas/tests/io/data/legacy_pickle/0.13.0/0.13.0_x86_64_linux_2.7.3.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.13.0
      copying pandas/tests/io/data/legacy_pickle/0.13.0/0.13.0_x86_64_darwin_2.7.6.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.13.0
      copying pandas/tests/io/data/legacy_pickle/0.13.0/0.13.0_AMD64_windows_2.7.3.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.13.0
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.17.1
      copying pandas/tests/io/data/legacy_pickle/0.17.1/0.17.1_x86_64_darwin_2.7.11.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.17.1
      copying pandas/tests/io/data/legacy_pickle/0.17.1/0.17.1_AMD64_windows_2.7.11.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.17.1
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.15.2
      copying pandas/tests/io/data/legacy_pickle/0.15.2/0.15.2_x86_64_darwin_2.7.9.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.15.2
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.17.0
      copying pandas/tests/io/data/legacy_pickle/0.17.0/0.17.0_x86_64_linux_3.4.4.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.17.0
      copying pandas/tests/io/data/legacy_pickle/0.17.0/0.17.0_x86_64_linux_2.7.11.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.17.0
      copying pandas/tests/io/data/legacy_pickle/0.17.0/0.17.0_x86_64_darwin_3.4.4.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.17.0
      copying pandas/tests/io/data/legacy_pickle/0.17.0/0.17.0_x86_64_darwin_2.7.11.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.17.0
      copying pandas/tests/io/data/legacy_pickle/0.17.0/0.17.0_AMD64_windows_3.4.4.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.17.0
      copying pandas/tests/io/data/legacy_pickle/0.17.0/0.17.1_AMD64_windows_2.7.11.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.17.0
      copying pandas/tests/io/data/legacy_pickle/0.17.0/0.17.0_AMD64_windows_2.7.11.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.17.0
      copying pandas/tests/io/data/legacy_pickle/0.17.0/0.17.0_x86_64_darwin_3.5.3.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.17.0
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.14.1
      copying pandas/tests/io/data/legacy_pickle/0.14.1/0.14.1_x86_64_linux_2.7.8.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.14.1
      copying pandas/tests/io/data/legacy_pickle/0.14.1/0.14.1_x86_64_darwin_2.7.12.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.14.1
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.16.2
      copying pandas/tests/io/data/legacy_pickle/0.16.2/0.16.2_x86_64_darwin_2.7.10.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.16.2
      copying pandas/tests/io/data/legacy_pickle/0.16.2/0.16.2_AMD64_windows_3.4.3.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.16.2
      copying pandas/tests/io/data/legacy_pickle/0.16.2/0.16.2_AMD64_windows_2.7.10.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.16.2
      copying pandas/tests/io/data/legacy_pickle/0.16.2/0.16.2_x86_64_linux_2.7.10.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.16.2
      copying pandas/tests/io/data/legacy_pickle/0.16.2/0.16.2_x86_64_darwin_2.7.9.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.16.2
      copying pandas/tests/io/data/legacy_pickle/0.16.2/0.16.2_x86_64_linux_3.4.3.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.16.2
      copying pandas/tests/io/data/legacy_pickle/0.16.2/0.16.2_x86_64_darwin_3.4.3.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.16.2
      copying pandas/tests/io/data/legacy_pickle/0.16.2/0.16.2_AMD64_windows_2.7.14.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.16.2
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.14.0
      copying pandas/tests/io/data/legacy_pickle/0.14.0/0.14.0_x86_64_darwin_2.7.6.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.14.0
      copying pandas/tests/io/data/legacy_pickle/0.14.0/0.14.0_x86_64_linux_2.7.8.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.14.0
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.10.1
      copying pandas/tests/io/data/legacy_pickle/0.10.1/x86_64_linux_2.7.3.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.10.1
      copying pandas/tests/io/data/legacy_pickle/0.10.1/AMD64_windows_2.7.3.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.10.1
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.19.2
      copying pandas/tests/io/data/legacy_msgpack/0.19.2/0.19.2_x86_64_darwin_3.6.1.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.19.2
      copying pandas/tests/io/data/legacy_msgpack/0.19.2/0.19.2_x86_64_darwin_2.7.12.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.19.2
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.18.0
      copying pandas/tests/io/data/legacy_msgpack/0.18.0/0.18.0_x86_64_darwin_3.5.1.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.18.0
      copying pandas/tests/io/data/legacy_msgpack/0.18.0/0.18.0_x86_64_darwin_2.7.11.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.18.0
      copying pandas/tests/io/data/legacy_msgpack/0.18.0/0.18.0_AMD64_windows_2.7.11.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.18.0
      copying pandas/tests/io/data/legacy_msgpack/0.18.0/0.18.0_AMD64_windows_3.5.1.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.18.0
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.18.1
      copying pandas/tests/io/data/legacy_msgpack/0.18.1/0.18.1_x86_64_darwin_3.5.2.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.18.1
      copying pandas/tests/io/data/legacy_msgpack/0.18.1/0.18.1_x86_64_darwin_2.7.12.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.18.1
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.16.0
      copying pandas/tests/io/data/legacy_msgpack/0.16.0/0.16.0_x86_64_darwin_2.7.9.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.16.0
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.17.1
      copying pandas/tests/io/data/legacy_msgpack/0.17.1/0.17.1_x86_64_darwin_2.7.11.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.17.1
      copying pandas/tests/io/data/legacy_msgpack/0.17.1/0.17.1_x86_64_darwin_3.5.1.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.17.1
      copying pandas/tests/io/data/legacy_msgpack/0.17.1/0.17.1_AMD64_windows_2.7.11.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.17.1
      copying pandas/tests/io/data/legacy_msgpack/0.17.1/0.17.1_x86_64_linux_3.4.4.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.17.1
      copying pandas/tests/io/data/legacy_msgpack/0.17.1/0.17.1_AMD64_windows_3.5.1.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.17.1
      copying pandas/tests/io/data/legacy_msgpack/0.17.1/0.17.1_x86_64_linux_2.7.11.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.17.1
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.17.0
      copying pandas/tests/io/data/legacy_msgpack/0.17.0/0.17.0_AMD64_windows_3.4.4.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.17.0
      copying pandas/tests/io/data/legacy_msgpack/0.17.0/0.17.1_AMD64_windows_2.7.11.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.17.0
      copying pandas/tests/io/data/legacy_msgpack/0.17.0/0.17.0_x86_64_darwin_3.4.4.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.17.0
      copying pandas/tests/io/data/legacy_msgpack/0.17.0/0.17.0_x86_64_darwin_2.7.11.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.17.0
      copying pandas/tests/io/data/legacy_msgpack/0.17.0/0.17.0_AMD64_windows_2.7.11.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.17.0
      copying pandas/tests/io/data/legacy_msgpack/0.17.0/0.17.0_x86_64_linux_2.7.11.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.17.0
      copying pandas/tests/io/data/legacy_msgpack/0.17.0/0.17.1_AMD64_windows_3.5.1.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.17.0
      copying pandas/tests/io/data/legacy_msgpack/0.17.0/0.17.0_x86_64_linux_3.4.4.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.17.0
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.16.2
      copying pandas/tests/io/data/legacy_msgpack/0.16.2/0.16.2_x86_64_darwin_2.7.10.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.16.2
      copying pandas/tests/io/data/legacy_msgpack/0.16.2/0.16.2_AMD64_windows_2.7.10.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.16.2
      copying pandas/tests/io/data/legacy_msgpack/0.16.2/0.16.2_x86_64_linux_3.4.3.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.16.2
      copying pandas/tests/io/data/legacy_msgpack/0.16.2/0.16.2_AMD64_windows_3.4.3.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.16.2
      copying pandas/tests/io/data/legacy_msgpack/0.16.2/0.16.2_x86_64_linux_2.7.10.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.16.2
      copying pandas/tests/io/data/legacy_msgpack/0.16.2/0.16.2_x86_64_darwin_2.7.9.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.16.2
      copying pandas/tests/io/data/legacy_msgpack/0.16.2/0.16.2_x86_64_darwin_3.4.3.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.16.2
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/html_encoding
      copying pandas/tests/io/data/html_encoding/chinese_utf-32.html -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/html_encoding
      copying pandas/tests/io/data/html_encoding/letz_latin1.html -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/html_encoding
      copying pandas/tests/io/data/html_encoding/chinese_utf-16.html -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/html_encoding
      copying pandas/tests/io/data/html_encoding/chinese_utf-8.html -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/html_encoding
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/data
      copying pandas/tests/indexes/data/multiindex_v1.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/data
      copying pandas/tests/indexes/data/mindex_073.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/data
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape/merge/data
      copying pandas/tests/reshape/merge/data/allow_exact_matches_and_tolerance.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape/merge/data
      copying pandas/tests/reshape/merge/data/quotes.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape/merge/data
      copying pandas/tests/reshape/merge/data/tolerance.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape/merge/data
      copying pandas/tests/reshape/merge/data/asof2.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape/merge/data
      copying pandas/tests/reshape/merge/data/quotes2.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape/merge/data
      copying pandas/tests/reshape/merge/data/trades.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape/merge/data
      copying pandas/tests/reshape/merge/data/trades2.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape/merge/data
      copying pandas/tests/reshape/merge/data/allow_exact_matches.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape/merge/data
      copying pandas/tests/reshape/merge/data/asof.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape/merge/data
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/msgpack/data
      copying pandas/tests/io/msgpack/data/frame.mp -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/msgpack/data
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/formats/data
      copying pandas/tests/io/formats/data/unicode_series.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/formats/data
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser/data
      copying pandas/tests/io/parser/data/utf16_ex.txt -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser/data
      copying pandas/tests/io/parser/data/items.jsonl -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser/data
      copying pandas/tests/io/parser/data/salaries.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser/data
      copying pandas/tests/io/parser/data/sub_char.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser/data
      copying pandas/tests/io/parser/data/tips.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser/data
      copying pandas/tests/io/parser/data/unicode_series.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser/data
      copying pandas/tests/io/parser/data/salaries.csv.zip -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser/data
      copying pandas/tests/io/parser/data/utf16_ex_small.zip -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser/data
      copying pandas/tests/io/parser/data/tips.csv.bz2 -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser/data
      copying pandas/tests/io/parser/data/salaries.csv.bz2 -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser/data
      copying pandas/tests/io/parser/data/iris.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser/data
      copying pandas/tests/io/parser/data/test1.csv.gz -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser/data
      copying pandas/tests/io/parser/data/tar_csv.tar -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser/data
      copying pandas/tests/io/parser/data/test2.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser/data
      copying pandas/tests/io/parser/data/sauron.SHIFT_JIS.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser/data
      copying pandas/tests/io/parser/data/salaries.csv.xz -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser/data
      copying pandas/tests/io/parser/data/test1.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser/data
      copying pandas/tests/io/parser/data/tips.csv.gz -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser/data
      copying pandas/tests/io/parser/data/tar_csv.tar.gz -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser/data
      copying pandas/tests/io/parser/data/test_mmap.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser/data
      copying pandas/tests/io/parser/data/test1.csv.bz2 -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser/data
      copying pandas/tests/io/parser/data/salaries.csv.gz -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser/data
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/json/data
      copying pandas/tests/io/json/data/tsframe_v012.json -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/json/data
      copying pandas/tests/io/json/data/tsframe_iso_v012.json -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/json/data
      copying pandas/tests/io/json/data/tsframe_v012.json.zip -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/json/data
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
      copying pandas/tests/io/sas/data/SSHSV1_A.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
      copying pandas/tests/io/sas/data/test14.sas7bdat -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
      copying pandas/tests/io/sas/data/test15.sas7bdat -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
      copying pandas/tests/io/sas/data/test1.sas7bdat -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
      copying pandas/tests/io/sas/data/test_sas7bdat_2.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
      copying pandas/tests/io/sas/data/test_sas7bdat_1.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
      copying pandas/tests/io/sas/data/zero_variables.sas7bdat -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
      copying pandas/tests/io/sas/data/test6.sas7bdat -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
      copying pandas/tests/io/sas/data/test7.sas7bdat -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
      copying pandas/tests/io/sas/data/productsales.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
      copying pandas/tests/io/sas/data/DEMO_G.xpt -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
      copying pandas/tests/io/sas/data/test_12659.sas7bdat -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
      copying pandas/tests/io/sas/data/datetime.sas7bdat -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
      copying pandas/tests/io/sas/data/DRXFCD_G.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
      copying pandas/tests/io/sas/data/paxraw_d_short.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
      copying pandas/tests/io/sas/data/test13.sas7bdat -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
      copying pandas/tests/io/sas/data/test12.sas7bdat -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
      copying pandas/tests/io/sas/data/test8.sas7bdat -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
      copying pandas/tests/io/sas/data/test9.sas7bdat -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
      copying pandas/tests/io/sas/data/test2.sas7bdat -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
      copying pandas/tests/io/sas/data/test3.sas7bdat -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
      copying pandas/tests/io/sas/data/productsales.sas7bdat -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
      copying pandas/tests/io/sas/data/airline.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
      copying pandas/tests/io/sas/data/DRXFCD_G.xpt -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
      copying pandas/tests/io/sas/data/test_12659.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
      copying pandas/tests/io/sas/data/test16.sas7bdat -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
      copying pandas/tests/io/sas/data/DEMO_G.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
      copying pandas/tests/io/sas/data/paxraw_d_short.xpt -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
      copying pandas/tests/io/sas/data/airline.sas7bdat -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
      copying pandas/tests/io/sas/data/test10.sas7bdat -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
      copying pandas/tests/io/sas/data/test11.sas7bdat -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
      copying pandas/tests/io/sas/data/datetime.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
      copying pandas/tests/io/sas/data/test5.sas7bdat -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
      copying pandas/tests/io/sas/data/test4.sas7bdat -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
      copying pandas/tests/io/sas/data/SSHSV1_A.xpt -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
      creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tseries/offsets/data
      copying pandas/tests/tseries/offsets/data/cday-0.14.1.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tseries/offsets/data
      copying pandas/tests/tseries/offsets/data/dateoffset_0_15_2.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tseries/offsets/data
      UPDATING build/lib.macosx-10.9-x86_64-3.8/pandas/_version.py
      set build/lib.macosx-10.9-x86_64-3.8/pandas/_version.py to '0.23.1'
      running build_ext
      skipping 'pandas/_libs/algos.c' Cython extension (up-to-date)
      skipping 'pandas/_libs/groupby.c' Cython extension (up-to-date)
      skipping 'pandas/_libs/hashing.c' Cython extension (up-to-date)
      skipping 'pandas/_libs/hashtable.c' Cython extension (up-to-date)
      skipping 'pandas/_libs/index.c' Cython extension (up-to-date)
      skipping 'pandas/_libs/indexing.c' Cython extension (up-to-date)
      skipping 'pandas/_libs/internals.c' Cython extension (up-to-date)
      skipping 'pandas/_libs/interval.c' Cython extension (up-to-date)
      skipping 'pandas/_libs/join.c' Cython extension (up-to-date)
      skipping 'pandas/_libs/lib.c' Cython extension (up-to-date)
      skipping 'pandas/_libs/missing.c' Cython extension (up-to-date)
      skipping 'pandas/_libs/parsers.c' Cython extension (up-to-date)
      skipping 'pandas/_libs/reduction.c' Cython extension (up-to-date)
      skipping 'pandas/_libs/ops.c' Cython extension (up-to-date)
      skipping 'pandas/_libs/tslibs/period.c' Cython extension (up-to-date)
      skipping 'pandas/_libs/properties.c' Cython extension (up-to-date)
      skipping 'pandas/_libs/reshape.c' Cython extension (up-to-date)
      skipping 'pandas/_libs/skiplist.c' Cython extension (up-to-date)
      skipping 'pandas/_libs/sparse.c' Cython extension (up-to-date)
      skipping 'pandas/_libs/tslib.c' Cython extension (up-to-date)
      skipping 'pandas/_libs/tslibs/ccalendar.c' Cython extension (up-to-date)
      skipping 'pandas/_libs/tslibs/conversion.c' Cython extension (up-to-date)
      skipping 'pandas/_libs/tslibs/fields.c' Cython extension (up-to-date)
      skipping 'pandas/_libs/tslibs/frequencies.c' Cython extension (up-to-date)
      skipping 'pandas/_libs/tslibs/nattype.c' Cython extension (up-to-date)
      skipping 'pandas/_libs/tslibs/np_datetime.c' Cython extension (up-to-date)
      skipping 'pandas/_libs/tslibs/offsets.c' Cython extension (up-to-date)
      skipping 'pandas/_libs/tslibs/parsing.c' Cython extension (up-to-date)
      skipping 'pandas/_libs/tslibs/resolution.c' Cython extension (up-to-date)
      skipping 'pandas/_libs/tslibs/strptime.c' Cython extension (up-to-date)
      skipping 'pandas/_libs/tslibs/timedeltas.c' Cython extension (up-to-date)
      skipping 'pandas/_libs/tslibs/timestamps.c' Cython extension (up-to-date)
      skipping 'pandas/_libs/tslibs/timezones.c' Cython extension (up-to-date)
      skipping 'pandas/_libs/testing.c' Cython extension (up-to-date)
      skipping 'pandas/_libs/window.cpp' Cython extension (up-to-date)
      skipping 'pandas/_libs/writers.c' Cython extension (up-to-date)
      skipping 'pandas/io/sas/sas.c' Cython extension (up-to-date)
      skipping 'pandas/io/msgpack/_packer.cpp' Cython extension (up-to-date)
      skipping 'pandas/io/msgpack/_unpacker.cpp' Cython extension (up-to-date)
      building 'pandas._libs.algos' extension
      creating build/temp.macosx-10.9-x86_64-3.8
      creating build/temp.macosx-10.9-x86_64-3.8/pandas
      creating build/temp.macosx-10.9-x86_64-3.8/pandas/_libs
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Ipandas/_libs/src/klib -Ipandas/_libs/src -I/opt/anaconda3/lib/python3.8/site-packages/numpy/core/include -I/opt/anaconda3/include/python3.8 -c pandas/_libs/algos.c -o build/temp.macosx-10.9-x86_64-3.8/pandas/_libs/algos.o -Wno-unused-function
      In file included from pandas/_libs/algos.c:566:
      In file included from /opt/anaconda3/lib/python3.8/site-packages/numpy/core/include/numpy/arrayobject.h:4:
      In file included from /opt/anaconda3/lib/python3.8/site-packages/numpy/core/include/numpy/ndarrayobject.h:12:
      In file included from /opt/anaconda3/lib/python3.8/site-packages/numpy/core/include/numpy/ndarraytypes.h:1822:
      /opt/anaconda3/lib/python3.8/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:17:2: warning: "Using deprecated NumPy API, disable it with "          "#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-W#warnings]
      #warning "Using deprecated NumPy API, disable it with " \
       ^
      pandas/_libs/algos.c:136914:26: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
        __pyx_type___pyx_array.tp_print = 0;
                               ^
      /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
          Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
          ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      pandas/_libs/algos.c:136919:32: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
        __pyx_type___pyx_MemviewEnum.tp_print = 0;
                                     ^
      /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
          Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
          ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      pandas/_libs/algos.c:136934:31: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
        __pyx_type___pyx_memoryview.tp_print = 0;
                                    ^
      /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
          Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
          ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      pandas/_libs/algos.c:136947:36: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
        __pyx_type___pyx_memoryviewslice.tp_print = 0;
                                         ^
      /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
          Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
          ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      5 warnings generated.
      gcc -bundle -undefined dynamic_lookup -L/opt/anaconda3/lib -arch x86_64 -L/opt/anaconda3/lib -arch x86_64 -arch x86_64 build/temp.macosx-10.9-x86_64-3.8/pandas/_libs/algos.o -o build/lib.macosx-10.9-x86_64-3.8/pandas/_libs/algos.cpython-38-darwin.so
      building 'pandas._libs.groupby' extension
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Ipandas/_libs/src/klib -Ipandas/_libs/src -I/opt/anaconda3/lib/python3.8/site-packages/numpy/core/include -I/opt/anaconda3/include/python3.8 -c pandas/_libs/groupby.c -o build/temp.macosx-10.9-x86_64-3.8/pandas/_libs/groupby.o -Wno-unused-function
      In file included from pandas/_libs/groupby.c:566:
      In file included from /opt/anaconda3/lib/python3.8/site-packages/numpy/core/include/numpy/arrayobject.h:4:
      In file included from /opt/anaconda3/lib/python3.8/site-packages/numpy/core/include/numpy/ndarrayobject.h:12:
      In file included from /opt/anaconda3/lib/python3.8/site-packages/numpy/core/include/numpy/ndarraytypes.h:1822:
      /opt/anaconda3/lib/python3.8/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:17:2: warning: "Using deprecated NumPy API, disable it with "          "#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-W#warnings]
      #warning "Using deprecated NumPy API, disable it with " \
       ^
      pandas/_libs/groupby.c:27830:40: warning: self-comparison always evaluates to true [-Wtautological-compare]
                  __pyx_t_24 = ((__pyx_v_val == __pyx_v_val) != 0);
                                             ^
      pandas/_libs/groupby.c:28615:40: warning: self-comparison always evaluates to true [-Wtautological-compare]
                  __pyx_t_24 = ((__pyx_v_val == __pyx_v_val) != 0);
                                             ^
      pandas/_libs/groupby.c:60495:26: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
        __pyx_type___pyx_array.tp_print = 0;
                               ^
      /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
          Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
          ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      pandas/_libs/groupby.c:60500:32: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
        __pyx_type___pyx_MemviewEnum.tp_print = 0;
                                     ^
      /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
          Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
          ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      pandas/_libs/groupby.c:60515:31: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
        __pyx_type___pyx_memoryview.tp_print = 0;
                                    ^
      /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
          Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
          ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      pandas/_libs/groupby.c:60528:36: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
        __pyx_type___pyx_memoryviewslice.tp_print = 0;
                                         ^
      /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
          Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
          ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      7 warnings generated.
      gcc -bundle -undefined dynamic_lookup -L/opt/anaconda3/lib -arch x86_64 -L/opt/anaconda3/lib -arch x86_64 -arch x86_64 build/temp.macosx-10.9-x86_64-3.8/pandas/_libs/groupby.o -o build/lib.macosx-10.9-x86_64-3.8/pandas/_libs/groupby.cpython-38-darwin.so
      building 'pandas._libs.hashing' extension
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Ipandas/_libs/src/klib -Ipandas/_libs/src -I/opt/anaconda3/lib/python3.8/site-packages/numpy/core/include -I/opt/anaconda3/include/python3.8 -c pandas/_libs/hashing.c -o build/temp.macosx-10.9-x86_64-3.8/pandas/_libs/hashing.o -Wno-unused-function
      In file included from pandas/_libs/hashing.c:566:
      In file included from /opt/anaconda3/lib/python3.8/site-packages/numpy/core/include/numpy/arrayobject.h:4:
      In file included from /opt/anaconda3/lib/python3.8/site-packages/numpy/core/include/numpy/ndarrayobject.h:12:
      In file included from /opt/anaconda3/lib/python3.8/site-packages/numpy/core/include/numpy/ndarraytypes.h:1822:
      /opt/anaconda3/lib/python3.8/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:17:2: warning: "Using deprecated NumPy API, disable it with "          "#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-W#warnings]
      #warning "Using deprecated NumPy API, disable it with " \
       ^
      1 warning generated.
      gcc -bundle -undefined dynamic_lookup -L/opt/anaconda3/lib -arch x86_64 -L/opt/anaconda3/lib -arch x86_64 -arch x86_64 build/temp.macosx-10.9-x86_64-3.8/pandas/_libs/hashing.o -o build/lib.macosx-10.9-x86_64-3.8/pandas/_libs/hashing.cpython-38-darwin.so
      building 'pandas._libs.hashtable' extension
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Ipandas/_libs/src/klib -Ipandas/_libs/src -I/opt/anaconda3/lib/python3.8/site-packages/numpy/core/include -I/opt/anaconda3/include/python3.8 -c pandas/_libs/hashtable.c -o build/temp.macosx-10.9-x86_64-3.8/pandas/_libs/hashtable.o -Wno-unused-function
      In file included from pandas/_libs/hashtable.c:567:
      In file included from /opt/anaconda3/lib/python3.8/site-packages/numpy/core/include/numpy/arrayobject.h:4:
      In file included from /opt/anaconda3/lib/python3.8/site-packages/numpy/core/include/numpy/ndarrayobject.h:12:
      In file included from /opt/anaconda3/lib/python3.8/site-packages/numpy/core/include/numpy/ndarraytypes.h:1822:
      /opt/anaconda3/lib/python3.8/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:17:2: warning: "Using deprecated NumPy API, disable it with "          "#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-W#warnings]
      #warning "Using deprecated NumPy API, disable it with " \
       ^
      pandas/_libs/hashtable.c:14482:38: warning: self-comparison always evaluates to false [-Wtautological-compare]
                __pyx_t_15 = ((__pyx_v_val != __pyx_v_val) != 0);
                                           ^
      pandas/_libs/hashtable.c:18311:38: warning: self-comparison always evaluates to false [-Wtautological-compare]
                __pyx_t_15 = ((__pyx_v_val != __pyx_v_val) != 0);
                                           ^
      pandas/_libs/hashtable.c:20466:13: warning: assigning to 'char *' from 'const char *' discards qualifiers [-Wincompatible-pointer-types-discards-qualifiers]
        __pyx_t_6 = get_c_string(__pyx_v_val); if (unlikely(__pyx_t_6 == ((char *)NULL))) __PYX_ERR(0, 1249, __pyx_L1_error)
                  ^ ~~~~~~~~~~~~~~~~~~~~~~~~~
      pandas/_libs/hashtable.c:20695:13: warning: assigning to 'char *' from 'const char *' discards qualifiers [-Wincompatible-pointer-types-discards-qualifiers]
        __pyx_t_8 = get_c_string(__pyx_t_1); if (unlikely(__pyx_t_8 == ((char *)NULL))) __PYX_ERR(0, 1263, __pyx_L1_error)
                  ^ ~~~~~~~~~~~~~~~~~~~~~~~
      pandas/_libs/hashtable.c:21061:16: warning: assigning to 'char *' from 'const char *' discards qualifiers [-Wincompatible-pointer-types-discards-qualifiers]
          __pyx_t_12 = get_c_string(__pyx_v_val); if (unlikely(__pyx_t_12 == ((char *)NULL))) __PYX_ERR(0, 1286, __pyx_L1_error)
                     ^ ~~~~~~~~~~~~~~~~~~~~~~~~~
      pandas/_libs/hashtable.c:21396:16: warning: assigning to 'char *' from 'const char *' discards qualifiers [-Wincompatible-pointer-types-discards-qualifiers]
          __pyx_t_11 = get_c_string(__pyx_v_val); if (unlikely(__pyx_t_11 == ((char *)NULL))) __PYX_ERR(0, 1316, __pyx_L1_error)
                     ^ ~~~~~~~~~~~~~~~~~~~~~~~~~
      pandas/_libs/hashtable.c:22032:18: warning: assigning to 'char *' from 'const char *' discards qualifiers [-Wincompatible-pointer-types-discards-qualifiers]
            __pyx_t_13 = get_c_string(__pyx_v_val); if (unlikely(__pyx_t_13 == ((char *)NULL))) __PYX_ERR(0, 1357, __pyx_L1_error)
                       ^ ~~~~~~~~~~~~~~~~~~~~~~~~~
      pandas/_libs/hashtable.c:22055:18: warning: assigning to 'char *' from 'const char *' discards qualifiers [-Wincompatible-pointer-types-discards-qualifiers]
            __pyx_t_13 = get_c_string(__pyx_t_6); if (unlikely(__pyx_t_13 == ((char *)NULL))) __PYX_ERR(0, 1359, __pyx_L1_error)
                       ^ ~~~~~~~~~~~~~~~~~~~~~~~
      pandas/_libs/hashtable.c:22427:17: warning: assigning to 'char *' from 'const char *' discards qualifiers [-Wincompatible-pointer-types-discards-qualifiers]
            __pyx_t_8 = get_c_string(__pyx_v_val); if (unlikely(__pyx_t_8 == ((char *)NULL))) __PYX_ERR(0, 1390, __pyx_L1_error)
                      ^ ~~~~~~~~~~~~~~~~~~~~~~~~~
      pandas/_libs/hashtable.c:22450:17: warning: assigning to 'char *' from 'const char *' discards qualifiers [-Wincompatible-pointer-types-discards-qualifiers]
            __pyx_t_8 = get_c_string(__pyx_t_4); if (unlikely(__pyx_t_8 == ((char *)NULL))) __PYX_ERR(0, 1392, __pyx_L1_error)
                      ^ ~~~~~~~~~~~~~~~~~~~~~~~
      pandas/_libs/hashtable.c:22967:18: warning: assigning to 'char *' from 'const char *' discards qualifiers [-Wincompatible-pointer-types-discards-qualifiers]
            __pyx_t_14 = get_c_string(__pyx_v_val); if (unlikely(__pyx_t_14 == ((char *)NULL))) __PYX_ERR(0, 1431, __pyx_L1_error)
                       ^ ~~~~~~~~~~~~~~~~~~~~~~~~~
      pandas/_libs/hashtable.c:27584:19: warning: comparison of integers of different signs: 'size_t' (aka 'unsigned long') and 'Py_ssize_t' (aka 'long') [-Wsign-compare]
        if (((__pyx_t_1 < __pyx_t_2) != 0)) {
              ~~~~~~~~~ ^ ~~~~~~~~~
      pandas/_libs/hashtable.c:29630:39: warning: self-comparison always evaluates to false [-Wtautological-compare]
                  __pyx_t_17 = (__pyx_v_val != __pyx_v_val);
                                            ^
      pandas/_libs/hashtable.c:29410:19: warning: comparison of integers of different signs: 'size_t' (aka 'unsigned long') and 'Py_ssize_t' (aka 'long') [-Wsign-compare]
        if (((__pyx_t_1 < __pyx_t_2) != 0)) {
              ~~~~~~~~~ ^ ~~~~~~~~~
      pandas/_libs/hashtable.c:33086:39: warning: self-comparison always evaluates to false [-Wtautological-compare]
                  __pyx_t_17 = (__pyx_v_val != __pyx_v_val);
                                            ^
      pandas/_libs/hashtable.c:32866:19: warning: comparison of integers of different signs: 'size_t' (aka 'unsigned long') and 'Py_ssize_t' (aka 'long') [-Wsign-compare]
        if (((__pyx_t_1 < __pyx_t_2) != 0)) {
              ~~~~~~~~~ ^ ~~~~~~~~~
      pandas/_libs/hashtable.c:59465:50: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
        __pyx_type_6pandas_5_libs_9hashtable_HashTable.tp_print = 0;
                                                       ^
      /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
          Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
          ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      pandas/_libs/hashtable.c:59477:56: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
        __pyx_type_6pandas_5_libs_9hashtable_UInt64HashTable.tp_print = 0;
                                                             ^
      /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
          Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
          ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      pandas/_libs/hashtable.c:59490:55: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
        __pyx_type_6pandas_5_libs_9hashtable_Int64HashTable.tp_print = 0;
                                                            ^
      /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
          Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
          ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      pandas/_libs/hashtable.c:59503:57: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
        __pyx_type_6pandas_5_libs_9hashtable_Float64HashTable.tp_print = 0;
                                                              ^
      /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
          Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
          ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      pandas/_libs/hashtable.c:59516:58: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
        __pyx_type_6pandas_5_libs_9hashtable_PyObjectHashTable.tp_print = 0;
                                                               ^
      /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
          Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
          ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      pandas/_libs/hashtable.c:59529:56: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
        __pyx_type_6pandas_5_libs_9hashtable_StringHashTable.tp_print = 0;
                                                             ^
      /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
          Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
          ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      pandas/_libs/hashtable.c:59543:52: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
        __pyx_type_6pandas_5_libs_9hashtable_Int64Vector.tp_print = 0;
                                                         ^
      /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
          Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
          ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      pandas/_libs/hashtable.c:59557:54: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
        __pyx_type_6pandas_5_libs_9hashtable_Float64Vector.tp_print = 0;
                                                           ^
      /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
          Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
          ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      pandas/_libs/hashtable.c:59571:53: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
        __pyx_type_6pandas_5_libs_9hashtable_UInt64Vector.tp_print = 0;
                                                          ^
      /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
          Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
          ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      pandas/_libs/hashtable.c:59584:53: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
        __pyx_type_6pandas_5_libs_9hashtable_StringVector.tp_print = 0;
                                                          ^
      /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
          Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
          ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      pandas/_libs/hashtable.c:59596:53: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
        __pyx_type_6pandas_5_libs_9hashtable_ObjectVector.tp_print = 0;
                                                          ^
      /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
          Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
          ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      pandas/_libs/hashtable.c:59605:51: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
        __pyx_type_6pandas_5_libs_9hashtable_Factorizer.tp_print = 0;
                                                        ^
      /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
          Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
          ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      pandas/_libs/hashtable.c:59613:56: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
        __pyx_type_6pandas_5_libs_9hashtable_Int64Factorizer.tp_print = 0;
                                                             ^
      /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
          Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
          ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      pandas/_libs/hashtable.c:59623:26: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
        __pyx_type___pyx_array.tp_print = 0;
                               ^
      /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
          Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
          ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      pandas/_libs/hashtable.c:59628:32: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
        __pyx_type___pyx_MemviewEnum.tp_print = 0;
                                     ^
      /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
          Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
          ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      pandas/_libs/hashtable.c:59643:31: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
        __pyx_type___pyx_memoryview.tp_print = 0;
                                    ^
      /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
          Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
          ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      pandas/_libs/hashtable.c:59656:36: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
        __pyx_type___pyx_memoryviewslice.tp_print = 0;
                                         ^
      /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
          Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
          ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      34 warnings generated.
      gcc -bundle -undefined dynamic_lookup -L/opt/anaconda3/lib -arch x86_64 -L/opt/anaconda3/lib -arch x86_64 -arch x86_64 build/temp.macosx-10.9-x86_64-3.8/pandas/_libs/hashtable.o -o build/lib.macosx-10.9-x86_64-3.8/pandas/_libs/hashtable.cpython-38-darwin.so
      building 'pandas._libs.index' extension
      creating build/temp.macosx-10.9-x86_64-3.8/pandas/_libs/src
      creating build/temp.macosx-10.9-x86_64-3.8/pandas/_libs/src/datetime
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Ipandas/_libs/src/klib -Ipandas/_libs/src -I/opt/anaconda3/lib/python3.8/site-packages/numpy/core/include -I/opt/anaconda3/include/python3.8 -c pandas/_libs/index.c -o build/temp.macosx-10.9-x86_64-3.8/pandas/_libs/index.o -Wno-unused-function
      In file included from pandas/_libs/index.c:567:
      In file included from /opt/anaconda3/lib/python3.8/site-packages/numpy/core/include/numpy/arrayobject.h:4:
      In file included from /opt/anaconda3/lib/python3.8/site-packages/numpy/core/include/numpy/ndarrayobject.h:12:
      In file included from /opt/anaconda3/lib/python3.8/site-packages/numpy/core/include/numpy/ndarraytypes.h:1822:
      /opt/anaconda3/lib/python3.8/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:17:2: warning: "Using deprecated NumPy API, disable it with "          "#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-W#warnings]
      #warning "Using deprecated NumPy API, disable it with " \
       ^
      pandas/_libs/index.c:48425:48: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
        __pyx_type_6pandas_5_libs_5index_IndexEngine.tp_print = 0;
                                                     ^
      /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
          Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
          ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      pandas/_libs/index.c:48441:48: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
        __pyx_type_6pandas_5_libs_5index_Int64Engine.tp_print = 0;
                                                     ^
      /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
          Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
          ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      pandas/_libs/index.c:48457:51: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
        __pyx_type_6pandas_5_libs_5index_DatetimeEngine.tp_print = 0;
                                                        ^
      /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
          Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
          ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      pandas/_libs/index.c:48470:52: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
        __pyx_type_6pandas_5_libs_5index_TimedeltaEngine.tp_print = 0;
                                                         ^
      /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
          Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
          ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      pandas/_libs/index.c:48484:49: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
        __pyx_type_6pandas_5_libs_5index_PeriodEngine.tp_print = 0;
                                                      ^
      /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
          Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
          ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      pandas/_libs/index.c:48493:62: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
        __pyx_type_6pandas_5_libs_5index_BaseMultiIndexCodesEngine.tp_print = 0;
                                                                   ^
      /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
          Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
          ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      pandas/_libs/index.c:48517:50: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
        __pyx_type_6pandas_5_libs_5index_Float64Engine.tp_print = 0;
                                                       ^
      /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
          Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
          ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      pandas/_libs/index.c:48533:49: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
        __pyx_type_6pandas_5_libs_5index_UInt64Engine.tp_print = 0;
                                                      ^
      /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
          Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
          ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      pandas/_libs/index.c:48546:49: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
        __pyx_type_6pandas_5_libs_5index_ObjectEngine.tp_print = 0;
                                                      ^
      /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
          Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
          ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      pandas/_libs/index.c:48555:65: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
        __pyx_type_6pandas_5_libs_5index___pyx_scope_struct____init__.tp_print = 0;
                                                                      ^
      /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
          Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
          ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      pandas/_libs/index.c:48563:26: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
        __pyx_type___pyx_array.tp_print = 0;
                               ^
      /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
          Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
          ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      pandas/_libs/index.c:48568:32: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
        __pyx_type___pyx_MemviewEnum.tp_print = 0;
                                     ^
      /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
          Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
          ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      pandas/_libs/index.c:48583:31: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
        __pyx_type___pyx_memoryview.tp_print = 0;
                                    ^
      /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
          Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
          ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      pandas/_libs/index.c:48596:36: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
        __pyx_type___pyx_memoryviewslice.tp_print = 0;
                                         ^
      /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
          Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
          ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      15 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Ipandas/_libs/src/klib -Ipandas/_libs/src -I/opt/anaconda3/lib/python3.8/site-packages/numpy/core/include -I/opt/anaconda3/include/python3.8 -c pandas/_libs/src/datetime/np_datetime.c -o build/temp.macosx-10.9-x86_64-3.8/pandas/_libs/src/datetime/np_datetime.o -Wno-unused-function
      In file included from pandas/_libs/src/datetime/np_datetime.c:22:
      In file included from /opt/anaconda3/lib/python3.8/site-packages/numpy/core/include/numpy/arrayobject.h:4:
      In file included from /opt/anaconda3/lib/python3.8/site-packages/numpy/core/include/numpy/ndarrayobject.h:12:
      In file included from /opt/anaconda3/lib/python3.8/site-packages/numpy/core/include/numpy/ndarraytypes.h:1822:
      /opt/anaconda3/lib/python3.8/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:17:2: warning: "Using deprecated NumPy API, disable it with "          "#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-W#warnings]
      #warning "Using deprecated NumPy API, disable it with " \
       ^
      pandas/_libs/src/datetime/np_datetime.c:518:5: error: implicit declaration of function 'convert_datetimestruct_to_datetime' is invalid in C99 [-Werror,-Wimplicit-function-declaration]
          convert_datetimestruct_to_datetime(fr, d, &result);
          ^
      pandas/_libs/src/datetime/np_datetime.c:518:5: note: did you mean 'pandas_datetimestruct_to_datetime'?
      pandas/_libs/src/datetime/np_datetime.c:514:14: note: 'pandas_datetimestruct_to_datetime' declared here
      npy_datetime pandas_datetimestruct_to_datetime(PANDAS_DATETIMEUNIT fr,
                   ^
      pandas/_libs/src/datetime/np_datetime.c:530:5: error: implicit declaration of function 'convert_timedelta_to_timedeltastruct' is invalid in C99 [-Werror,-Wimplicit-function-declaration]
          convert_timedelta_to_timedeltastruct(fr, val, result);
          ^
      pandas/_libs/src/datetime/np_datetime.c:530:5: note: did you mean 'pandas_timedelta_to_timedeltastruct'?
      pandas/_libs/src/datetime/np_datetime.c:527:6: note: 'pandas_timedelta_to_timedeltastruct' declared here
      void pandas_timedelta_to_timedeltastruct(npy_timedelta val,
           ^
      1 warning and 2 errors generated.
      error: command 'gcc' failed with exit status 1
      ----------------------------------------[0m
    [31m  ERROR: Failed building wheel for pandas[0m
    [?25h  Running setup.py clean for pandas
      Building wheel for bokeh (setup.py) ... [?25ldone
    [?25h  Created wheel for bokeh: filename=bokeh-0.13.0-py3-none-any.whl size=6228397 sha256=fedc7bbf517d3d3a22ad1c9f84cb9909f6b1b4110a8a2e5982a1d52de4c24a0a
      Stored in directory: /Users/felipe/Library/Caches/pip/wheels/45/71/87/3268e75a402cba75ac605f98c9fb3b1336a7736005a230b2b5
      Building wheel for pyproj (setup.py) ... [?25lerror
    [31m  ERROR: Command errored out with exit status 1:
       command: /opt/anaconda3/bin/python -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pyproj/setup.py'"'"'; __file__='"'"'/private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pyproj/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' bdist_wheel -d /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-wheel-k8t3_ms_
           cwd: /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pyproj/
      Complete output (2426 lines):
      using bundled proj4..
      In file included from nad2bin.c:7:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from nad2bin.c:7:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      nad2bin.c:362:21: warning: comparison of integers of different signs: 'unsigned long' and 'int' [-Wsign-compare]
                          != 4 * ct.lim.lam )
                          ^  ~~~~~~~~~~~~~~
      3 warnings generated.
      In file included from src/pj_malloc.c:5:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/pj_malloc.c:5:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      executing /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pyproj/nad2bin lib/pyproj/data/TN < datumgrid/TN.llaOutput Binary File Format: ctable2
      executing /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pyproj/nad2bin lib/pyproj/data/stlrnc < datumgrid/stlrnc.llaOutput Binary File Format: ctable2
      executing /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pyproj/nad2bin lib/pyproj/data/hawaii < datumgrid/hawaii.llaOutput Binary File Format: ctable2
      executing /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pyproj/nad2bin lib/pyproj/data/null < datumgrid/null.llaOutput Binary File Format: ctable2
      executing /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pyproj/nad2bin lib/pyproj/data/FL < datumgrid/FL.llaOutput Binary File Format: ctable2
      executing /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pyproj/nad2bin lib/pyproj/data/stpaul < datumgrid/stpaul.llaOutput Binary File Format: ctable2
      executing /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pyproj/nad2bin lib/pyproj/data/conus < datumgrid/conus.llaOutput Binary File Format: ctable2
      executing /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pyproj/nad2bin lib/pyproj/data/prvi < datumgrid/prvi.llaOutput Binary File Format: ctable2
      executing /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pyproj/nad2bin lib/pyproj/data/MD < datumgrid/MD.llaOutput Binary File Format: ctable2
      executing /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pyproj/nad2bin lib/pyproj/data/WI < datumgrid/WI.llaOutput Binary File Format: ctable2
      executing /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pyproj/nad2bin lib/pyproj/data/stgeorge < datumgrid/stgeorge.llaOutput Binary File Format: ctable2
      executing /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pyproj/nad2bin lib/pyproj/data/alaska < datumgrid/alaska.llaOutput Binary File Format: ctable2
      executing /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pyproj/nad2bin lib/pyproj/data/WO < datumgrid/WO.llaOutput Binary File Format: ctable2
      running bdist_wheel
      running build
      running build_py
      creating build
      creating build/lib.macosx-10.9-x86_64-3.8
      creating build/lib.macosx-10.9-x86_64-3.8/pyproj
      copying lib/pyproj/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pyproj
      copying lib/pyproj/datadir.py -> build/lib.macosx-10.9-x86_64-3.8/pyproj
      creating build/lib.macosx-10.9-x86_64-3.8/pyproj/data
      copying lib/pyproj/data/test27 -> build/lib.macosx-10.9-x86_64-3.8/pyproj/data
      copying lib/pyproj/data/esri.extra -> build/lib.macosx-10.9-x86_64-3.8/pyproj/data
      copying lib/pyproj/data/testvarious -> build/lib.macosx-10.9-x86_64-3.8/pyproj/data
      copying lib/pyproj/data/alaska -> build/lib.macosx-10.9-x86_64-3.8/pyproj/data
      copying lib/pyproj/data/pj_out27.dist -> build/lib.macosx-10.9-x86_64-3.8/pyproj/data
      copying lib/pyproj/data/ntv2_out.dist -> build/lib.macosx-10.9-x86_64-3.8/pyproj/data
      copying lib/pyproj/data/ntf_r93.gsb -> build/lib.macosx-10.9-x86_64-3.8/pyproj/data
      copying lib/pyproj/data/conus -> build/lib.macosx-10.9-x86_64-3.8/pyproj/data
      copying lib/pyproj/data/stpaul -> build/lib.macosx-10.9-x86_64-3.8/pyproj/data
      copying lib/pyproj/data/IGNF -> build/lib.macosx-10.9-x86_64-3.8/pyproj/data
      copying lib/pyproj/data/nad83 -> build/lib.macosx-10.9-x86_64-3.8/pyproj/data
      copying lib/pyproj/data/esri -> build/lib.macosx-10.9-x86_64-3.8/pyproj/data
      copying lib/pyproj/data/prvi -> build/lib.macosx-10.9-x86_64-3.8/pyproj/data
      copying lib/pyproj/data/pj_out83.dist -> build/lib.macosx-10.9-x86_64-3.8/pyproj/data
      copying lib/pyproj/data/testntv2 -> build/lib.macosx-10.9-x86_64-3.8/pyproj/data
      copying lib/pyproj/data/FL -> build/lib.macosx-10.9-x86_64-3.8/pyproj/data
      copying lib/pyproj/data/world -> build/lib.macosx-10.9-x86_64-3.8/pyproj/data
      copying lib/pyproj/data/README -> build/lib.macosx-10.9-x86_64-3.8/pyproj/data
      copying lib/pyproj/data/test83 -> build/lib.macosx-10.9-x86_64-3.8/pyproj/data
      copying lib/pyproj/data/nzgd2kgrid0005.gsb -> build/lib.macosx-10.9-x86_64-3.8/pyproj/data
      copying lib/pyproj/data/nad.lst -> build/lib.macosx-10.9-x86_64-3.8/pyproj/data
      copying lib/pyproj/data/null -> build/lib.macosx-10.9-x86_64-3.8/pyproj/data
      copying lib/pyproj/data/ntv1_can.dat -> build/lib.macosx-10.9-x86_64-3.8/pyproj/data
      copying lib/pyproj/data/td_out.dist -> build/lib.macosx-10.9-x86_64-3.8/pyproj/data
      copying lib/pyproj/data/MD -> build/lib.macosx-10.9-x86_64-3.8/pyproj/data
      copying lib/pyproj/data/proj_def.dat -> build/lib.macosx-10.9-x86_64-3.8/pyproj/data
      copying lib/pyproj/data/hawaii -> build/lib.macosx-10.9-x86_64-3.8/pyproj/data
      copying lib/pyproj/data/nad27 -> build/lib.macosx-10.9-x86_64-3.8/pyproj/data
      copying lib/pyproj/data/tv_out.dist -> build/lib.macosx-10.9-x86_64-3.8/pyproj/data
      copying lib/pyproj/data/stgeorge -> build/lib.macosx-10.9-x86_64-3.8/pyproj/data
      copying lib/pyproj/data/testdatumfile -> build/lib.macosx-10.9-x86_64-3.8/pyproj/data
      copying lib/pyproj/data/stlrnc -> build/lib.macosx-10.9-x86_64-3.8/pyproj/data
      copying lib/pyproj/data/GL27 -> build/lib.macosx-10.9-x86_64-3.8/pyproj/data
      copying lib/pyproj/data/proj_outIGNF.dist -> build/lib.macosx-10.9-x86_64-3.8/pyproj/data
      copying lib/pyproj/data/WI -> build/lib.macosx-10.9-x86_64-3.8/pyproj/data
      copying lib/pyproj/data/TN -> build/lib.macosx-10.9-x86_64-3.8/pyproj/data
      copying lib/pyproj/data/other.extra -> build/lib.macosx-10.9-x86_64-3.8/pyproj/data
      copying lib/pyproj/data/WO -> build/lib.macosx-10.9-x86_64-3.8/pyproj/data
      copying lib/pyproj/data/testIGNF -> build/lib.macosx-10.9-x86_64-3.8/pyproj/data
      copying lib/pyproj/data/epsg -> build/lib.macosx-10.9-x86_64-3.8/pyproj/data
      running build_ext
      building 'pyproj._proj' extension
      creating build/temp.macosx-10.9-x86_64-3.8
      creating build/temp.macosx-10.9-x86_64-3.8/src
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_putp5.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_putp5.o
      In file included from src/PJ_putp5.c:4:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_putp5.c:4:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/proj_mdist.c -o build/temp.macosx-10.9-x86_64-3.8/src/proj_mdist.o
      In file included from src/proj_mdist.c:31:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/proj_mdist.c:31:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/pj_datum_set.c -o build/temp.macosx-10.9-x86_64-3.8/src/pj_datum_set.o
      In file included from src/pj_datum_set.c:28:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/pj_datum_set.c:28:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/pj_inv.c -o build/temp.macosx-10.9-x86_64-3.8/src/pj_inv.o
      In file included from src/pj_inv.c:3:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/pj_inv.c:3:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/pj_apply_gridshift.c -o build/temp.macosx-10.9-x86_64-3.8/src/pj_apply_gridshift.o
      In file included from src/pj_apply_gridshift.c:33:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/pj_apply_gridshift.c:33:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/emess.c -o build/temp.macosx-10.9-x86_64-3.8/src/emess.o
      In file included from src/emess.c:17:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      1 warning generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/pj_param.c -o build/temp.macosx-10.9-x86_64-3.8/src/pj_param.o
      In file included from src/pj_param.c:2:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/pj_param.c:2:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_nocol.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_nocol.o
      In file included from src/PJ_nocol.c:2:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_nocol.c:2:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_eck4.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_eck4.o
      In file included from src/PJ_eck4.c:2:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_eck4.c:2:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_gins8.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_gins8.o
      In file included from src/PJ_gins8.c:2:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_gins8.c:2:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_crast.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_crast.o
      In file included from src/PJ_crast.c:2:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_crast.c:2:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/pj_ellps.c -o build/temp.macosx-10.9-x86_64-3.8/src/pj_ellps.o
      In file included from src/pj_ellps.c:3:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/pj_ellps.c:3:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_lagrng.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_lagrng.o
      In file included from src/PJ_lagrng.c:7:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_lagrng.c:7:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_denoy.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_denoy.o
      In file included from src/PJ_denoy.c:2:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_denoy.c:2:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/nad_cvt.c -o build/temp.macosx-10.9-x86_64-3.8/src/nad_cvt.o
      In file included from src/nad_cvt.c:2:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/nad_cvt.c:2:
    
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_laea.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_laea.o
      In file included from src/PJ_laea.c:13:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_laea.c:13:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_sterea.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_sterea.o
      In file included from src/PJ_sterea.c:33:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_sterea.c:33:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_mill.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_mill.o
      In file included from src/PJ_mill.c:2:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_mill.c:2:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_nell.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_nell.o
      In file included from src/PJ_nell.c:2:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_nell.c:2:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/pj_ctx.c -o build/temp.macosx-10.9-x86_64-3.8/src/pj_ctx.o
      In file included from src/pj_ctx.c:28:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/pj_ctx.c:28:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/nad_init.c -o build/temp.macosx-10.9-x86_64-3.8/src/nad_init.o
      In file included from src/nad_init.c:30:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/nad_init.c:30:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_tcc.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_tcc.o
      In file included from src/PJ_tcc.c:5:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_tcc.c:5:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_igh.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_igh.o
      In file included from src/PJ_igh.c:5:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_igh.c:5:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_chamb.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_chamb.o
      In file included from src/PJ_chamb.c:13:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_chamb.c:13:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_cc.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_cc.o
      In file included from src/PJ_cc.c:4:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_cc.c:4:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/pj_malloc.c -o build/temp.macosx-10.9-x86_64-3.8/src/pj_malloc.o
      In file included from src/pj_malloc.c:5:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/pj_malloc.c:5:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/pj_msfn.c -o build/temp.macosx-10.9-x86_64-3.8/src/pj_msfn.o
      In file included from src/pj_msfn.c:3:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/pj_msfn.c:3:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_boggs.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_boggs.o
      In file included from src/PJ_boggs.c:2:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_boggs.c:2:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_nzmg.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_nzmg.o
      In file included from src/PJ_nzmg.c:30:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_nzmg.c:30:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/pj_gauss.c -o build/temp.macosx-10.9-x86_64-3.8/src/pj_gauss.o
      In file included from src/pj_gauss.c:27:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/pj_gauss.c:27:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_tcea.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_tcea.o
      In file included from src/PJ_tcea.c:4:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_tcea.c:4:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_eqdc.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_eqdc.o
      In file included from src/PJ_eqdc.c:11:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_eqdc.c:11:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_bipc.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_bipc.o
      In file included from src/PJ_bipc.c:4:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_bipc.c:4:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_moll.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_moll.o
      In file included from src/PJ_moll.c:4:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_moll.c:4:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/pj_fwd3d.c -o build/temp.macosx-10.9-x86_64-3.8/src/pj_fwd3d.o
      In file included from src/pj_fwd3d.c:3:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/pj_fwd3d.c:3:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_robin.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_robin.o
      In file included from src/PJ_robin.c:2:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_robin.c:2:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_imw_p.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_imw_p.o
      In file included from src/PJ_imw_p.c:7:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_imw_p.c:7:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/geod_interface.c -o build/temp.macosx-10.9-x86_64-3.8/src/geod_interface.o
      In file included from src/geod_interface.c:1:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/geod_interface.c:1:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_mod_ster.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_mod_ster.o
      In file included from src/PJ_mod_ster.c:7:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_mod_ster.c:7:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_geos.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_geos.o
      In file included from src/PJ_geos.c:41:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_geos.c:41:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/pj_tsfn.c -o build/temp.macosx-10.9-x86_64-3.8/src/pj_tsfn.o
      In file included from src/pj_tsfn.c:3:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/pj_tsfn.c:3:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_vandg4.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_vandg4.o
      In file included from src/PJ_vandg4.c:2:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_vandg4.c:2:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_tmerc.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_tmerc.o
      In file included from src/PJ_tmerc.c:6:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_tmerc.c:6:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_omerc.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_omerc.o
      In file included from src/PJ_omerc.c:29:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_omerc.c:29:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_putp6.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_putp6.o
      In file included from src/PJ_putp6.c:4:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_putp6.c:4:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_aea.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_aea.o
      In file included from src/PJ_aea.c:42:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_aea.c:42:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_lsat.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_lsat.o
      In file included from src/PJ_lsat.c:6:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_lsat.c:6:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_lask.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_lask.o
      In file included from src/PJ_lask.c:3:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_lask.c:3:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/pj_datums.c -o build/temp.macosx-10.9-x86_64-3.8/src/pj_datums.o
      In file included from src/pj_datums.c:30:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/pj_datums.c:30:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_goode.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_goode.o
      In file included from src/PJ_goode.c:5:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_goode.c:5:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_aeqd.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_aeqd.o
      In file included from src/PJ_aeqd.c:41:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_aeqd.c:41:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/pj_mutex.c -o build/temp.macosx-10.9-x86_64-3.8/src/pj_mutex.o
      In file included from src/pj_mutex.c:39:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/pj_mutex.c:39:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_cea.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_cea.o
      In file included from src/PJ_cea.c:5:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_cea.c:5:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_putp2.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_putp2.o
      In file included from src/PJ_putp2.c:2:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_putp2.c:2:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_gn_sinu.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_gn_sinu.o
      In file included from src/PJ_gn_sinu.c:5:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_gn_sinu.c:5:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_krovak.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_krovak.o
      In file included from src/PJ_krovak.c:36:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_krovak.c:36:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_rpoly.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_rpoly.o
      In file included from src/PJ_rpoly.c:8:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_rpoly.c:8:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/pj_latlong.c -o build/temp.macosx-10.9-x86_64-3.8/src/pj_latlong.o
      In file included from src/pj_latlong.c:32:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/pj_latlong.c:32:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_healpix.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_healpix.o
      In file included from src/PJ_healpix.c:37:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_healpix.c:37:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/biveval.c -o build/temp.macosx-10.9-x86_64-3.8/src/biveval.o
      In file included from src/biveval.c:2:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/biveval.c:2:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/pj_errno.c -o build/temp.macosx-10.9-x86_64-3.8/src/pj_errno.o
      In file included from src/pj_errno.c:3:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/pj_errno.c:3:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_eck3.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_eck3.o
      In file included from src/PJ_eck3.c:4:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_eck3.c:4:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_gnom.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_gnom.o
      In file included from src/PJ_gnom.c:6:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_gnom.c:6:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/bchgen.c -o build/temp.macosx-10.9-x86_64-3.8/src/bchgen.o
      In file included from src/bchgen.c:2:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/bchgen.c:2:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/pj_strerrno.c -o build/temp.macosx-10.9-x86_64-3.8/src/pj_strerrno.o
      In file included from src/pj_strerrno.c:2:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/pj_strerrno.c:2:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_natearth.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_natearth.o
      In file included from src/PJ_natearth.c:17:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_natearth.c:17:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/pj_log.c -o build/temp.macosx-10.9-x86_64-3.8/src/pj_log.o
      In file included from src/pj_log.c:28:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/pj_log.c:28:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/pj_factors.c -o build/temp.macosx-10.9-x86_64-3.8/src/pj_factors.o
      In file included from src/pj_factors.c:3:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/pj_factors.c:3:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_wag2.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_wag2.o
      In file included from src/PJ_wag2.c:2:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_wag2.c:2:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_collg.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_collg.o
      In file included from src/PJ_collg.c:2:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_collg.c:2:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_labrd.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_labrd.o
      In file included from src/PJ_labrd.c:5:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_labrd.c:5:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_ortho.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_ortho.o
      In file included from src/PJ_ortho.c:6:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_ortho.c:6:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_urmfps.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_urmfps.o
      In file included from src/PJ_urmfps.c:4:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_urmfps.c:4:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/pj_ell_set.c -o build/temp.macosx-10.9-x86_64-3.8/src/pj_ell_set.o
      In file included from src/pj_ell_set.c:2:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/pj_ell_set.c:2:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/pj_strtod.c -o build/temp.macosx-10.9-x86_64-3.8/src/pj_strtod.o
      In file included from src/pj_strtod.c:30:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/pj_strtod.c:30:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      src/pj_strtod.c:83:2: warning: "localeconv not available" [-W#warnings]
      #warning "localeconv not available"
       ^
      3 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/p_series.c -o build/temp.macosx-10.9-x86_64-3.8/src/p_series.o
      In file included from src/p_series.c:2:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/p_series.c:2:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_eqc.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_eqc.o
      In file included from src/PJ_eqc.c:4:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_eqc.c:4:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_nsper.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_nsper.o
      In file included from src/PJ_nsper.c:17:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_nsper.c:17:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/pj_units.c -o build/temp.macosx-10.9-x86_64-3.8/src/pj_units.o
      In file included from src/pj_units.c:3:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/pj_units.c:3:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_mbtfpq.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_mbtfpq.o
      In file included from src/PJ_mbtfpq.c:2:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_mbtfpq.c:2:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_bonne.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_bonne.o
      In file included from src/PJ_bonne.c:8:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_bonne.c:8:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_tpeqd.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_tpeqd.o
      In file included from src/PJ_tpeqd.c:5:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_tpeqd.c:5:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/pj_zpoly1.c -o build/temp.macosx-10.9-x86_64-3.8/src/pj_zpoly1.o
      In file included from src/pj_zpoly1.c:2:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/pj_zpoly1.c:2:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/dmstor.c -o build/temp.macosx-10.9-x86_64-3.8/src/dmstor.o
      In file included from src/dmstor.c:2:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/dmstor.c:2:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_somerc.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_somerc.o
      In file included from src/PJ_somerc.c:4:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_somerc.c:4:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_cass.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_cass.o
      In file included from src/PJ_cass.c:14:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_cass.c:14:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_urm5.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_urm5.o
      In file included from src/PJ_urm5.c:4:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_urm5.c:4:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_isea.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_isea.o
      src/PJ_isea.c:921:6: warning: code will never be executed [-Wunreachable-code]
              d = v.x;
                  ^
      In file included from src/PJ_isea.c:1023:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_isea.c:1023:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      3 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_wink2.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_wink2.o
      In file included from src/PJ_wink2.c:4:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_wink2.c:4:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/pj_gridinfo.c -o build/temp.macosx-10.9-x86_64-3.8/src/pj_gridinfo.o
      In file included from src/pj_gridinfo.c:31:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/pj_gridinfo.c:31:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/pj_utils.c -o build/temp.macosx-10.9-x86_64-3.8/src/pj_utils.o
      In file included from src/pj_utils.c:31:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/pj_utils.c:31:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_putp3.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_putp3.o
      In file included from src/PJ_putp3.c:4:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_putp3.c:4:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_gstmerc.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_gstmerc.o
      In file included from src/PJ_gstmerc.c:11:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_gstmerc.c:11:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_larr.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_larr.o
      In file included from src/PJ_larr.c:3:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_larr.c:3:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_hatano.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_hatano.o
      In file included from src/PJ_hatano.c:2:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_hatano.c:2:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_aitoff.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_aitoff.o
      In file included from src/PJ_aitoff.c:33:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_aitoff.c:33:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/pj_geocent.c -o build/temp.macosx-10.9-x86_64-3.8/src/pj_geocent.o
      In file included from src/pj_geocent.c:31:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/pj_geocent.c:31:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_gall.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_gall.o
      In file included from src/PJ_gall.c:2:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_gall.c:2:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_eck2.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_eck2.o
      In file included from src/PJ_eck2.c:2:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_eck2.c:2:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/pj_phi2.c -o build/temp.macosx-10.9-x86_64-3.8/src/pj_phi2.o
      In file included from src/pj_phi2.c:2:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/pj_phi2.c:2:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/geodesic.c -o build/temp.macosx-10.9-x86_64-3.8/src/geodesic.o
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/mk_cheby.c -o build/temp.macosx-10.9-x86_64-3.8/src/mk_cheby.o
      In file included from src/mk_cheby.c:1:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/mk_cheby.c:1:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/geocent.c -o build/temp.macosx-10.9-x86_64-3.8/src/geocent.o
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/pj_qsfn.c -o build/temp.macosx-10.9-x86_64-3.8/src/pj_qsfn.o
      In file included from src/pj_qsfn.c:3:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/pj_qsfn.c:3:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/pj_apply_vgridshift.c -o build/temp.macosx-10.9-x86_64-3.8/src/pj_apply_vgridshift.o
      In file included from src/pj_apply_vgridshift.c:31:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/pj_apply_vgridshift.c:31:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_oea.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_oea.o
      In file included from src/PJ_oea.c:7:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_oea.c:7:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_wag3.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_wag3.o
      In file included from src/PJ_wag3.c:4:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_wag3.c:4:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/nad_intr.c -o build/temp.macosx-10.9-x86_64-3.8/src/nad_intr.o
      In file included from src/nad_intr.c:3:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/nad_intr.c:3:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/pj_gridcatalog.c -o build/temp.macosx-10.9-x86_64-3.8/src/pj_gridcatalog.o
      In file included from src/pj_gridcatalog.c:30:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/pj_gridcatalog.c:30:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_bacon.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_bacon.o
      In file included from src/PJ_bacon.c:7:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_bacon.c:7:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/pj_init.c -o build/temp.macosx-10.9-x86_64-3.8/src/pj_init.o
      In file included from src/pj_init.c:31:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/pj_init.c:31:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/pj_open_lib.c -o build/temp.macosx-10.9-x86_64-3.8/src/pj_open_lib.o
      In file included from src/pj_open_lib.c:32:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/pj_open_lib.c:32:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/pj_inv3d.c -o build/temp.macosx-10.9-x86_64-3.8/src/pj_inv3d.o
      In file included from src/pj_inv3d.c:3:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/pj_inv3d.c:3:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_qsc.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_qsc.o
      In file included from src/PJ_qsc.c:48:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_qsc.c:48:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/pj_fileapi.c -o build/temp.macosx-10.9-x86_64-3.8/src/pj_fileapi.o
      In file included from src/pj_fileapi.c:29:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/pj_fileapi.c:29:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      src/pj_fileapi.c:57:36: warning: this old-style function definition is not preceded by a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi()
                                         ^
      3 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_mbtfpp.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_mbtfpp.o
      In file included from src/PJ_mbtfpp.c:2:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_mbtfpp.c:2:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_airy.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_airy.o
      In file included from src/PJ_airy.c:36:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_airy.c:36:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/bch2bps.c -o build/temp.macosx-10.9-x86_64-3.8/src/bch2bps.o
      In file included from src/bch2bps.c:2:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/bch2bps.c:2:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_wag7.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_wag7.o
      In file included from src/PJ_wag7.c:2:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_wag7.c:2:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_stere.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_stere.o
      In file included from src/PJ_stere.c:8:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_stere.c:8:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/pj_transform.c -o build/temp.macosx-10.9-x86_64-3.8/src/pj_transform.o
      In file included from src/pj_transform.c:30:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/pj_transform.c:30:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_wink1.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_wink1.o
      In file included from src/PJ_wink1.c:4:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_wink1.c:4:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/hypot.c -o build/temp.macosx-10.9-x86_64-3.8/src/hypot.o
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_mbt_fps.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_mbt_fps.o
      In file included from src/PJ_mbt_fps.c:2:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_mbt_fps.c:2:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_calcofi.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_calcofi.o
      In file included from src/PJ_calcofi.c:2:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_calcofi.c:2:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_sconics.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_sconics.o
      In file included from src/PJ_sconics.c:9:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_sconics.c:9:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_putp4p.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_putp4p.o
      In file included from src/PJ_putp4p.c:4:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_putp4p.c:4:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/pj_auth.c -o build/temp.macosx-10.9-x86_64-3.8/src/pj_auth.o
      In file included from src/pj_auth.c:2:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/pj_auth.c:2:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_poly.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_poly.o
      In file included from src/PJ_poly.c:5:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_poly.c:5:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/aasincos.c -o build/temp.macosx-10.9-x86_64-3.8/src/aasincos.o
      In file included from src/aasincos.c:2:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/aasincos.c:2:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_eck5.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_eck5.o
      In file included from src/PJ_eck5.c:2:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_eck5.c:2:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/proj_rouss.c -o build/temp.macosx-10.9-x86_64-3.8/src/proj_rouss.o
      In file included from src/proj_rouss.c:34:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/proj_rouss.c:34:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_fouc_s.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_fouc_s.o
      In file included from src/PJ_fouc_s.c:4:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_fouc_s.c:4:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_lcca.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_lcca.o
      In file included from src/PJ_lcca.c:10:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_lcca.c:10:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
    
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/pj_deriv.c -o build/temp.macosx-10.9-x86_64-3.8/src/pj_deriv.o
      In file included from src/pj_deriv.c:3:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/pj_deriv.c:3:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_eck1.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_eck1.o
      In file included from src/PJ_eck1.c:2:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_eck1.c:2:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_vandg2.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_vandg2.o
      In file included from src/PJ_vandg2.c:6:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_vandg2.c:6:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_vandg.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_vandg.o
      In file included from src/PJ_vandg.c:2:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_vandg.c:2:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_august.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_august.o
      In file included from src/PJ_august.c:2:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_august.c:2:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/adjlon.c -o build/temp.macosx-10.9-x86_64-3.8/src/adjlon.o
      In file included from src/adjlon.c:3:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/adjlon.c:3:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/rtodms.c -o build/temp.macosx-10.9-x86_64-3.8/src/rtodms.o
      In file included from src/rtodms.c:2:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/rtodms.c:2:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/pj_gridlist.c -o build/temp.macosx-10.9-x86_64-3.8/src/pj_gridlist.o
      In file included from src/pj_gridlist.c:31:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/pj_gridlist.c:31:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_loxim.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_loxim.o
      In file included from src/PJ_loxim.c:6:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_loxim.c:6:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/vector1.c -o build/temp.macosx-10.9-x86_64-3.8/src/vector1.o
      In file included from src/vector1.c:3:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/vector1.c:3:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_nell_h.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_nell_h.o
      In file included from src/PJ_nell_h.c:2:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_nell_h.c:2:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_ob_tran.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_ob_tran.o
      In file included from src/PJ_ob_tran.c:6:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_ob_tran.c:6:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/proj_etmerc.c -o build/temp.macosx-10.9-x86_64-3.8/src/proj_etmerc.o
      In file included from src/proj_etmerc.c:51:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/proj_etmerc.c:51:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/pj_mlfn.c -o build/temp.macosx-10.9-x86_64-3.8/src/pj_mlfn.o
      In file included from src/pj_mlfn.c:1:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/pj_mlfn.c:1:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/geod_set.c -o build/temp.macosx-10.9-x86_64-3.8/src/geod_set.o
      In file included from src/geod_set.c:5:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/geod_set.c:5:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/pj_initcache.c -o build/temp.macosx-10.9-x86_64-3.8/src/pj_initcache.o
      In file included from src/pj_initcache.c:28:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/pj_initcache.c:28:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/pj_pr_list.c -o build/temp.macosx-10.9-x86_64-3.8/src/pj_pr_list.o
      In file included from src/pj_pr_list.c:2:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/pj_pr_list.c:2:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_sch.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_sch.o
      In file included from src/PJ_sch.c:49:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_sch.c:49:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_fahey.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_fahey.o
      In file included from src/PJ_fahey.c:2:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_fahey.c:2:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_merc.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_merc.o
      In file included from src/PJ_merc.c:2:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_merc.c:2:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/pj_release.c -o build/temp.macosx-10.9-x86_64-3.8/src/pj_release.o
      In file included from src/pj_release.c:3:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/pj_release.c:3:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/pj_fwd.c -o build/temp.macosx-10.9-x86_64-3.8/src/pj_fwd.o
      In file included from src/pj_fwd.c:3:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/pj_fwd.c:3:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_hammer.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_hammer.o
      In file included from src/PJ_hammer.c:6:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_hammer.c:6:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_lcc.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_lcc.o
      In file included from src/PJ_lcc.c:9:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_lcc.c:9:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/pj_gc_reader.c -o build/temp.macosx-10.9-x86_64-3.8/src/pj_gc_reader.o
      In file included from src/pj_gc_reader.c:30:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/pj_gc_reader.c:30:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/pj_list.c -o build/temp.macosx-10.9-x86_64-3.8/src/pj_list.o
      In file included from src/pj_list.c:5:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/pj_list.c:5:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_sts.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_sts.o
      In file included from src/PJ_sts.c:5:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_sts.c:5:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/gen_cheb.c -o build/temp.macosx-10.9-x86_64-3.8/src/gen_cheb.o
      In file included from src/gen_cheb.c:3:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/gen_cheb.c:3:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c src/PJ_ocea.c -o build/temp.macosx-10.9-x86_64-3.8/src/PJ_ocea.o
      In file included from src/PJ_ocea.c:9:
      In file included from src/projects.h:292:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      In file included from src/PJ_ocea.c:9:
      src/projects.h:486:25: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      void pj_deallocate_grids();
                              ^
                               void
      2 warnings generated.
      gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Isrc -I/opt/anaconda3/include/python3.8 -c _proj.c -o build/temp.macosx-10.9-x86_64-3.8/_proj.o
      In file included from _proj.c:241:
      src/proj_api.h:147:36: warning: this function declaration is not a prototype [-Wstrict-prototypes]
      projFileAPI *pj_get_default_fileapi();
                                         ^
                                          void
      _proj.c:1606:17: warning: 'PyObject_AsWriteBuffer' is deprecated [-Wdeprecated-declarations]
        __pyx_t_1 = ((PyObject_AsWriteBuffer(__pyx_v_lons, (&__pyx_v_londata), (&__pyx_v_buflenx)) != 0) != 0);
                      ^
      /opt/anaconda3/include/python3.8/abstract.h:347:1: note: 'PyObject_AsWriteBuffer' has been explicitly marked deprecated here
      Py_DEPRECATED(3.0)
      ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      _proj.c:1635:17: warning: 'PyObject_AsWriteBuffer' is deprecated [-Wdeprecated-declarations]
        __pyx_t_1 = ((PyObject_AsWriteBuffer(__pyx_v_lats, (&__pyx_v_latdata), (&__pyx_v_bufleny)) != 0) != 0);
                      ^
      /opt/anaconda3/include/python3.8/abstract.h:347:1: note: 'PyObject_AsWriteBuffer' has been explicitly marked deprecated here
      Py_DEPRECATED(3.0)
      ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      _proj.c:2296:17: warning: 'PyObject_AsWriteBuffer' is deprecated [-Wdeprecated-declarations]
        __pyx_t_1 = ((PyObject_AsWriteBuffer(__pyx_v_x, (&__pyx_v_xdata), (&__pyx_v_buflenx)) != 0) != 0);
                      ^
      /opt/anaconda3/include/python3.8/abstract.h:347:1: note: 'PyObject_AsWriteBuffer' has been explicitly marked deprecated here
      Py_DEPRECATED(3.0)
      ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      _proj.c:2325:17: warning: 'PyObject_AsWriteBuffer' is deprecated [-Wdeprecated-declarations]
        __pyx_t_1 = ((PyObject_AsWriteBuffer(__pyx_v_y, (&__pyx_v_ydata), (&__pyx_v_bufleny)) != 0) != 0);
                      ^
      /opt/anaconda3/include/python3.8/abstract.h:347:1: note: 'PyObject_AsWriteBuffer' has been explicitly marked deprecated here
      Py_DEPRECATED(3.0)
      ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      _proj.c:3408:17: warning: 'PyObject_AsWriteBuffer' is deprecated [-Wdeprecated-declarations]
        __pyx_t_1 = ((PyObject_AsWriteBuffer(__pyx_v_inx, (&__pyx_v_xdata), (&__pyx_v_buflenx)) != 0) != 0);
                      ^
      /opt/anaconda3/include/python3.8/abstract.h:347:1: note: 'PyObject_AsWriteBuffer' has been explicitly marked deprecated here
      Py_DEPRECATED(3.0)
      ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      _proj.c:3437:17: warning: 'PyObject_AsWriteBuffer' is deprecated [-Wdeprecated-declarations]
        __pyx_t_1 = ((PyObject_AsWriteBuffer(__pyx_v_iny, (&__pyx_v_ydata), (&__pyx_v_bufleny)) != 0) != 0);
                      ^
      /opt/anaconda3/include/python3.8/abstract.h:347:1: note: 'PyObject_AsWriteBuffer' has been explicitly marked deprecated here
      Py_DEPRECATED(3.0)
      ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      _proj.c:3477:19: warning: 'PyObject_AsWriteBuffer' is deprecated [-Wdeprecated-declarations]
          __pyx_t_2 = ((PyObject_AsWriteBuffer(__pyx_v_inz, (&__pyx_v_zdata), (&__pyx_v_buflenz)) != 0) != 0);
                        ^
      /opt/anaconda3/include/python3.8/abstract.h:347:1: note: 'PyObject_AsWriteBuffer' has been explicitly marked deprecated here
      Py_DEPRECATED(3.0)
      ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      _proj.c:4412:17: warning: 'PyObject_AsWriteBuffer' is deprecated [-Wdeprecated-declarations]
        __pyx_t_1 = ((PyObject_AsWriteBuffer(__pyx_v_lons, (&__pyx_v_londata), (&__pyx_v_buflenlons)) != 0) != 0);
                      ^
      /opt/anaconda3/include/python3.8/abstract.h:347:1: note: 'PyObject_AsWriteBuffer' has been explicitly marked deprecated here
      Py_DEPRECATED(3.0)
      ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      _proj.c:4441:17: warning: 'PyObject_AsWriteBuffer' is deprecated [-Wdeprecated-declarations]
        __pyx_t_1 = ((PyObject_AsWriteBuffer(__pyx_v_lats, (&__pyx_v_latdata), (&__pyx_v_buflenlats)) != 0) != 0);
                      ^
      /opt/anaconda3/include/python3.8/abstract.h:347:1: note: 'PyObject_AsWriteBuffer' has been explicitly marked deprecated here
      Py_DEPRECATED(3.0)
      ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      _proj.c:4470:17: warning: 'PyObject_AsWriteBuffer' is deprecated [-Wdeprecated-declarations]
        __pyx_t_1 = ((PyObject_AsWriteBuffer(__pyx_v_az, (&__pyx_v_azdat), (&__pyx_v_buflenaz)) != 0) != 0);
                      ^
      /opt/anaconda3/include/python3.8/abstract.h:347:1: note: 'PyObject_AsWriteBuffer' has been explicitly marked deprecated here
      Py_DEPRECATED(3.0)
      ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      _proj.c:4499:17: warning: 'PyObject_AsWriteBuffer' is deprecated [-Wdeprecated-declarations]
        __pyx_t_1 = ((PyObject_AsWriteBuffer(__pyx_v_dist, (&__pyx_v_distdat), (&__pyx_v_buflend)) != 0) != 0);
                      ^
      /opt/anaconda3/include/python3.8/abstract.h:347:1: note: 'PyObject_AsWriteBuffer' has been explicitly marked deprecated here
      Py_DEPRECATED(3.0)
      ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      _proj.c:5065:17: warning: 'PyObject_AsWriteBuffer' is deprecated [-Wdeprecated-declarations]
        __pyx_t_1 = ((PyObject_AsWriteBuffer(__pyx_v_lons1, (&__pyx_v_londata), (&__pyx_v_buflenlons)) != 0) != 0);
                      ^
      /opt/anaconda3/include/python3.8/abstract.h:347:1: note: 'PyObject_AsWriteBuffer' has been explicitly marked deprecated here
      Py_DEPRECATED(3.0)
      ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      _proj.c:5094:17: warning: 'PyObject_AsWriteBuffer' is deprecated [-Wdeprecated-declarations]
        __pyx_t_1 = ((PyObject_AsWriteBuffer(__pyx_v_lats1, (&__pyx_v_latdata), (&__pyx_v_buflenlats)) != 0) != 0);
                      ^
      /opt/anaconda3/include/python3.8/abstract.h:347:1: note: 'PyObject_AsWriteBuffer' has been explicitly marked deprecated here
      Py_DEPRECATED(3.0)
      ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      _proj.c:5123:17: warning: 'PyObject_AsWriteBuffer' is deprecated [-Wdeprecated-declarations]
        __pyx_t_1 = ((PyObject_AsWriteBuffer(__pyx_v_lons2, (&__pyx_v_azdat), (&__pyx_v_buflenaz)) != 0) != 0);
                      ^
      /opt/anaconda3/include/python3.8/abstract.h:347:1: note: 'PyObject_AsWriteBuffer' has been explicitly marked deprecated here
      Py_DEPRECATED(3.0)
      ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      _proj.c:5152:17: warning: 'PyObject_AsWriteBuffer' is deprecated [-Wdeprecated-declarations]
        __pyx_t_1 = ((PyObject_AsWriteBuffer(__pyx_v_lats2, (&__pyx_v_distdat), (&__pyx_v_buflend)) != 0) != 0);
                      ^
      /opt/anaconda3/include/python3.8/abstract.h:347:1: note: 'PyObject_AsWriteBuffer' has been explicitly marked deprecated here
      Py_DEPRECATED(3.0)
      ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      _proj.c:6770:26: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
        __pyx_type_5_proj_Proj.tp_print = 0;
                               ^
      /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
          Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
          ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      _proj.c:6774:26: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
        __pyx_type_5_proj_Geod.tp_print = 0;
                               ^
      /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
          Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
          ^
      /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
      #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                           ^
      _proj.c:7421:21: error: no member named 'exc_type' in 'struct _ts'
          *type = tstate->exc_type;
                  ~~~~~~  ^
      _proj.c:7422:22: error: no member named 'exc_value' in 'struct _ts'; did you mean 'curexc_value'?
          *value = tstate->exc_value;
                           ^~~~~~~~~
                           curexc_value
      /opt/anaconda3/include/python3.8/cpython/pystate.h:80:15: note: 'curexc_value' declared here
          PyObject *curexc_value;
                    ^
      _proj.c:7423:19: error: no member named 'exc_traceback' in 'struct _ts'; did you mean 'curexc_traceback'?
          *tb = tstate->exc_traceback;
                        ^~~~~~~~~~~~~
                        curexc_traceback
      /opt/anaconda3/include/python3.8/cpython/pystate.h:81:15: note: 'curexc_traceback' declared here
          PyObject *curexc_traceback;
                    ^
      _proj.c:7435:24: error: no member named 'exc_type' in 'struct _ts'
          tmp_type = tstate->exc_type;
                     ~~~~~~  ^
      _proj.c:7436:25: error: no member named 'exc_value' in 'struct _ts'; did you mean 'curexc_value'?
          tmp_value = tstate->exc_value;
                              ^~~~~~~~~
                              curexc_value
      /opt/anaconda3/include/python3.8/cpython/pystate.h:80:15: note: 'curexc_value' declared here
          PyObject *curexc_value;
                    ^
      _proj.c:7437:22: error: no member named 'exc_traceback' in 'struct _ts'; did you mean 'curexc_traceback'?
          tmp_tb = tstate->exc_traceback;
                           ^~~~~~~~~~~~~
                           curexc_traceback
      /opt/anaconda3/include/python3.8/cpython/pystate.h:81:15: note: 'curexc_traceback' declared here
          PyObject *curexc_traceback;
                    ^
      _proj.c:7438:13: error: no member named 'exc_type' in 'struct _ts'
          tstate->exc_type = type;
          ~~~~~~  ^
      _proj.c:7439:13: error: no member named 'exc_value' in 'struct _ts'; did you mean 'curexc_value'?
          tstate->exc_value = value;
                  ^~~~~~~~~
                  curexc_value
      /opt/anaconda3/include/python3.8/cpython/pystate.h:80:15: note: 'curexc_value' declared here
          PyObject *curexc_value;
                    ^
      _proj.c:7440:13: error: no member named 'exc_traceback' in 'struct _ts'; did you mean 'curexc_traceback'?
          tstate->exc_traceback = tb;
                  ^~~~~~~~~~~~~
                  curexc_traceback
      /opt/anaconda3/include/python3.8/cpython/pystate.h:81:15: note: 'curexc_traceback' declared here
          PyObject *curexc_traceback;
                    ^
      _proj.c:7483:24: error: no member named 'exc_type' in 'struct _ts'
          tmp_type = tstate->exc_type;
                     ~~~~~~  ^
      _proj.c:7484:25: error: no member named 'exc_value' in 'struct _ts'; did you mean 'curexc_value'?
          tmp_value = tstate->exc_value;
                              ^~~~~~~~~
                              curexc_value
      /opt/anaconda3/include/python3.8/cpython/pystate.h:80:15: note: 'curexc_value' declared here
          PyObject *curexc_value;
                    ^
      _proj.c:7485:22: error: no member named 'exc_traceback' in 'struct _ts'; did you mean 'curexc_traceback'?
          tmp_tb = tstate->exc_traceback;
                           ^~~~~~~~~~~~~
                           curexc_traceback
      /opt/anaconda3/include/python3.8/cpython/pystate.h:81:15: note: 'curexc_traceback' declared here
          PyObject *curexc_traceback;
                    ^
      _proj.c:7486:13: error: no member named 'exc_type' in 'struct _ts'
          tstate->exc_type = local_type;
          ~~~~~~  ^
      _proj.c:7487:13: error: no member named 'exc_value' in 'struct _ts'; did you mean 'curexc_value'?
          tstate->exc_value = local_value;
                  ^~~~~~~~~
                  curexc_value
      /opt/anaconda3/include/python3.8/cpython/pystate.h:80:15: note: 'curexc_value' declared here
          PyObject *curexc_value;
                    ^
      _proj.c:7488:13: error: no member named 'exc_traceback' in 'struct _ts'; did you mean 'curexc_traceback'?
          tstate->exc_traceback = local_tb;
                  ^~~~~~~~~~~~~
                  curexc_traceback
      /opt/anaconda3/include/python3.8/cpython/pystate.h:81:15: note: 'curexc_traceback' declared here
          PyObject *curexc_traceback;
                    ^
      18 warnings and 15 errors generated.
      error: command 'gcc' failed with exit status 1
      ----------------------------------------[0m
    [31m  ERROR: Failed building wheel for pyproj[0m
    [?25h  Running setup.py clean for pyproj
    Successfully built bokeh
    Failed to build pandas pyproj
    Installing collected packages: pandas, bokeh, pyproj
      Attempting uninstall: pandas
        Found existing installation: pandas 1.1.3
        Uninstalling pandas-1.1.3:
          Successfully uninstalled pandas-1.1.3
        Running setup.py install for pandas ... [?25lerror
    [31m    ERROR: Command errored out with exit status 1:
         command: /opt/anaconda3/bin/python -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pandas/setup.py'"'"'; __file__='"'"'/private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pandas/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' install --record /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-record-8nfssjdm/install-record.txt --single-version-externally-managed --compile --install-headers /opt/anaconda3/include/python3.8/pandas
             cwd: /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pandas/
        Complete output (1663 lines):
        running install
        running build
        running build_py
        creating build
        creating build/lib.macosx-10.9-x86_64-3.8
        creating build/lib.macosx-10.9-x86_64-3.8/pandas
        copying pandas/conftest.py -> build/lib.macosx-10.9-x86_64-3.8/pandas
        copying pandas/_version.py -> build/lib.macosx-10.9-x86_64-3.8/pandas
        copying pandas/lib.py -> build/lib.macosx-10.9-x86_64-3.8/pandas
        copying pandas/tslib.py -> build/lib.macosx-10.9-x86_64-3.8/pandas
        copying pandas/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas
        copying pandas/parser.py -> build/lib.macosx-10.9-x86_64-3.8/pandas
        copying pandas/testing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas
        copying pandas/json.py -> build/lib.macosx-10.9-x86_64-3.8/pandas
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tools
        copying pandas/tools/merge.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tools
        copying pandas/tools/plotting.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tools
        copying pandas/tools/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tools
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/compat
        copying pandas/compat/chainmap_impl.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/compat
        copying pandas/compat/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/compat
        copying pandas/compat/chainmap.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/compat
        copying pandas/compat/pickle_compat.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/compat
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/types
        copying pandas/types/concat.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/types
        copying pandas/types/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/types
        copying pandas/types/common.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/types
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/core
        copying pandas/core/accessor.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
        copying pandas/core/categorical.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
        copying pandas/core/nanops.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
        copying pandas/core/missing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
        copying pandas/core/internals.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
        copying pandas/core/algorithms.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
        copying pandas/core/config.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
        copying pandas/core/resample.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
        copying pandas/core/window.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
        copying pandas/core/index.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
        copying pandas/core/config_init.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
        copying pandas/core/generic.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
        copying pandas/core/series.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
        copying pandas/core/sorting.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
        copying pandas/core/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
        copying pandas/core/datetools.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
        copying pandas/core/api.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
        copying pandas/core/ops.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
        copying pandas/core/common.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
        copying pandas/core/frame.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
        copying pandas/core/indexing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
        copying pandas/core/panel.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
        copying pandas/core/base.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
        copying pandas/core/strings.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
        copying pandas/core/apply.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/formats
        copying pandas/formats/style.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/formats
        copying pandas/formats/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/formats
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/util
        copying pandas/util/_depr_module.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/util
        copying pandas/util/_test_decorators.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/util
        copying pandas/util/_validators.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/util
        copying pandas/util/_print_versions.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/util
        copying pandas/util/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/util
        copying pandas/util/_decorators.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/util
        copying pandas/util/_doctools.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/util
        copying pandas/util/testing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/util
        copying pandas/util/_tester.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/util
        copying pandas/util/decorators.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/util
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/io
        copying pandas/io/feather_format.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io
        copying pandas/io/parquet.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io
        copying pandas/io/pytables.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io
        copying pandas/io/html.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io
        copying pandas/io/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io
        copying pandas/io/clipboards.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io
        copying pandas/io/parsers.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io
        copying pandas/io/excel.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io
        copying pandas/io/api.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io
        copying pandas/io/common.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io
        copying pandas/io/date_converters.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io
        copying pandas/io/pickle.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io
        copying pandas/io/sql.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io
        copying pandas/io/s3.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io
        copying pandas/io/packers.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io
        copying pandas/io/stata.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io
        copying pandas/io/gbq.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tseries
        copying pandas/tseries/plotting.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tseries
        copying pandas/tseries/converter.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tseries
        copying pandas/tseries/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tseries
        copying pandas/tseries/api.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tseries
        copying pandas/tseries/offsets.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tseries
        copying pandas/tseries/frequencies.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tseries
        copying pandas/tseries/holiday.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tseries
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests
        copying pandas/tests/test_expressions.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests
        copying pandas/tests/test_register_accessor.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests
        copying pandas/tests/test_common.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests
        copying pandas/tests/test_downstream.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests
        copying pandas/tests/test_errors.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests
        copying pandas/tests/test_sorting.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests
        copying pandas/tests/test_join.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests
        copying pandas/tests/test_panel.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests
        copying pandas/tests/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests
        copying pandas/tests/test_lib.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests
        copying pandas/tests/test_resample.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests
        copying pandas/tests/test_nanops.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests
        copying pandas/tests/test_take.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests
        copying pandas/tests/test_algos.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests
        copying pandas/tests/test_multilevel.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests
        copying pandas/tests/test_compat.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests
        copying pandas/tests/test_config.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests
        copying pandas/tests/test_window.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests
        copying pandas/tests/test_strings.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests
        copying pandas/tests/test_base.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/computation
        copying pandas/computation/expressions.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/computation
        copying pandas/computation/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/computation
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/_libs
        copying pandas/_libs/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/_libs
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/plotting
        copying pandas/plotting/_converter.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/plotting
        copying pandas/plotting/_tools.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/plotting
        copying pandas/plotting/_style.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/plotting
        copying pandas/plotting/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/plotting
        copying pandas/plotting/_core.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/plotting
        copying pandas/plotting/_timeseries.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/plotting
        copying pandas/plotting/_compat.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/plotting
        copying pandas/plotting/_misc.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/plotting
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/api
        copying pandas/api/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/api
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/errors
        copying pandas/errors/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/errors
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/compat/numpy
        copying pandas/compat/numpy/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/compat/numpy
        copying pandas/compat/numpy/function.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/compat/numpy
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/core/reshape
        copying pandas/core/reshape/tile.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/reshape
        copying pandas/core/reshape/merge.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/reshape
        copying pandas/core/reshape/concat.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/reshape
        copying pandas/core/reshape/util.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/reshape
        copying pandas/core/reshape/reshape.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/reshape
        copying pandas/core/reshape/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/reshape
        copying pandas/core/reshape/api.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/reshape
        copying pandas/core/reshape/melt.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/reshape
        copying pandas/core/reshape/pivot.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/reshape
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/core/tools
        copying pandas/core/tools/timedeltas.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/tools
        copying pandas/core/tools/datetimes.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/tools
        copying pandas/core/tools/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/tools
        copying pandas/core/tools/numeric.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/tools
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/core/util
        copying pandas/core/util/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/util
        copying pandas/core/util/hashing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/util
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/core/dtypes
        copying pandas/core/dtypes/cast.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/dtypes
        copying pandas/core/dtypes/missing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/dtypes
        copying pandas/core/dtypes/concat.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/dtypes
        copying pandas/core/dtypes/generic.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/dtypes
        copying pandas/core/dtypes/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/dtypes
        copying pandas/core/dtypes/dtypes.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/dtypes
        copying pandas/core/dtypes/api.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/dtypes
        copying pandas/core/dtypes/common.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/dtypes
        copying pandas/core/dtypes/inference.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/dtypes
        copying pandas/core/dtypes/base.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/dtypes
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/core/groupby
        copying pandas/core/groupby/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/groupby
        copying pandas/core/groupby/groupby.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/groupby
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/core/computation
        copying pandas/core/computation/check.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/computation
        copying pandas/core/computation/align.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/computation
        copying pandas/core/computation/pytables.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/computation
        copying pandas/core/computation/engines.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/computation
        copying pandas/core/computation/expressions.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/computation
        copying pandas/core/computation/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/computation
        copying pandas/core/computation/api.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/computation
        copying pandas/core/computation/ops.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/computation
        copying pandas/core/computation/common.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/computation
        copying pandas/core/computation/eval.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/computation
        copying pandas/core/computation/scope.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/computation
        copying pandas/core/computation/expr.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/computation
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/core/arrays
        copying pandas/core/arrays/categorical.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/arrays
        copying pandas/core/arrays/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/arrays
        copying pandas/core/arrays/base.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/arrays
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/core/sparse
        copying pandas/core/sparse/scipy_sparse.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/sparse
        copying pandas/core/sparse/series.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/sparse
        copying pandas/core/sparse/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/sparse
        copying pandas/core/sparse/api.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/sparse
        copying pandas/core/sparse/frame.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/sparse
        copying pandas/core/sparse/array.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/sparse
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/core/indexes
        copying pandas/core/indexes/accessors.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/indexes
        copying pandas/core/indexes/interval.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/indexes
        copying pandas/core/indexes/timedeltas.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/indexes
        copying pandas/core/indexes/range.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/indexes
        copying pandas/core/indexes/datetimes.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/indexes
        copying pandas/core/indexes/multi.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/indexes
        copying pandas/core/indexes/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/indexes
        copying pandas/core/indexes/api.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/indexes
        copying pandas/core/indexes/period.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/indexes
        copying pandas/core/indexes/frozen.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/indexes
        copying pandas/core/indexes/numeric.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/indexes
        copying pandas/core/indexes/datetimelike.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/indexes
        copying pandas/core/indexes/base.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/indexes
        copying pandas/core/indexes/category.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/core/indexes
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/io/msgpack
        copying pandas/io/msgpack/_version.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/msgpack
        copying pandas/io/msgpack/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/msgpack
        copying pandas/io/msgpack/exceptions.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/msgpack
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/io/formats
        copying pandas/io/formats/console.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/formats
        copying pandas/io/formats/style.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/formats
        copying pandas/io/formats/terminal.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/formats
        copying pandas/io/formats/html.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/formats
        copying pandas/io/formats/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/formats
        copying pandas/io/formats/format.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/formats
        copying pandas/io/formats/excel.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/formats
        copying pandas/io/formats/css.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/formats
        copying pandas/io/formats/csvs.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/formats
        copying pandas/io/formats/latex.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/formats
        copying pandas/io/formats/printing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/formats
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/io/json
        copying pandas/io/json/normalize.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/json
        copying pandas/io/json/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/json
        copying pandas/io/json/table_schema.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/json
        copying pandas/io/json/json.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/json
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/io/sas
        copying pandas/io/sas/sas7bdat.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/sas
        copying pandas/io/sas/sas_constants.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/sas
        copying pandas/io/sas/sasreader.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/sas
        copying pandas/io/sas/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/sas
        copying pandas/io/sas/sas_xport.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/sas
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/io/clipboard
        copying pandas/io/clipboard/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/clipboard
        copying pandas/io/clipboard/clipboards.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/clipboard
        copying pandas/io/clipboard/exceptions.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/clipboard
        copying pandas/io/clipboard/windows.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/clipboard
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
        copying pandas/tests/series/test_alter_axes.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
        copying pandas/tests/series/test_period.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
        copying pandas/tests/series/test_timeseries.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
        copying pandas/tests/series/test_constructors.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
        copying pandas/tests/series/test_missing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
        copying pandas/tests/series/test_sorting.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
        copying pandas/tests/series/test_timezones.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
        copying pandas/tests/series/test_operators.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
        copying pandas/tests/series/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
        copying pandas/tests/series/test_subclass.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
        copying pandas/tests/series/test_analytics.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
        copying pandas/tests/series/test_io.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
        copying pandas/tests/series/test_apply.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
        copying pandas/tests/series/test_quantile.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
        copying pandas/tests/series/test_datetime_values.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
        copying pandas/tests/series/test_internals.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
        copying pandas/tests/series/common.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
        copying pandas/tests/series/test_repr.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
        copying pandas/tests/series/test_validate.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
        copying pandas/tests/series/test_asof.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
        copying pandas/tests/series/test_api.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
        copying pandas/tests/series/test_rank.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
        copying pandas/tests/series/test_arithmetic.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
        copying pandas/tests/series/test_replace.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
        copying pandas/tests/series/test_combine_concat.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
        copying pandas/tests/series/test_dtypes.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape
        copying pandas/tests/reshape/test_union_categoricals.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape
        copying pandas/tests/reshape/test_tile.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape
        copying pandas/tests/reshape/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape
        copying pandas/tests/reshape/test_pivot.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape
        copying pandas/tests/reshape/test_reshape.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape
        copying pandas/tests/reshape/test_util.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape
        copying pandas/tests/reshape/test_melt.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape
        copying pandas/tests/reshape/test_concat.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tools
        copying pandas/tests/tools/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tools
        copying pandas/tests/tools/test_numeric.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tools
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension
        copying pandas/tests/extension/test_external_block.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension
        copying pandas/tests/extension/conftest.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension
        copying pandas/tests/extension/test_common.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension
        copying pandas/tests/extension/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/util
        copying pandas/tests/util/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/util
        copying pandas/tests/util/test_util.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/util
        copying pandas/tests/util/test_hashing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/util
        copying pandas/tests/util/test_testing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/util
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io
        copying pandas/tests/io/test_parquet.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io
        copying pandas/tests/io/conftest.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io
        copying pandas/tests/io/test_common.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io
        copying pandas/tests/io/test_pickle.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io
        copying pandas/tests/io/test_clipboard.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io
        copying pandas/tests/io/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io
        copying pandas/tests/io/test_stata.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io
        copying pandas/tests/io/test_html.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io
        copying pandas/tests/io/test_pytables.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io
        copying pandas/tests/io/test_sql.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io
        copying pandas/tests/io/test_gbq.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io
        copying pandas/tests/io/test_feather.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io
        copying pandas/tests/io/generate_legacy_storage_files.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io
        copying pandas/tests/io/test_excel.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io
        copying pandas/tests/io/test_s3.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io
        copying pandas/tests/io/test_packers.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tseries
        copying pandas/tests/tseries/conftest.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tseries
        copying pandas/tests/tseries/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tseries
        copying pandas/tests/tseries/test_frequencies.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tseries
        copying pandas/tests/tseries/test_holiday.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tseries
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
        copying pandas/tests/frame/test_block_internals.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
        copying pandas/tests/frame/test_alter_axes.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
        copying pandas/tests/frame/test_period.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
        copying pandas/tests/frame/test_axis_select_reindex.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
        copying pandas/tests/frame/test_convert_to.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
        copying pandas/tests/frame/test_timeseries.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
        copying pandas/tests/frame/test_constructors.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
        copying pandas/tests/frame/test_mutate_columns.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
        copying pandas/tests/frame/test_missing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
        copying pandas/tests/frame/test_sorting.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
        copying pandas/tests/frame/test_query_eval.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
        copying pandas/tests/frame/test_join.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
        copying pandas/tests/frame/test_timezones.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
        copying pandas/tests/frame/test_sort_values_level_as_str.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
        copying pandas/tests/frame/test_operators.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
        copying pandas/tests/frame/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
        copying pandas/tests/frame/test_subclass.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
        copying pandas/tests/frame/test_reshape.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
        copying pandas/tests/frame/test_analytics.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
        copying pandas/tests/frame/test_apply.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
        copying pandas/tests/frame/test_quantile.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
        copying pandas/tests/frame/test_indexing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
        copying pandas/tests/frame/test_repr_info.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
        copying pandas/tests/frame/common.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
        copying pandas/tests/frame/test_nonunique_indexes.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
        copying pandas/tests/frame/test_validate.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
        copying pandas/tests/frame/test_asof.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
        copying pandas/tests/frame/test_api.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
        copying pandas/tests/frame/test_rank.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
        copying pandas/tests/frame/test_arithmetic.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
        copying pandas/tests/frame/test_replace.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
        copying pandas/tests/frame/test_combine_concat.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
        copying pandas/tests/frame/test_dtypes.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
        copying pandas/tests/frame/test_to_csv.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/frame
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/dtypes
        copying pandas/tests/dtypes/test_inference.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/dtypes
        copying pandas/tests/dtypes/test_common.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/dtypes
        copying pandas/tests/dtypes/test_cast.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/dtypes
        copying pandas/tests/dtypes/test_missing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/dtypes
        copying pandas/tests/dtypes/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/dtypes
        copying pandas/tests/dtypes/test_generic.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/dtypes
        copying pandas/tests/dtypes/test_concat.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/dtypes
        copying pandas/tests/dtypes/test_dtypes.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/dtypes
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/categorical
        copying pandas/tests/categorical/conftest.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/categorical
        copying pandas/tests/categorical/test_warnings.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/categorical
        copying pandas/tests/categorical/test_constructors.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/categorical
        copying pandas/tests/categorical/test_missing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/categorical
        copying pandas/tests/categorical/test_sorting.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/categorical
        copying pandas/tests/categorical/test_operators.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/categorical
        copying pandas/tests/categorical/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/categorical
        copying pandas/tests/categorical/test_subclass.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/categorical
        copying pandas/tests/categorical/test_analytics.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/categorical
        copying pandas/tests/categorical/test_indexing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/categorical
        copying pandas/tests/categorical/test_algos.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/categorical
        copying pandas/tests/categorical/common.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/categorical
        copying pandas/tests/categorical/test_repr.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/categorical
        copying pandas/tests/categorical/test_api.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/categorical
        copying pandas/tests/categorical/test_dtypes.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/categorical
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/groupby
        copying pandas/tests/groupby/test_timegrouper.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/groupby
        copying pandas/tests/groupby/test_grouping.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/groupby
        copying pandas/tests/groupby/test_counting.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/groupby
        copying pandas/tests/groupby/test_value_counts.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/groupby
        copying pandas/tests/groupby/conftest.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/groupby
        copying pandas/tests/groupby/test_transform.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/groupby
        copying pandas/tests/groupby/test_nth.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/groupby
        copying pandas/tests/groupby/test_categorical.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/groupby
        copying pandas/tests/groupby/test_bin_groupby.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/groupby
        copying pandas/tests/groupby/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/groupby
        copying pandas/tests/groupby/test_apply.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/groupby
        copying pandas/tests/groupby/test_function.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/groupby
        copying pandas/tests/groupby/test_groupby.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/groupby
        copying pandas/tests/groupby/test_filters.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/groupby
        copying pandas/tests/groupby/test_rank.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/groupby
        copying pandas/tests/groupby/test_index_as_string.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/groupby
        copying pandas/tests/groupby/test_whitelist.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/groupby
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/internals
        copying pandas/tests/internals/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/internals
        copying pandas/tests/internals/test_internals.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/internals
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/computation
        copying pandas/tests/computation/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/computation
        copying pandas/tests/computation/test_compat.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/computation
        copying pandas/tests/computation/test_eval.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/computation
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/plotting
        copying pandas/tests/plotting/test_frame.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/plotting
        copying pandas/tests/plotting/test_misc.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/plotting
        copying pandas/tests/plotting/test_boxplot_method.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/plotting
        copying pandas/tests/plotting/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/plotting
        copying pandas/tests/plotting/test_datetimelike.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/plotting
        copying pandas/tests/plotting/test_deprecated.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/plotting
        copying pandas/tests/plotting/test_hist_method.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/plotting
        copying pandas/tests/plotting/common.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/plotting
        copying pandas/tests/plotting/test_groupby.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/plotting
        copying pandas/tests/plotting/test_converter.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/plotting
        copying pandas/tests/plotting/test_series.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/plotting
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/api
        copying pandas/tests/api/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/api
        copying pandas/tests/api/test_api.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/api
        copying pandas/tests/api/test_types.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/api
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/generic
        copying pandas/tests/generic/test_frame.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/generic
        copying pandas/tests/generic/test_panel.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/generic
        copying pandas/tests/generic/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/generic
        copying pandas/tests/generic/test_generic.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/generic
        copying pandas/tests/generic/test_label_or_level_utils.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/generic
        copying pandas/tests/generic/test_series.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/generic
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tslibs
        copying pandas/tests/tslibs/test_parsing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tslibs
        copying pandas/tests/tslibs/test_ccalendar.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tslibs
        copying pandas/tests/tslibs/test_timezones.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tslibs
        copying pandas/tests/tslibs/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tslibs
        copying pandas/tests/tslibs/test_conversion.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tslibs
        copying pandas/tests/tslibs/test_array_to_datetime.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tslibs
        copying pandas/tests/tslibs/test_liboffsets.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tslibs
        copying pandas/tests/tslibs/test_libfrequencies.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tslibs
        copying pandas/tests/tslibs/test_period_asfreq.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tslibs
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/sparse
        copying pandas/tests/sparse/test_libsparse.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/sparse
        copying pandas/tests/sparse/test_array.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/sparse
        copying pandas/tests/sparse/test_arithmetics.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/sparse
        copying pandas/tests/sparse/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/sparse
        copying pandas/tests/sparse/test_pivot.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/sparse
        copying pandas/tests/sparse/test_reshape.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/sparse
        copying pandas/tests/sparse/test_indexing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/sparse
        copying pandas/tests/sparse/common.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/sparse
        copying pandas/tests/sparse/test_groupby.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/sparse
        copying pandas/tests/sparse/test_combine_concat.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/sparse
        copying pandas/tests/sparse/test_format.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/sparse
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexing
        copying pandas/tests/indexing/test_indexing_slow.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexing
        copying pandas/tests/indexing/test_multiindex.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexing
        copying pandas/tests/indexing/test_ix.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexing
        copying pandas/tests/indexing/test_chaining_and_caching.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexing
        copying pandas/tests/indexing/test_callable.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexing
        copying pandas/tests/indexing/test_panel.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexing
        copying pandas/tests/indexing/test_categorical.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexing
        copying pandas/tests/indexing/test_iloc.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexing
        copying pandas/tests/indexing/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexing
        copying pandas/tests/indexing/test_loc.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexing
        copying pandas/tests/indexing/test_timedelta.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexing
        copying pandas/tests/indexing/test_indexing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexing
        copying pandas/tests/indexing/test_datetime.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexing
        copying pandas/tests/indexing/test_floats.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexing
        copying pandas/tests/indexing/common.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexing
        copying pandas/tests/indexing/test_coercion.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexing
        copying pandas/tests/indexing/test_scalar.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexing
        copying pandas/tests/indexing/test_partial.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexing
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/scalar
        copying pandas/tests/scalar/test_nat.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/scalar
        copying pandas/tests/scalar/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/scalar
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes
        copying pandas/tests/indexes/test_frozen.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes
        copying pandas/tests/indexes/conftest.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes
        copying pandas/tests/indexes/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes
        copying pandas/tests/indexes/test_numeric.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes
        copying pandas/tests/indexes/common.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes
        copying pandas/tests/indexes/datetimelike.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes
        copying pandas/tests/indexes/test_category.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes
        copying pandas/tests/indexes/test_multi.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes
        copying pandas/tests/indexes/test_range.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes
        copying pandas/tests/indexes/test_base.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series/indexing
        copying pandas/tests/series/indexing/test_alter_index.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series/indexing
        copying pandas/tests/series/indexing/conftest.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series/indexing
        copying pandas/tests/series/indexing/test_callable.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series/indexing
        copying pandas/tests/series/indexing/test_boolean.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series/indexing
        copying pandas/tests/series/indexing/test_iloc.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series/indexing
        copying pandas/tests/series/indexing/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series/indexing
        copying pandas/tests/series/indexing/test_loc.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series/indexing
        copying pandas/tests/series/indexing/test_indexing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series/indexing
        copying pandas/tests/series/indexing/test_numeric.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series/indexing
        copying pandas/tests/series/indexing/test_datetime.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/series/indexing
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape/merge
        copying pandas/tests/reshape/merge/test_merge_index_as_string.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape/merge
        copying pandas/tests/reshape/merge/test_merge_asof.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape/merge
        copying pandas/tests/reshape/merge/test_join.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape/merge
        copying pandas/tests/reshape/merge/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape/merge
        copying pandas/tests/reshape/merge/test_merge.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape/merge
        copying pandas/tests/reshape/merge/test_merge_ordered.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape/merge
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension/decimal
        copying pandas/tests/extension/decimal/test_decimal.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension/decimal
        copying pandas/tests/extension/decimal/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension/decimal
        copying pandas/tests/extension/decimal/array.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension/decimal
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension/category
        copying pandas/tests/extension/category/test_categorical.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension/category
        copying pandas/tests/extension/category/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension/category
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension/json
        copying pandas/tests/extension/json/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension/json
        copying pandas/tests/extension/json/test_json.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension/json
        copying pandas/tests/extension/json/array.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension/json
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension/base
        copying pandas/tests/extension/base/missing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension/base
        copying pandas/tests/extension/base/reshaping.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension/base
        copying pandas/tests/extension/base/methods.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension/base
        copying pandas/tests/extension/base/setitem.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension/base
        copying pandas/tests/extension/base/dtype.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension/base
        copying pandas/tests/extension/base/interface.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension/base
        copying pandas/tests/extension/base/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension/base
        copying pandas/tests/extension/base/getitem.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension/base
        copying pandas/tests/extension/base/casting.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension/base
        copying pandas/tests/extension/base/groupby.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension/base
        copying pandas/tests/extension/base/base.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension/base
        copying pandas/tests/extension/base/constructors.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/extension/base
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/msgpack
        copying pandas/tests/io/msgpack/test_extension.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/msgpack
        copying pandas/tests/io/msgpack/test_subtype.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/msgpack
        copying pandas/tests/io/msgpack/test_buffer.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/msgpack
        copying pandas/tests/io/msgpack/test_unpack.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/msgpack
        copying pandas/tests/io/msgpack/test_pack.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/msgpack
        copying pandas/tests/io/msgpack/test_unpack_raw.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/msgpack
        copying pandas/tests/io/msgpack/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/msgpack
        copying pandas/tests/io/msgpack/test_except.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/msgpack
        copying pandas/tests/io/msgpack/test_case.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/msgpack
        copying pandas/tests/io/msgpack/test_read_size.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/msgpack
        copying pandas/tests/io/msgpack/common.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/msgpack
        copying pandas/tests/io/msgpack/test_seq.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/msgpack
        copying pandas/tests/io/msgpack/test_limits.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/msgpack
        copying pandas/tests/io/msgpack/test_obj.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/msgpack
        copying pandas/tests/io/msgpack/test_newspec.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/msgpack
        copying pandas/tests/io/msgpack/test_format.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/msgpack
        copying pandas/tests/io/msgpack/test_sequnpack.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/msgpack
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/formats
        copying pandas/tests/io/formats/test_to_latex.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/formats
        copying pandas/tests/io/formats/test_to_html.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/formats
        copying pandas/tests/io/formats/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/formats
        copying pandas/tests/io/formats/test_eng_formatting.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/formats
        copying pandas/tests/io/formats/test_printing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/formats
        copying pandas/tests/io/formats/test_style.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/formats
        copying pandas/tests/io/formats/test_css.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/formats
        copying pandas/tests/io/formats/test_to_excel.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/formats
        copying pandas/tests/io/formats/test_format.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/formats
        copying pandas/tests/io/formats/test_to_csv.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/formats
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser
        copying pandas/tests/io/parser/parse_dates.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser
        copying pandas/tests/io/parser/na_values.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser
        copying pandas/tests/io/parser/comment.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser
        copying pandas/tests/io/parser/skiprows.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser
        copying pandas/tests/io/parser/header.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser
        copying pandas/tests/io/parser/dialect.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser
        copying pandas/tests/io/parser/test_parsers.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser
        copying pandas/tests/io/parser/compression.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser
        copying pandas/tests/io/parser/python_parser_only.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser
        copying pandas/tests/io/parser/index_col.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser
        copying pandas/tests/io/parser/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser
        copying pandas/tests/io/parser/dtypes.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser
        copying pandas/tests/io/parser/test_read_fwf.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser
        copying pandas/tests/io/parser/c_parser_only.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser
        copying pandas/tests/io/parser/test_unsupported.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser
        copying pandas/tests/io/parser/test_textreader.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser
        copying pandas/tests/io/parser/usecols.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser
        copying pandas/tests/io/parser/test_network.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser
        copying pandas/tests/io/parser/quoting.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser
        copying pandas/tests/io/parser/common.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser
        copying pandas/tests/io/parser/mangle_dupes.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser
        copying pandas/tests/io/parser/multithread.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser
        copying pandas/tests/io/parser/converters.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/json
        copying pandas/tests/io/json/test_compression.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/json
        copying pandas/tests/io/json/test_json_table_schema.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/json
        copying pandas/tests/io/json/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/json
        copying pandas/tests/io/json/test_readlines.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/json
        copying pandas/tests/io/json/test_ujson.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/json
        copying pandas/tests/io/json/test_pandas.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/json
        copying pandas/tests/io/json/test_normalize.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/json
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas
        copying pandas/tests/io/sas/test_sas7bdat.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas
        copying pandas/tests/io/sas/test_sas.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas
        copying pandas/tests/io/sas/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas
        copying pandas/tests/io/sas/test_xport.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tseries/offsets
        copying pandas/tests/tseries/offsets/conftest.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tseries/offsets
        copying pandas/tests/tseries/offsets/test_fiscal.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tseries/offsets
        copying pandas/tests/tseries/offsets/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tseries/offsets
        copying pandas/tests/tseries/offsets/test_yqm_offsets.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tseries/offsets
        copying pandas/tests/tseries/offsets/common.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tseries/offsets
        copying pandas/tests/tseries/offsets/test_ticks.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tseries/offsets
        copying pandas/tests/tseries/offsets/test_offsets.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tseries/offsets
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/groupby/aggregate
        copying pandas/tests/groupby/aggregate/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/groupby/aggregate
        copying pandas/tests/groupby/aggregate/test_cython.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/groupby/aggregate
        copying pandas/tests/groupby/aggregate/test_aggregate.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/groupby/aggregate
        copying pandas/tests/groupby/aggregate/test_other.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/groupby/aggregate
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/sparse/series
        copying pandas/tests/sparse/series/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/sparse/series
        copying pandas/tests/sparse/series/test_indexing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/sparse/series
        copying pandas/tests/sparse/series/test_series.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/sparse/series
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/sparse/frame
        copying pandas/tests/sparse/frame/test_frame.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/sparse/frame
        copying pandas/tests/sparse/frame/test_to_from_scipy.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/sparse/frame
        copying pandas/tests/sparse/frame/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/sparse/frame
        copying pandas/tests/sparse/frame/test_analytics.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/sparse/frame
        copying pandas/tests/sparse/frame/test_apply.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/sparse/frame
        copying pandas/tests/sparse/frame/test_indexing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/sparse/frame
        copying pandas/tests/sparse/frame/test_to_csv.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/sparse/frame
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexing/interval
        copying pandas/tests/indexing/interval/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexing/interval
        copying pandas/tests/indexing/interval/test_interval.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexing/interval
        copying pandas/tests/indexing/interval/test_interval_new.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexing/interval
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/scalar/interval
        copying pandas/tests/scalar/interval/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/scalar/interval
        copying pandas/tests/scalar/interval/test_interval.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/scalar/interval
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/scalar/timedelta
        copying pandas/tests/scalar/timedelta/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/scalar/timedelta
        copying pandas/tests/scalar/timedelta/test_timedelta.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/scalar/timedelta
        copying pandas/tests/scalar/timedelta/test_formats.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/scalar/timedelta
        copying pandas/tests/scalar/timedelta/test_construction.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/scalar/timedelta
        copying pandas/tests/scalar/timedelta/test_arithmetic.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/scalar/timedelta
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/scalar/period
        copying pandas/tests/scalar/period/test_period.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/scalar/period
        copying pandas/tests/scalar/period/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/scalar/period
        copying pandas/tests/scalar/period/test_asfreq.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/scalar/period
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/scalar/timestamp
        copying pandas/tests/scalar/timestamp/test_timezones.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/scalar/timestamp
        copying pandas/tests/scalar/timestamp/test_timestamp.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/scalar/timestamp
        copying pandas/tests/scalar/timestamp/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/scalar/timestamp
        copying pandas/tests/scalar/timestamp/test_comparisons.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/scalar/timestamp
        copying pandas/tests/scalar/timestamp/test_rendering.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/scalar/timestamp
        copying pandas/tests/scalar/timestamp/test_unary_ops.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/scalar/timestamp
        copying pandas/tests/scalar/timestamp/test_arithmetic.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/scalar/timestamp
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/interval
        copying pandas/tests/indexes/interval/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/interval
        copying pandas/tests/indexes/interval/test_interval_range.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/interval
        copying pandas/tests/indexes/interval/test_interval.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/interval
        copying pandas/tests/indexes/interval/test_astype.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/interval
        copying pandas/tests/indexes/interval/test_construction.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/interval
        copying pandas/tests/indexes/interval/test_interval_new.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/interval
        copying pandas/tests/indexes/interval/test_interval_tree.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/interval
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/period
        copying pandas/tests/indexes/period/test_period.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/period
        copying pandas/tests/indexes/period/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/period
        copying pandas/tests/indexes/period/test_scalar_compat.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/period
        copying pandas/tests/indexes/period/test_indexing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/period
        copying pandas/tests/indexes/period/test_astype.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/period
        copying pandas/tests/indexes/period/test_formats.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/period
        copying pandas/tests/indexes/period/test_setops.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/period
        copying pandas/tests/indexes/period/test_construction.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/period
        copying pandas/tests/indexes/period/test_partial_slicing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/period
        copying pandas/tests/indexes/period/test_ops.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/period
        copying pandas/tests/indexes/period/test_arithmetic.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/period
        copying pandas/tests/indexes/period/test_tools.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/period
        copying pandas/tests/indexes/period/test_asfreq.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/period
        copying pandas/tests/indexes/period/test_period_range.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/period
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/datetimes
        copying pandas/tests/indexes/datetimes/test_misc.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/datetimes
        copying pandas/tests/indexes/datetimes/test_missing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/datetimes
        copying pandas/tests/indexes/datetimes/test_date_range.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/datetimes
        copying pandas/tests/indexes/datetimes/test_timezones.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/datetimes
        copying pandas/tests/indexes/datetimes/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/datetimes
        copying pandas/tests/indexes/datetimes/test_datetimelike.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/datetimes
        copying pandas/tests/indexes/datetimes/test_scalar_compat.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/datetimes
        copying pandas/tests/indexes/datetimes/test_indexing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/datetimes
        copying pandas/tests/indexes/datetimes/test_astype.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/datetimes
        copying pandas/tests/indexes/datetimes/test_formats.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/datetimes
        copying pandas/tests/indexes/datetimes/test_setops.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/datetimes
        copying pandas/tests/indexes/datetimes/test_datetime.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/datetimes
        copying pandas/tests/indexes/datetimes/test_construction.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/datetimes
        copying pandas/tests/indexes/datetimes/test_partial_slicing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/datetimes
        copying pandas/tests/indexes/datetimes/test_ops.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/datetimes
        copying pandas/tests/indexes/datetimes/test_arithmetic.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/datetimes
        copying pandas/tests/indexes/datetimes/test_tools.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/datetimes
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/timedeltas
        copying pandas/tests/indexes/timedeltas/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/timedeltas
        copying pandas/tests/indexes/timedeltas/test_timedelta.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/timedeltas
        copying pandas/tests/indexes/timedeltas/test_scalar_compat.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/timedeltas
        copying pandas/tests/indexes/timedeltas/test_indexing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/timedeltas
        copying pandas/tests/indexes/timedeltas/test_astype.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/timedeltas
        copying pandas/tests/indexes/timedeltas/test_formats.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/timedeltas
        copying pandas/tests/indexes/timedeltas/test_setops.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/timedeltas
        copying pandas/tests/indexes/timedeltas/test_construction.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/timedeltas
        copying pandas/tests/indexes/timedeltas/test_partial_slicing.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/timedeltas
        copying pandas/tests/indexes/timedeltas/test_ops.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/timedeltas
        copying pandas/tests/indexes/timedeltas/test_arithmetic.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/timedeltas
        copying pandas/tests/indexes/timedeltas/test_timedelta_range.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/timedeltas
        copying pandas/tests/indexes/timedeltas/test_tools.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/timedeltas
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/_libs/tslibs
        copying pandas/_libs/tslibs/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/_libs/tslibs
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/api/types
        copying pandas/api/types/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/api/types
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/api/extensions
        copying pandas/api/extensions/__init__.py -> build/lib.macosx-10.9-x86_64-3.8/pandas/api/extensions
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/data
        copying pandas/tests/data/tips.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/data
        copying pandas/tests/data/iris.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/data
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/io/formats/templates
        copying pandas/io/formats/templates/html.tpl -> build/lib.macosx-10.9-x86_64-3.8/pandas/io/formats/templates
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape/data
        copying pandas/tests/reshape/data/cut_data.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape/data
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/test3.xlsx -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/test3.xls -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/stata6_114.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/testdtype.xlsx -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/stata7_111.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/testdtype.xlsm -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/stata15.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/stata6_115.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/test2.xls -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/test3.xlsm -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/stata6_117.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/spam.html -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/stata13_dates.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/test1.xls -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/gbq_fake_job.txt -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/test5.xls -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/stata7_117.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/stata6_113.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/test4.xls -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/blank.xls -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/banklist.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/test2.xlsm -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/test_types.xls -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/test_multisheet.xlsx -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/testdateoverflow.xls -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/stata7_115.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/test_multisheet.xlsm -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/valid_markup.html -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/test2.xlsx -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/blank_with_header.xlsm -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/stata5_117.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/test_converters.xls -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/times_1900.xls -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/blank_with_header.xlsx -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/stata6.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/stata4_113.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/test5.xlsx -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/stata5_114.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/nyse_wsj.html -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/wikipedia_states.html -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/stata5_115.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/test5.xlsm -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/stata5.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/times_1900.xlsx -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/stata4_114.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/test4.xlsm -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/test_index_name_pre17.xlsm -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/categorical_0_15_2.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/test_index_name_pre17.xlsx -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/times_1900.xlsm -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/stata4_115.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/test4.xlsx -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/testmultiindex.xlsx -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/tips.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/stata4_117.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/blank.xlsm -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/testskiprows.xlsx -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/times_1904.xls -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/testmultiindex.xls -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/stata5_113.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/testmultiindex.xlsm -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/blank.xlsx -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/stata3.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/testskiprows.xlsm -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/test_squeeze.xlsx -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/stata8_115.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/testdateoverflow.xlsx -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/testdateoverflow.xlsm -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/stata10_117.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/stata1_117.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/test_squeeze.xlsm -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/test_types.xlsx -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/iris.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/stata10_115.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/stata1_114.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/macau.html -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/stata8_117.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/test_types.xlsm -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/stata14_118.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/stata8_113.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/stata11_115.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/testdtype.xls -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/blank_with_header.xls -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/stata9_117.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/stata9_115.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/computer_sales_page.html -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/test1.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/stata11_117.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/test_index_name_pre17.xls -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/stata2_115.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/test1.xlsm -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/test_multisheet.xls -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/categorical_0_14_1.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/S4_EDUC1.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/test1.xlsx -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/stata2_114.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/stata3_113.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/test_mmap.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/stata2_117.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/stata2_113.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/test_squeeze.xls -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/test_converters.xlsm -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/banklist.html -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/stata1_encoding.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/feather-0_3_1.feather -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/testskiprows.xls -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/stata3_117.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/stata12_117.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/test_converters.xlsx -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/stata3_115.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/times_1904.xlsm -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/fixed_width_format.txt -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/stata3_114.dta -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        copying pandas/tests/io/data/times_1904.xlsx -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_hdf
        copying pandas/tests/io/data/legacy_hdf/legacy_table.h5 -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_hdf
        copying pandas/tests/io/data/legacy_hdf/datetimetz_object.h5 -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_hdf
        copying pandas/tests/io/data/legacy_hdf/pytables_native.h5 -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_hdf
        copying pandas/tests/io/data/legacy_hdf/pytables_native2.h5 -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_hdf
        copying pandas/tests/io/data/legacy_hdf/periodindex_0.20.1_x86_64_darwin_2.7.13.h5 -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_hdf
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.11.0
        copying pandas/tests/io/data/legacy_pickle/0.11.0/x86_64_linux_2.7.3.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.11.0
        copying pandas/tests/io/data/legacy_pickle/0.11.0/x86_64_linux_3.3.0.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.11.0
        copying pandas/tests/io/data/legacy_pickle/0.11.0/0.11.0_x86_64_linux_3.3.0.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.11.0
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.15.0
        copying pandas/tests/io/data/legacy_pickle/0.15.0/0.15.0_x86_64_darwin_2.7.12.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.15.0
        copying pandas/tests/io/data/legacy_pickle/0.15.0/0.15.0_x86_64_linux_2.7.8.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.15.0
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.19.2
        copying pandas/tests/io/data/legacy_pickle/0.19.2/0.19.2_x86_64_darwin_2.7.12.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.19.2
        copying pandas/tests/io/data/legacy_pickle/0.19.2/0.19.2_x86_64_darwin_2.7.14.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.19.2
        copying pandas/tests/io/data/legacy_pickle/0.19.2/0.19.2_x86_64_darwin_3.6.1.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.19.2
        copying pandas/tests/io/data/legacy_pickle/0.19.2/0.19.2_AMD64_windows_2.7.14.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.19.2
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.18.0
        copying pandas/tests/io/data/legacy_pickle/0.18.0/0.18.0_x86_64_darwin_3.5.1.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.18.0
        copying pandas/tests/io/data/legacy_pickle/0.18.0/0.18.0_x86_64_darwin_2.7.11.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.18.0
        copying pandas/tests/io/data/legacy_pickle/0.18.0/0.18.0_AMD64_windows_3.5.1.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.18.0
        copying pandas/tests/io/data/legacy_pickle/0.18.0/0.18.0_AMD64_windows_2.7.11.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.18.0
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.12.0
        copying pandas/tests/io/data/legacy_pickle/0.12.0/0.12.0_AMD64_windows_2.7.3.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.12.0
        copying pandas/tests/io/data/legacy_pickle/0.12.0/0.12.0_x86_64_linux_2.7.3.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.12.0
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.18.1
        copying pandas/tests/io/data/legacy_pickle/0.18.1/0.18.1_x86_64_darwin_2.7.12.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.18.1
        copying pandas/tests/io/data/legacy_pickle/0.18.1/0.18.1_x86_64_darwin_3.5.2.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.18.1
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.16.0
        copying pandas/tests/io/data/legacy_pickle/0.16.0/0.16.0_x86_64_darwin_2.7.9.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.16.0
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.20.3
        copying pandas/tests/io/data/legacy_pickle/0.20.3/0.20.3_x86_64_darwin_2.7.14.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.20.3
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.13.0
        copying pandas/tests/io/data/legacy_pickle/0.13.0/0.13.0_x86_64_darwin_2.7.5.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.13.0
        copying pandas/tests/io/data/legacy_pickle/0.13.0/0.13.0_i686_linux_3.2.3.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.13.0
        copying pandas/tests/io/data/legacy_pickle/0.13.0/0.13.0_i686_linux_2.6.5.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.13.0
        copying pandas/tests/io/data/legacy_pickle/0.13.0/0.13.0_x86_64_linux_3.3.0.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.13.0
        copying pandas/tests/io/data/legacy_pickle/0.13.0/0.13.0_x86_64_linux_2.7.8.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.13.0
        copying pandas/tests/io/data/legacy_pickle/0.13.0/0.13.0_i686_linux_2.7.3.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.13.0
        copying pandas/tests/io/data/legacy_pickle/0.13.0/0.13.0_x86_64_linux_2.7.3.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.13.0
        copying pandas/tests/io/data/legacy_pickle/0.13.0/0.13.0_x86_64_darwin_2.7.6.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.13.0
        copying pandas/tests/io/data/legacy_pickle/0.13.0/0.13.0_AMD64_windows_2.7.3.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.13.0
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.17.1
        copying pandas/tests/io/data/legacy_pickle/0.17.1/0.17.1_x86_64_darwin_2.7.11.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.17.1
        copying pandas/tests/io/data/legacy_pickle/0.17.1/0.17.1_AMD64_windows_2.7.11.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.17.1
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.15.2
        copying pandas/tests/io/data/legacy_pickle/0.15.2/0.15.2_x86_64_darwin_2.7.9.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.15.2
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.17.0
        copying pandas/tests/io/data/legacy_pickle/0.17.0/0.17.0_x86_64_linux_3.4.4.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.17.0
        copying pandas/tests/io/data/legacy_pickle/0.17.0/0.17.0_x86_64_linux_2.7.11.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.17.0
        copying pandas/tests/io/data/legacy_pickle/0.17.0/0.17.0_x86_64_darwin_3.4.4.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.17.0
        copying pandas/tests/io/data/legacy_pickle/0.17.0/0.17.0_x86_64_darwin_2.7.11.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.17.0
        copying pandas/tests/io/data/legacy_pickle/0.17.0/0.17.0_AMD64_windows_3.4.4.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.17.0
        copying pandas/tests/io/data/legacy_pickle/0.17.0/0.17.1_AMD64_windows_2.7.11.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.17.0
        copying pandas/tests/io/data/legacy_pickle/0.17.0/0.17.0_AMD64_windows_2.7.11.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.17.0
        copying pandas/tests/io/data/legacy_pickle/0.17.0/0.17.0_x86_64_darwin_3.5.3.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.17.0
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.14.1
        copying pandas/tests/io/data/legacy_pickle/0.14.1/0.14.1_x86_64_linux_2.7.8.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.14.1
        copying pandas/tests/io/data/legacy_pickle/0.14.1/0.14.1_x86_64_darwin_2.7.12.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.14.1
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.16.2
        copying pandas/tests/io/data/legacy_pickle/0.16.2/0.16.2_x86_64_darwin_2.7.10.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.16.2
        copying pandas/tests/io/data/legacy_pickle/0.16.2/0.16.2_AMD64_windows_3.4.3.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.16.2
        copying pandas/tests/io/data/legacy_pickle/0.16.2/0.16.2_AMD64_windows_2.7.10.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.16.2
        copying pandas/tests/io/data/legacy_pickle/0.16.2/0.16.2_x86_64_linux_2.7.10.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.16.2
        copying pandas/tests/io/data/legacy_pickle/0.16.2/0.16.2_x86_64_darwin_2.7.9.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.16.2
        copying pandas/tests/io/data/legacy_pickle/0.16.2/0.16.2_x86_64_linux_3.4.3.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.16.2
        copying pandas/tests/io/data/legacy_pickle/0.16.2/0.16.2_x86_64_darwin_3.4.3.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.16.2
        copying pandas/tests/io/data/legacy_pickle/0.16.2/0.16.2_AMD64_windows_2.7.14.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.16.2
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.14.0
        copying pandas/tests/io/data/legacy_pickle/0.14.0/0.14.0_x86_64_darwin_2.7.6.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.14.0
        copying pandas/tests/io/data/legacy_pickle/0.14.0/0.14.0_x86_64_linux_2.7.8.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.14.0
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.10.1
        copying pandas/tests/io/data/legacy_pickle/0.10.1/x86_64_linux_2.7.3.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.10.1
        copying pandas/tests/io/data/legacy_pickle/0.10.1/AMD64_windows_2.7.3.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_pickle/0.10.1
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.19.2
        copying pandas/tests/io/data/legacy_msgpack/0.19.2/0.19.2_x86_64_darwin_3.6.1.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.19.2
        copying pandas/tests/io/data/legacy_msgpack/0.19.2/0.19.2_x86_64_darwin_2.7.12.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.19.2
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.18.0
        copying pandas/tests/io/data/legacy_msgpack/0.18.0/0.18.0_x86_64_darwin_3.5.1.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.18.0
        copying pandas/tests/io/data/legacy_msgpack/0.18.0/0.18.0_x86_64_darwin_2.7.11.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.18.0
        copying pandas/tests/io/data/legacy_msgpack/0.18.0/0.18.0_AMD64_windows_2.7.11.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.18.0
        copying pandas/tests/io/data/legacy_msgpack/0.18.0/0.18.0_AMD64_windows_3.5.1.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.18.0
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.18.1
        copying pandas/tests/io/data/legacy_msgpack/0.18.1/0.18.1_x86_64_darwin_3.5.2.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.18.1
        copying pandas/tests/io/data/legacy_msgpack/0.18.1/0.18.1_x86_64_darwin_2.7.12.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.18.1
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.16.0
        copying pandas/tests/io/data/legacy_msgpack/0.16.0/0.16.0_x86_64_darwin_2.7.9.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.16.0
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.17.1
        copying pandas/tests/io/data/legacy_msgpack/0.17.1/0.17.1_x86_64_darwin_2.7.11.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.17.1
        copying pandas/tests/io/data/legacy_msgpack/0.17.1/0.17.1_x86_64_darwin_3.5.1.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.17.1
        copying pandas/tests/io/data/legacy_msgpack/0.17.1/0.17.1_AMD64_windows_2.7.11.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.17.1
        copying pandas/tests/io/data/legacy_msgpack/0.17.1/0.17.1_x86_64_linux_3.4.4.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.17.1
        copying pandas/tests/io/data/legacy_msgpack/0.17.1/0.17.1_AMD64_windows_3.5.1.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.17.1
        copying pandas/tests/io/data/legacy_msgpack/0.17.1/0.17.1_x86_64_linux_2.7.11.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.17.1
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.17.0
        copying pandas/tests/io/data/legacy_msgpack/0.17.0/0.17.0_AMD64_windows_3.4.4.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.17.0
        copying pandas/tests/io/data/legacy_msgpack/0.17.0/0.17.1_AMD64_windows_2.7.11.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.17.0
        copying pandas/tests/io/data/legacy_msgpack/0.17.0/0.17.0_x86_64_darwin_3.4.4.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.17.0
        copying pandas/tests/io/data/legacy_msgpack/0.17.0/0.17.0_x86_64_darwin_2.7.11.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.17.0
        copying pandas/tests/io/data/legacy_msgpack/0.17.0/0.17.0_AMD64_windows_2.7.11.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.17.0
        copying pandas/tests/io/data/legacy_msgpack/0.17.0/0.17.0_x86_64_linux_2.7.11.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.17.0
        copying pandas/tests/io/data/legacy_msgpack/0.17.0/0.17.1_AMD64_windows_3.5.1.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.17.0
        copying pandas/tests/io/data/legacy_msgpack/0.17.0/0.17.0_x86_64_linux_3.4.4.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.17.0
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.16.2
        copying pandas/tests/io/data/legacy_msgpack/0.16.2/0.16.2_x86_64_darwin_2.7.10.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.16.2
        copying pandas/tests/io/data/legacy_msgpack/0.16.2/0.16.2_AMD64_windows_2.7.10.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.16.2
        copying pandas/tests/io/data/legacy_msgpack/0.16.2/0.16.2_x86_64_linux_3.4.3.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.16.2
        copying pandas/tests/io/data/legacy_msgpack/0.16.2/0.16.2_AMD64_windows_3.4.3.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.16.2
        copying pandas/tests/io/data/legacy_msgpack/0.16.2/0.16.2_x86_64_linux_2.7.10.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.16.2
        copying pandas/tests/io/data/legacy_msgpack/0.16.2/0.16.2_x86_64_darwin_2.7.9.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.16.2
        copying pandas/tests/io/data/legacy_msgpack/0.16.2/0.16.2_x86_64_darwin_3.4.3.msgpack -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/legacy_msgpack/0.16.2
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/html_encoding
        copying pandas/tests/io/data/html_encoding/chinese_utf-32.html -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/html_encoding
        copying pandas/tests/io/data/html_encoding/letz_latin1.html -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/html_encoding
        copying pandas/tests/io/data/html_encoding/chinese_utf-16.html -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/html_encoding
        copying pandas/tests/io/data/html_encoding/chinese_utf-8.html -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/data/html_encoding
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/data
        copying pandas/tests/indexes/data/multiindex_v1.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/data
        copying pandas/tests/indexes/data/mindex_073.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/indexes/data
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape/merge/data
        copying pandas/tests/reshape/merge/data/allow_exact_matches_and_tolerance.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape/merge/data
        copying pandas/tests/reshape/merge/data/quotes.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape/merge/data
        copying pandas/tests/reshape/merge/data/tolerance.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape/merge/data
        copying pandas/tests/reshape/merge/data/asof2.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape/merge/data
        copying pandas/tests/reshape/merge/data/quotes2.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape/merge/data
        copying pandas/tests/reshape/merge/data/trades.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape/merge/data
        copying pandas/tests/reshape/merge/data/trades2.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape/merge/data
        copying pandas/tests/reshape/merge/data/allow_exact_matches.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape/merge/data
        copying pandas/tests/reshape/merge/data/asof.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/reshape/merge/data
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/msgpack/data
        copying pandas/tests/io/msgpack/data/frame.mp -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/msgpack/data
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/formats/data
        copying pandas/tests/io/formats/data/unicode_series.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/formats/data
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser/data
        copying pandas/tests/io/parser/data/utf16_ex.txt -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser/data
        copying pandas/tests/io/parser/data/items.jsonl -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser/data
        copying pandas/tests/io/parser/data/salaries.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser/data
        copying pandas/tests/io/parser/data/sub_char.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser/data
        copying pandas/tests/io/parser/data/tips.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser/data
        copying pandas/tests/io/parser/data/unicode_series.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser/data
        copying pandas/tests/io/parser/data/salaries.csv.zip -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser/data
        copying pandas/tests/io/parser/data/utf16_ex_small.zip -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser/data
        copying pandas/tests/io/parser/data/tips.csv.bz2 -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser/data
        copying pandas/tests/io/parser/data/salaries.csv.bz2 -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser/data
        copying pandas/tests/io/parser/data/iris.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser/data
        copying pandas/tests/io/parser/data/test1.csv.gz -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser/data
        copying pandas/tests/io/parser/data/tar_csv.tar -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser/data
        copying pandas/tests/io/parser/data/test2.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser/data
        copying pandas/tests/io/parser/data/sauron.SHIFT_JIS.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser/data
        copying pandas/tests/io/parser/data/salaries.csv.xz -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser/data
        copying pandas/tests/io/parser/data/test1.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser/data
        copying pandas/tests/io/parser/data/tips.csv.gz -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser/data
        copying pandas/tests/io/parser/data/tar_csv.tar.gz -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser/data
        copying pandas/tests/io/parser/data/test_mmap.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser/data
        copying pandas/tests/io/parser/data/test1.csv.bz2 -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser/data
        copying pandas/tests/io/parser/data/salaries.csv.gz -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/parser/data
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/json/data
        copying pandas/tests/io/json/data/tsframe_v012.json -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/json/data
        copying pandas/tests/io/json/data/tsframe_iso_v012.json -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/json/data
        copying pandas/tests/io/json/data/tsframe_v012.json.zip -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/json/data
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
        copying pandas/tests/io/sas/data/SSHSV1_A.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
        copying pandas/tests/io/sas/data/test14.sas7bdat -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
        copying pandas/tests/io/sas/data/test15.sas7bdat -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
        copying pandas/tests/io/sas/data/test1.sas7bdat -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
        copying pandas/tests/io/sas/data/test_sas7bdat_2.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
        copying pandas/tests/io/sas/data/test_sas7bdat_1.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
        copying pandas/tests/io/sas/data/zero_variables.sas7bdat -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
        copying pandas/tests/io/sas/data/test6.sas7bdat -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
        copying pandas/tests/io/sas/data/test7.sas7bdat -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
        copying pandas/tests/io/sas/data/productsales.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
        copying pandas/tests/io/sas/data/DEMO_G.xpt -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
        copying pandas/tests/io/sas/data/test_12659.sas7bdat -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
        copying pandas/tests/io/sas/data/datetime.sas7bdat -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
        copying pandas/tests/io/sas/data/DRXFCD_G.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
        copying pandas/tests/io/sas/data/paxraw_d_short.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
        copying pandas/tests/io/sas/data/test13.sas7bdat -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
        copying pandas/tests/io/sas/data/test12.sas7bdat -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
        copying pandas/tests/io/sas/data/test8.sas7bdat -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
        copying pandas/tests/io/sas/data/test9.sas7bdat -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
        copying pandas/tests/io/sas/data/test2.sas7bdat -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
        copying pandas/tests/io/sas/data/test3.sas7bdat -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
        copying pandas/tests/io/sas/data/productsales.sas7bdat -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
        copying pandas/tests/io/sas/data/airline.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
        copying pandas/tests/io/sas/data/DRXFCD_G.xpt -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
        copying pandas/tests/io/sas/data/test_12659.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
        copying pandas/tests/io/sas/data/test16.sas7bdat -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
        copying pandas/tests/io/sas/data/DEMO_G.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
        copying pandas/tests/io/sas/data/paxraw_d_short.xpt -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
        copying pandas/tests/io/sas/data/airline.sas7bdat -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
        copying pandas/tests/io/sas/data/test10.sas7bdat -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
        copying pandas/tests/io/sas/data/test11.sas7bdat -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
        copying pandas/tests/io/sas/data/datetime.csv -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
        copying pandas/tests/io/sas/data/test5.sas7bdat -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
        copying pandas/tests/io/sas/data/test4.sas7bdat -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
        copying pandas/tests/io/sas/data/SSHSV1_A.xpt -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/io/sas/data
        creating build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tseries/offsets/data
        copying pandas/tests/tseries/offsets/data/cday-0.14.1.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tseries/offsets/data
        copying pandas/tests/tseries/offsets/data/dateoffset_0_15_2.pickle -> build/lib.macosx-10.9-x86_64-3.8/pandas/tests/tseries/offsets/data
        UPDATING build/lib.macosx-10.9-x86_64-3.8/pandas/_version.py
        set build/lib.macosx-10.9-x86_64-3.8/pandas/_version.py to '0.23.1'
        running build_ext
        cythoning pandas/_libs/algos.pyx to pandas/_libs/algos.c
        /opt/anaconda3/lib/python3.8/site-packages/Cython/Compiler/Main.py:369: FutureWarning: Cython directive 'language_level' not set, using 2 for now (Py2). This will change in a later release! File: /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pandas/pandas/_libs/algos.pxd
          tree = Parsing.p_module(s, pxd, full_module_name)
        cythoning pandas/_libs/groupby.pyx to pandas/_libs/groupby.c
        /opt/anaconda3/lib/python3.8/site-packages/Cython/Compiler/Main.py:369: FutureWarning: Cython directive 'language_level' not set, using 2 for now (Py2). This will change in a later release! File: /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pandas/pandas/_libs/groupby.pyx
          tree = Parsing.p_module(s, pxd, full_module_name)
        cythoning pandas/_libs/hashing.pyx to pandas/_libs/hashing.c
        /opt/anaconda3/lib/python3.8/site-packages/Cython/Compiler/Main.py:369: FutureWarning: Cython directive 'language_level' not set, using 2 for now (Py2). This will change in a later release! File: /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pandas/pandas/_libs/hashing.pyx
          tree = Parsing.p_module(s, pxd, full_module_name)
        cythoning pandas/_libs/hashtable.pyx to pandas/_libs/hashtable.c
        /opt/anaconda3/lib/python3.8/site-packages/Cython/Compiler/Main.py:369: FutureWarning: Cython directive 'language_level' not set, using 2 for now (Py2). This will change in a later release! File: /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pandas/pandas/_libs/hashtable.pxd
          tree = Parsing.p_module(s, pxd, full_module_name)
        cythoning pandas/_libs/index.pyx to pandas/_libs/index.c
        /opt/anaconda3/lib/python3.8/site-packages/Cython/Compiler/Main.py:369: FutureWarning: Cython directive 'language_level' not set, using 2 for now (Py2). This will change in a later release! File: /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pandas/pandas/_libs/index.pyx
          tree = Parsing.p_module(s, pxd, full_module_name)
        cythoning pandas/_libs/indexing.pyx to pandas/_libs/indexing.c
        /opt/anaconda3/lib/python3.8/site-packages/Cython/Compiler/Main.py:369: FutureWarning: Cython directive 'language_level' not set, using 2 for now (Py2). This will change in a later release! File: /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pandas/pandas/_libs/indexing.pyx
          tree = Parsing.p_module(s, pxd, full_module_name)
        cythoning pandas/_libs/internals.pyx to pandas/_libs/internals.c
        /opt/anaconda3/lib/python3.8/site-packages/Cython/Compiler/Main.py:369: FutureWarning: Cython directive 'language_level' not set, using 2 for now (Py2). This will change in a later release! File: /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pandas/pandas/_libs/internals.pyx
          tree = Parsing.p_module(s, pxd, full_module_name)
        cythoning pandas/_libs/interval.pyx to pandas/_libs/interval.c
        /opt/anaconda3/lib/python3.8/site-packages/Cython/Compiler/Main.py:369: FutureWarning: Cython directive 'language_level' not set, using 2 for now (Py2). This will change in a later release! File: /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pandas/pandas/_libs/interval.pyx
          tree = Parsing.p_module(s, pxd, full_module_name)
        cythoning pandas/_libs/join.pyx to pandas/_libs/join.c
        /opt/anaconda3/lib/python3.8/site-packages/Cython/Compiler/Main.py:369: FutureWarning: Cython directive 'language_level' not set, using 2 for now (Py2). This will change in a later release! File: /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pandas/pandas/_libs/join.pyx
          tree = Parsing.p_module(s, pxd, full_module_name)
        cythoning pandas/_libs/lib.pyx to pandas/_libs/lib.c
        /opt/anaconda3/lib/python3.8/site-packages/Cython/Compiler/Main.py:369: FutureWarning: Cython directive 'language_level' not set, using 2 for now (Py2). This will change in a later release! File: /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pandas/pandas/_libs/lib.pyx
          tree = Parsing.p_module(s, pxd, full_module_name)
        cythoning pandas/_libs/missing.pyx to pandas/_libs/missing.c
        /opt/anaconda3/lib/python3.8/site-packages/Cython/Compiler/Main.py:369: FutureWarning: Cython directive 'language_level' not set, using 2 for now (Py2). This will change in a later release! File: /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pandas/pandas/_libs/missing.pxd
          tree = Parsing.p_module(s, pxd, full_module_name)
        cythoning pandas/_libs/parsers.pyx to pandas/_libs/parsers.c
        /opt/anaconda3/lib/python3.8/site-packages/Cython/Compiler/Main.py:369: FutureWarning: Cython directive 'language_level' not set, using 2 for now (Py2). This will change in a later release! File: /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pandas/pandas/_libs/parsers.pyx
          tree = Parsing.p_module(s, pxd, full_module_name)
        warning: pandas/_libs/parsers.pyx:1705:34: Casting a GIL-requiring function into a nogil function circumvents GIL validation
        cythoning pandas/_libs/reduction.pyx to pandas/_libs/reduction.c
        /opt/anaconda3/lib/python3.8/site-packages/Cython/Compiler/Main.py:369: FutureWarning: Cython directive 'language_level' not set, using 2 for now (Py2). This will change in a later release! File: /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pandas/pandas/_libs/reduction.pyx
          tree = Parsing.p_module(s, pxd, full_module_name)
        cythoning pandas/_libs/ops.pyx to pandas/_libs/ops.c
        /opt/anaconda3/lib/python3.8/site-packages/Cython/Compiler/Main.py:369: FutureWarning: Cython directive 'language_level' not set, using 2 for now (Py2). This will change in a later release! File: /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pandas/pandas/_libs/ops.pyx
          tree = Parsing.p_module(s, pxd, full_module_name)
        cythoning pandas/_libs/tslibs/period.pyx to pandas/_libs/tslibs/period.c
        /opt/anaconda3/lib/python3.8/site-packages/Cython/Compiler/Main.py:369: FutureWarning: Cython directive 'language_level' not set, using 2 for now (Py2). This will change in a later release! File: /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pandas/pandas/_libs/tslibs/period.pyx
          tree = Parsing.p_module(s, pxd, full_module_name)
        cythoning pandas/_libs/properties.pyx to pandas/_libs/properties.c
        /opt/anaconda3/lib/python3.8/site-packages/Cython/Compiler/Main.py:369: FutureWarning: Cython directive 'language_level' not set, using 2 for now (Py2). This will change in a later release! File: /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pandas/pandas/_libs/properties.pyx
          tree = Parsing.p_module(s, pxd, full_module_name)
        cythoning pandas/_libs/reshape.pyx to pandas/_libs/reshape.c
        /opt/anaconda3/lib/python3.8/site-packages/Cython/Compiler/Main.py:369: FutureWarning: Cython directive 'language_level' not set, using 2 for now (Py2). This will change in a later release! File: /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pandas/pandas/_libs/reshape.pyx
          tree = Parsing.p_module(s, pxd, full_module_name)
        cythoning pandas/_libs/skiplist.pyx to pandas/_libs/skiplist.c
        /opt/anaconda3/lib/python3.8/site-packages/Cython/Compiler/Main.py:369: FutureWarning: Cython directive 'language_level' not set, using 2 for now (Py2). This will change in a later release! File: /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pandas/pandas/_libs/skiplist.pxd
          tree = Parsing.p_module(s, pxd, full_module_name)
        cythoning pandas/_libs/sparse.pyx to pandas/_libs/sparse.c
        /opt/anaconda3/lib/python3.8/site-packages/Cython/Compiler/Main.py:369: FutureWarning: Cython directive 'language_level' not set, using 2 for now (Py2). This will change in a later release! File: /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pandas/pandas/_libs/sparse.pyx
          tree = Parsing.p_module(s, pxd, full_module_name)
        cythoning pandas/_libs/tslib.pyx to pandas/_libs/tslib.c
        /opt/anaconda3/lib/python3.8/site-packages/Cython/Compiler/Main.py:369: FutureWarning: Cython directive 'language_level' not set, using 2 for now (Py2). This will change in a later release! File: /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pandas/pandas/_libs/tslib.pyx
          tree = Parsing.p_module(s, pxd, full_module_name)
        cythoning pandas/_libs/tslibs/ccalendar.pyx to pandas/_libs/tslibs/ccalendar.c
        /opt/anaconda3/lib/python3.8/site-packages/Cython/Compiler/Main.py:369: FutureWarning: Cython directive 'language_level' not set, using 2 for now (Py2). This will change in a later release! File: /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pandas/pandas/_libs/tslibs/ccalendar.pxd
          tree = Parsing.p_module(s, pxd, full_module_name)
        cythoning pandas/_libs/tslibs/conversion.pyx to pandas/_libs/tslibs/conversion.c
        /opt/anaconda3/lib/python3.8/site-packages/Cython/Compiler/Main.py:369: FutureWarning: Cython directive 'language_level' not set, using 2 for now (Py2). This will change in a later release! File: /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pandas/pandas/_libs/tslibs/conversion.pxd
          tree = Parsing.p_module(s, pxd, full_module_name)
        cythoning pandas/_libs/tslibs/fields.pyx to pandas/_libs/tslibs/fields.c
        /opt/anaconda3/lib/python3.8/site-packages/Cython/Compiler/Main.py:369: FutureWarning: Cython directive 'language_level' not set, using 2 for now (Py2). This will change in a later release! File: /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pandas/pandas/_libs/tslibs/fields.pyx
          tree = Parsing.p_module(s, pxd, full_module_name)
        cythoning pandas/_libs/tslibs/frequencies.pyx to pandas/_libs/tslibs/frequencies.c
        /opt/anaconda3/lib/python3.8/site-packages/Cython/Compiler/Main.py:369: FutureWarning: Cython directive 'language_level' not set, using 2 for now (Py2). This will change in a later release! File: /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pandas/pandas/_libs/tslibs/frequencies.pxd
          tree = Parsing.p_module(s, pxd, full_module_name)
        cythoning pandas/_libs/tslibs/nattype.pyx to pandas/_libs/tslibs/nattype.c
        /opt/anaconda3/lib/python3.8/site-packages/Cython/Compiler/Main.py:369: FutureWarning: Cython directive 'language_level' not set, using 2 for now (Py2). This will change in a later release! File: /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pandas/pandas/_libs/tslibs/nattype.pxd
          tree = Parsing.p_module(s, pxd, full_module_name)
        cythoning pandas/_libs/tslibs/np_datetime.pyx to pandas/_libs/tslibs/np_datetime.c
        /opt/anaconda3/lib/python3.8/site-packages/Cython/Compiler/Main.py:369: FutureWarning: Cython directive 'language_level' not set, using 2 for now (Py2). This will change in a later release! File: /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pandas/pandas/_libs/tslibs/np_datetime.pxd
          tree = Parsing.p_module(s, pxd, full_module_name)
        cythoning pandas/_libs/tslibs/offsets.pyx to pandas/_libs/tslibs/offsets.c
        /opt/anaconda3/lib/python3.8/site-packages/Cython/Compiler/Main.py:369: FutureWarning: Cython directive 'language_level' not set, using 2 for now (Py2). This will change in a later release! File: /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pandas/pandas/_libs/tslibs/offsets.pyx
          tree = Parsing.p_module(s, pxd, full_module_name)
        cythoning pandas/_libs/tslibs/parsing.pyx to pandas/_libs/tslibs/parsing.c
        /opt/anaconda3/lib/python3.8/site-packages/Cython/Compiler/Main.py:369: FutureWarning: Cython directive 'language_level' not set, using 2 for now (Py2). This will change in a later release! File: /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pandas/pandas/_libs/tslibs/parsing.pyx
          tree = Parsing.p_module(s, pxd, full_module_name)
        cythoning pandas/_libs/tslibs/resolution.pyx to pandas/_libs/tslibs/resolution.c
        /opt/anaconda3/lib/python3.8/site-packages/Cython/Compiler/Main.py:369: FutureWarning: Cython directive 'language_level' not set, using 2 for now (Py2). This will change in a later release! File: /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pandas/pandas/_libs/tslibs/resolution.pyx
          tree = Parsing.p_module(s, pxd, full_module_name)
        cythoning pandas/_libs/tslibs/strptime.pyx to pandas/_libs/tslibs/strptime.c
        /opt/anaconda3/lib/python3.8/site-packages/Cython/Compiler/Main.py:369: FutureWarning: Cython directive 'language_level' not set, using 2 for now (Py2). This will change in a later release! File: /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pandas/pandas/_libs/tslibs/strptime.pyx
          tree = Parsing.p_module(s, pxd, full_module_name)
        cythoning pandas/_libs/tslibs/timedeltas.pyx to pandas/_libs/tslibs/timedeltas.c
        /opt/anaconda3/lib/python3.8/site-packages/Cython/Compiler/Main.py:369: FutureWarning: Cython directive 'language_level' not set, using 2 for now (Py2). This will change in a later release! File: /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pandas/pandas/_libs/tslibs/timedeltas.pxd
          tree = Parsing.p_module(s, pxd, full_module_name)
        cythoning pandas/_libs/tslibs/timestamps.pyx to pandas/_libs/tslibs/timestamps.c
        /opt/anaconda3/lib/python3.8/site-packages/Cython/Compiler/Main.py:369: FutureWarning: Cython directive 'language_level' not set, using 2 for now (Py2). This will change in a later release! File: /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pandas/pandas/_libs/tslibs/timestamps.pxd
          tree = Parsing.p_module(s, pxd, full_module_name)
        cythoning pandas/_libs/tslibs/timezones.pyx to pandas/_libs/tslibs/timezones.c
        /opt/anaconda3/lib/python3.8/site-packages/Cython/Compiler/Main.py:369: FutureWarning: Cython directive 'language_level' not set, using 2 for now (Py2). This will change in a later release! File: /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pandas/pandas/_libs/tslibs/timezones.pxd
          tree = Parsing.p_module(s, pxd, full_module_name)
        cythoning pandas/_libs/testing.pyx to pandas/_libs/testing.c
        /opt/anaconda3/lib/python3.8/site-packages/Cython/Compiler/Main.py:369: FutureWarning: Cython directive 'language_level' not set, using 2 for now (Py2). This will change in a later release! File: /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pandas/pandas/_libs/testing.pyx
          tree = Parsing.p_module(s, pxd, full_module_name)
        skipping 'pandas/_libs/window.cpp' Cython extension (up-to-date)
        cythoning pandas/_libs/writers.pyx to pandas/_libs/writers.c
        /opt/anaconda3/lib/python3.8/site-packages/Cython/Compiler/Main.py:369: FutureWarning: Cython directive 'language_level' not set, using 2 for now (Py2). This will change in a later release! File: /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pandas/pandas/_libs/writers.pyx
          tree = Parsing.p_module(s, pxd, full_module_name)
        cythoning pandas/io/sas/sas.pyx to pandas/io/sas/sas.c
        /opt/anaconda3/lib/python3.8/site-packages/Cython/Compiler/Main.py:369: FutureWarning: Cython directive 'language_level' not set, using 2 for now (Py2). This will change in a later release! File: /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pandas/pandas/io/sas/sas.pyx
          tree = Parsing.p_module(s, pxd, full_module_name)
        skipping 'pandas/io/msgpack/_packer.cpp' Cython extension (up-to-date)
        skipping 'pandas/io/msgpack/_unpacker.cpp' Cython extension (up-to-date)
        building 'pandas._libs.algos' extension
        creating build/temp.macosx-10.9-x86_64-3.8
        creating build/temp.macosx-10.9-x86_64-3.8/pandas
        creating build/temp.macosx-10.9-x86_64-3.8/pandas/_libs
        gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Ipandas/_libs/src/klib -Ipandas/_libs/src -I/opt/anaconda3/lib/python3.8/site-packages/numpy/core/include -I/opt/anaconda3/include/python3.8 -c pandas/_libs/algos.c -o build/temp.macosx-10.9-x86_64-3.8/pandas/_libs/algos.o -Wno-unused-function
        In file included from pandas/_libs/algos.c:610:
        In file included from /opt/anaconda3/lib/python3.8/site-packages/numpy/core/include/numpy/arrayobject.h:4:
        In file included from /opt/anaconda3/lib/python3.8/site-packages/numpy/core/include/numpy/ndarrayobject.h:12:
        In file included from /opt/anaconda3/lib/python3.8/site-packages/numpy/core/include/numpy/ndarraytypes.h:1822:
        /opt/anaconda3/lib/python3.8/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:17:2: warning: "Using deprecated NumPy API, disable it with "          "#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-W#warnings]
        #warning "Using deprecated NumPy API, disable it with " \
         ^
        pandas/_libs/algos.c:128597:3: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
          0, /*tp_print*/
          ^
        /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
            Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
            ^
        /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
        #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                             ^
        pandas/_libs/algos.c:128716:3: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
          0, /*tp_print*/
          ^
        /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
            Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
            ^
        /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
        #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                             ^
        pandas/_libs/algos.c:128977:3: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
          0, /*tp_print*/
          ^
        /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
            Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
            ^
        /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
        #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                             ^
        pandas/_libs/algos.c:129123:3: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
          0, /*tp_print*/
          ^
        /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
            Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
            ^
        /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
        #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                             ^
        pandas/_libs/algos.c:140814:5: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
            0,
            ^
        /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
            Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
            ^
        /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
        #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                             ^
        pandas/_libs/algos.c:141274:5: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
            0,
            ^
        /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
            Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
            ^
        /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
        #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                             ^
        7 warnings generated.
        gcc -bundle -undefined dynamic_lookup -L/opt/anaconda3/lib -arch x86_64 -L/opt/anaconda3/lib -arch x86_64 -arch x86_64 build/temp.macosx-10.9-x86_64-3.8/pandas/_libs/algos.o -o build/lib.macosx-10.9-x86_64-3.8/pandas/_libs/algos.cpython-38-darwin.so
        building 'pandas._libs.groupby' extension
        gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Ipandas/_libs/src/klib -Ipandas/_libs/src -I/opt/anaconda3/lib/python3.8/site-packages/numpy/core/include -I/opt/anaconda3/include/python3.8 -c pandas/_libs/groupby.c -o build/temp.macosx-10.9-x86_64-3.8/pandas/_libs/groupby.o -Wno-unused-function
        In file included from pandas/_libs/groupby.c:610:
        In file included from /opt/anaconda3/lib/python3.8/site-packages/numpy/core/include/numpy/arrayobject.h:4:
        In file included from /opt/anaconda3/lib/python3.8/site-packages/numpy/core/include/numpy/ndarrayobject.h:12:
        In file included from /opt/anaconda3/lib/python3.8/site-packages/numpy/core/include/numpy/ndarraytypes.h:1822:
        /opt/anaconda3/lib/python3.8/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:17:2: warning: "Using deprecated NumPy API, disable it with "          "#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-W#warnings]
        #warning "Using deprecated NumPy API, disable it with " \
         ^
        pandas/_libs/groupby.c:26393:40: warning: self-comparison always evaluates to true [-Wtautological-compare]
                    __pyx_t_22 = ((__pyx_v_val == __pyx_v_val) != 0);
                                               ^
        pandas/_libs/groupby.c:27142:40: warning: self-comparison always evaluates to true [-Wtautological-compare]
                    __pyx_t_22 = ((__pyx_v_val == __pyx_v_val) != 0);
                                               ^
        pandas/_libs/groupby.c:54115:3: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
          0, /*tp_print*/
          ^
        /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
            Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
            ^
        /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
        #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                             ^
        pandas/_libs/groupby.c:54234:3: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
          0, /*tp_print*/
          ^
        /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
            Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
            ^
        /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
        #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                             ^
        pandas/_libs/groupby.c:54495:3: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
          0, /*tp_print*/
          ^
        /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
            Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
            ^
        /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
        #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                             ^
        pandas/_libs/groupby.c:54641:3: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
          0, /*tp_print*/
          ^
        /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
            Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
            ^
        /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
        #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                             ^
        pandas/_libs/groupby.c:60797:5: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
            0,
            ^
        /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
            Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
            ^
        /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
        #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                             ^
        pandas/_libs/groupby.c:61177:5: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
            0,
            ^
        /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
            Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
            ^
        /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
        #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                             ^
        9 warnings generated.
        gcc -bundle -undefined dynamic_lookup -L/opt/anaconda3/lib -arch x86_64 -L/opt/anaconda3/lib -arch x86_64 -arch x86_64 build/temp.macosx-10.9-x86_64-3.8/pandas/_libs/groupby.o -o build/lib.macosx-10.9-x86_64-3.8/pandas/_libs/groupby.cpython-38-darwin.so
        building 'pandas._libs.hashing' extension
        gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Ipandas/_libs/src/klib -Ipandas/_libs/src -I/opt/anaconda3/lib/python3.8/site-packages/numpy/core/include -I/opt/anaconda3/include/python3.8 -c pandas/_libs/hashing.c -o build/temp.macosx-10.9-x86_64-3.8/pandas/_libs/hashing.o -Wno-unused-function
        In file included from pandas/_libs/hashing.c:610:
        In file included from /opt/anaconda3/lib/python3.8/site-packages/numpy/core/include/numpy/arrayobject.h:4:
        In file included from /opt/anaconda3/lib/python3.8/site-packages/numpy/core/include/numpy/ndarrayobject.h:12:
        In file included from /opt/anaconda3/lib/python3.8/site-packages/numpy/core/include/numpy/ndarraytypes.h:1822:
        /opt/anaconda3/lib/python3.8/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:17:2: warning: "Using deprecated NumPy API, disable it with "          "#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-W#warnings]
        #warning "Using deprecated NumPy API, disable it with " \
         ^
        1 warning generated.
        gcc -bundle -undefined dynamic_lookup -L/opt/anaconda3/lib -arch x86_64 -L/opt/anaconda3/lib -arch x86_64 -arch x86_64 build/temp.macosx-10.9-x86_64-3.8/pandas/_libs/hashing.o -o build/lib.macosx-10.9-x86_64-3.8/pandas/_libs/hashing.cpython-38-darwin.so
        building 'pandas._libs.hashtable' extension
        gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Ipandas/_libs/src/klib -Ipandas/_libs/src -I/opt/anaconda3/lib/python3.8/site-packages/numpy/core/include -I/opt/anaconda3/include/python3.8 -c pandas/_libs/hashtable.c -o build/temp.macosx-10.9-x86_64-3.8/pandas/_libs/hashtable.o -Wno-unused-function
        In file included from pandas/_libs/hashtable.c:611:
        In file included from /opt/anaconda3/lib/python3.8/site-packages/numpy/core/include/numpy/arrayobject.h:4:
        In file included from /opt/anaconda3/lib/python3.8/site-packages/numpy/core/include/numpy/ndarrayobject.h:12:
        In file included from /opt/anaconda3/lib/python3.8/site-packages/numpy/core/include/numpy/ndarraytypes.h:1822:
        /opt/anaconda3/lib/python3.8/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:17:2: warning: "Using deprecated NumPy API, disable it with "          "#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-W#warnings]
        #warning "Using deprecated NumPy API, disable it with " \
         ^
        pandas/_libs/hashtable.c:14700:38: warning: self-comparison always evaluates to false [-Wtautological-compare]
                  __pyx_t_15 = ((__pyx_v_val != __pyx_v_val) != 0);
                                             ^
        pandas/_libs/hashtable.c:18483:38: warning: self-comparison always evaluates to false [-Wtautological-compare]
                  __pyx_t_15 = ((__pyx_v_val != __pyx_v_val) != 0);
                                             ^
        pandas/_libs/hashtable.c:20570:13: warning: assigning to 'char *' from 'const char *' discards qualifiers [-Wincompatible-pointer-types-discards-qualifiers]
          __pyx_t_5 = get_c_string(__pyx_v_val); if (unlikely(__pyx_t_5 == ((char *)NULL))) __PYX_ERR(0, 1249, __pyx_L1_error)
                    ^ ~~~~~~~~~~~~~~~~~~~~~~~~~
        pandas/_libs/hashtable.c:20819:13: warning: assigning to 'char *' from 'const char *' discards qualifiers [-Wincompatible-pointer-types-discards-qualifiers]
          __pyx_t_8 = get_c_string(__pyx_t_1); if (unlikely(__pyx_t_8 == ((char *)NULL))) __PYX_ERR(0, 1263, __pyx_L1_error)
                    ^ ~~~~~~~~~~~~~~~~~~~~~~~
        pandas/_libs/hashtable.c:21197:16: warning: assigning to 'char *' from 'const char *' discards qualifiers [-Wincompatible-pointer-types-discards-qualifiers]
            __pyx_t_12 = get_c_string(__pyx_v_val); if (unlikely(__pyx_t_12 == ((char *)NULL))) __PYX_ERR(0, 1286, __pyx_L1_error)
                       ^ ~~~~~~~~~~~~~~~~~~~~~~~~~
        pandas/_libs/hashtable.c:21536:16: warning: assigning to 'char *' from 'const char *' discards qualifiers [-Wincompatible-pointer-types-discards-qualifiers]
            __pyx_t_11 = get_c_string(__pyx_v_val); if (unlikely(__pyx_t_11 == ((char *)NULL))) __PYX_ERR(0, 1316, __pyx_L1_error)
                       ^ ~~~~~~~~~~~~~~~~~~~~~~~~~
        pandas/_libs/hashtable.c:22176:18: warning: assigning to 'char *' from 'const char *' discards qualifiers [-Wincompatible-pointer-types-discards-qualifiers]
              __pyx_t_13 = get_c_string(__pyx_v_val); if (unlikely(__pyx_t_13 == ((char *)NULL))) __PYX_ERR(0, 1357, __pyx_L1_error)
                         ^ ~~~~~~~~~~~~~~~~~~~~~~~~~
        pandas/_libs/hashtable.c:22199:18: warning: assigning to 'char *' from 'const char *' discards qualifiers [-Wincompatible-pointer-types-discards-qualifiers]
              __pyx_t_13 = get_c_string(__pyx_t_6); if (unlikely(__pyx_t_13 == ((char *)NULL))) __PYX_ERR(0, 1359, __pyx_L1_error)
                         ^ ~~~~~~~~~~~~~~~~~~~~~~~
        pandas/_libs/hashtable.c:22547:17: warning: assigning to 'char *' from 'const char *' discards qualifiers [-Wincompatible-pointer-types-discards-qualifiers]
              __pyx_t_8 = get_c_string(__pyx_v_val); if (unlikely(__pyx_t_8 == ((char *)NULL))) __PYX_ERR(0, 1390, __pyx_L1_error)
                        ^ ~~~~~~~~~~~~~~~~~~~~~~~~~
        pandas/_libs/hashtable.c:22570:17: warning: assigning to 'char *' from 'const char *' discards qualifiers [-Wincompatible-pointer-types-discards-qualifiers]
              __pyx_t_8 = get_c_string(__pyx_t_4); if (unlikely(__pyx_t_8 == ((char *)NULL))) __PYX_ERR(0, 1392, __pyx_L1_error)
                        ^ ~~~~~~~~~~~~~~~~~~~~~~~
        pandas/_libs/hashtable.c:23087:18: warning: assigning to 'char *' from 'const char *' discards qualifiers [-Wincompatible-pointer-types-discards-qualifiers]
              __pyx_t_14 = get_c_string(__pyx_v_val); if (unlikely(__pyx_t_14 == ((char *)NULL))) __PYX_ERR(0, 1431, __pyx_L1_error)
                         ^ ~~~~~~~~~~~~~~~~~~~~~~~~~
        pandas/_libs/hashtable.c:27621:19: warning: comparison of integers of different signs: 'size_t' (aka 'unsigned long') and 'Py_ssize_t' (aka 'long') [-Wsign-compare]
          if (((__pyx_t_1 < __pyx_t_2) != 0)) {
                ~~~~~~~~~ ^ ~~~~~~~~~
        pandas/_libs/hashtable.c:29586:39: warning: self-comparison always evaluates to false [-Wtautological-compare]
                    __pyx_t_16 = (__pyx_v_val != __pyx_v_val);
                                              ^
        pandas/_libs/hashtable.c:29366:19: warning: comparison of integers of different signs: 'size_t' (aka 'unsigned long') and 'Py_ssize_t' (aka 'long') [-Wsign-compare]
          if (((__pyx_t_1 < __pyx_t_2) != 0)) {
                ~~~~~~~~~ ^ ~~~~~~~~~
        pandas/_libs/hashtable.c:32946:39: warning: self-comparison always evaluates to false [-Wtautological-compare]
                    __pyx_t_16 = (__pyx_v_val != __pyx_v_val);
                                              ^
        pandas/_libs/hashtable.c:32726:19: warning: comparison of integers of different signs: 'size_t' (aka 'unsigned long') and 'Py_ssize_t' (aka 'long') [-Wsign-compare]
          if (((__pyx_t_1 < __pyx_t_2) != 0)) {
                ~~~~~~~~~ ^ ~~~~~~~~~
        pandas/_libs/hashtable.c:53916:3: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
          0, /*tp_print*/
          ^
        /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
            Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
            ^
        /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
        #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                             ^
        pandas/_libs/hashtable.c:54052:3: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
          0, /*tp_print*/
          ^
        /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
            Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
            ^
        /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
        #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                             ^
        pandas/_libs/hashtable.c:54188:3: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
          0, /*tp_print*/
          ^
        /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
            Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
            ^
        /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
        #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                             ^
        pandas/_libs/hashtable.c:54324:3: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
          0, /*tp_print*/
          ^
        /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
            Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
            ^
        /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
        #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                             ^
        pandas/_libs/hashtable.c:54452:3: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
          0, /*tp_print*/
          ^
        /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
            Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
            ^
        /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
        #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                             ^
        pandas/_libs/hashtable.c:54563:3: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
          0, /*tp_print*/
          ^
        /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
            Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
            ^
        /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
        #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                             ^
        pandas/_libs/hashtable.c:54716:3: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
          0, /*tp_print*/
          ^
        /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
            Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
            ^
        /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
        #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                             ^
        pandas/_libs/hashtable.c:54869:3: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
          0, /*tp_print*/
          ^
        /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
            Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
            ^
        /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
        #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                             ^
        pandas/_libs/hashtable.c:55022:3: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
          0, /*tp_print*/
          ^
        /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
            Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
            ^
        /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
        #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                             ^
        pandas/_libs/hashtable.c:55153:3: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
          0, /*tp_print*/
          ^
        /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
            Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
            ^
        /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
        #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                             ^
        pandas/_libs/hashtable.c:55298:3: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
          0, /*tp_print*/
          ^
        /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
            Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
            ^
        /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
        #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                             ^
        pandas/_libs/hashtable.c:55475:3: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
          0, /*tp_print*/
          ^
        /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
            Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
            ^
        /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
        #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                             ^
        pandas/_libs/hashtable.c:55651:3: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
          0, /*tp_print*/
          ^
        /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
            Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
            ^
        /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
        #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                             ^
        pandas/_libs/hashtable.c:55840:3: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
          0, /*tp_print*/
          ^
        /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
            Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
            ^
        /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
        #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                             ^
        pandas/_libs/hashtable.c:55959:3: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
          0, /*tp_print*/
          ^
        /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
            Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
            ^
        /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
        #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                             ^
        pandas/_libs/hashtable.c:56220:3: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
          0, /*tp_print*/
          ^
        /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
            Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
            ^
        /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
        #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                             ^
        pandas/_libs/hashtable.c:56366:3: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
          0, /*tp_print*/
          ^
        /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
            Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
            ^
        /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
        #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                             ^
        34 warnings generated.
        gcc -bundle -undefined dynamic_lookup -L/opt/anaconda3/lib -arch x86_64 -L/opt/anaconda3/lib -arch x86_64 -arch x86_64 build/temp.macosx-10.9-x86_64-3.8/pandas/_libs/hashtable.o -o build/lib.macosx-10.9-x86_64-3.8/pandas/_libs/hashtable.cpython-38-darwin.so
        building 'pandas._libs.index' extension
        creating build/temp.macosx-10.9-x86_64-3.8/pandas/_libs/src
        creating build/temp.macosx-10.9-x86_64-3.8/pandas/_libs/src/datetime
        gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Ipandas/_libs/src/klib -Ipandas/_libs/src -I/opt/anaconda3/lib/python3.8/site-packages/numpy/core/include -I/opt/anaconda3/include/python3.8 -c pandas/_libs/index.c -o build/temp.macosx-10.9-x86_64-3.8/pandas/_libs/index.o -Wno-unused-function
        In file included from pandas/_libs/index.c:611:
        In file included from /opt/anaconda3/lib/python3.8/site-packages/numpy/core/include/numpy/arrayobject.h:4:
        In file included from /opt/anaconda3/lib/python3.8/site-packages/numpy/core/include/numpy/ndarrayobject.h:12:
        In file included from /opt/anaconda3/lib/python3.8/site-packages/numpy/core/include/numpy/ndarraytypes.h:1822:
        /opt/anaconda3/lib/python3.8/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:17:2: warning: "Using deprecated NumPy API, disable it with "          "#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-W#warnings]
        #warning "Using deprecated NumPy API, disable it with " \
         ^
        pandas/_libs/index.c:42804:3: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
          0, /*tp_print*/
          ^
        /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
            Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
            ^
        /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
        #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                             ^
        pandas/_libs/index.c:42896:3: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
          0, /*tp_print*/
          ^
        /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
            Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
            ^
        /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
        #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                             ^
        pandas/_libs/index.c:43003:3: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
          0, /*tp_print*/
          ^
        /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
            Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
            ^
        /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
        #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                             ^
        pandas/_libs/index.c:43092:3: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
          0, /*tp_print*/
          ^
        /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
            Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
            ^
        /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
        #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                             ^
        pandas/_libs/index.c:43187:3: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
          0, /*tp_print*/
          ^
        /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
            Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
            ^
        /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
        #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                             ^
        pandas/_libs/index.c:43299:3: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
          0, /*tp_print*/
          ^
        /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
            Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
            ^
        /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
        #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                             ^
        pandas/_libs/index.c:43391:3: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
          0, /*tp_print*/
          ^
        /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
            Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
            ^
        /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
        #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                             ^
        pandas/_libs/index.c:43483:3: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
          0, /*tp_print*/
          ^
        /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
            Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
            ^
        /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
        #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                             ^
        pandas/_libs/index.c:43575:3: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
          0, /*tp_print*/
          ^
        /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
            Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
            ^
        /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
        #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                             ^
        pandas/_libs/index.c:43690:3: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
          0, /*tp_print*/
          ^
        /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
            Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
            ^
        /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
        #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                             ^
        pandas/_libs/index.c:43879:3: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
          0, /*tp_print*/
          ^
        /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
            Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
            ^
        /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
        #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                             ^
        pandas/_libs/index.c:43998:3: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
          0, /*tp_print*/
          ^
        /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
            Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
            ^
        /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
        #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                             ^
        pandas/_libs/index.c:44259:3: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
          0, /*tp_print*/
          ^
        /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
            Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
            ^
        /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
        #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                             ^
        pandas/_libs/index.c:44405:3: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
          0, /*tp_print*/
          ^
        /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
            Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
            ^
        /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
        #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                             ^
        pandas/_libs/index.c:48918:5: warning: 'tp_print' is deprecated [-Wdeprecated-declarations]
            0,
            ^
        /opt/anaconda3/include/python3.8/cpython/object.h:260:5: note: 'tp_print' has been explicitly marked deprecated here
            Py_DEPRECATED(3.8) int (*tp_print)(PyObject *, FILE *, int);
            ^
        /opt/anaconda3/include/python3.8/pyport.h:515:54: note: expanded from macro 'Py_DEPRECATED'
        #define Py_DEPRECATED(VERSION_UNUSED) __attribute__((__deprecated__))
                                                             ^
        16 warnings generated.
        gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/opt/anaconda3/include -arch x86_64 -I/opt/anaconda3/include -arch x86_64 -Ipandas/_libs/src/klib -Ipandas/_libs/src -I/opt/anaconda3/lib/python3.8/site-packages/numpy/core/include -I/opt/anaconda3/include/python3.8 -c pandas/_libs/src/datetime/np_datetime.c -o build/temp.macosx-10.9-x86_64-3.8/pandas/_libs/src/datetime/np_datetime.o -Wno-unused-function
        In file included from pandas/_libs/src/datetime/np_datetime.c:22:
        In file included from /opt/anaconda3/lib/python3.8/site-packages/numpy/core/include/numpy/arrayobject.h:4:
        In file included from /opt/anaconda3/lib/python3.8/site-packages/numpy/core/include/numpy/ndarrayobject.h:12:
        In file included from /opt/anaconda3/lib/python3.8/site-packages/numpy/core/include/numpy/ndarraytypes.h:1822:
        /opt/anaconda3/lib/python3.8/site-packages/numpy/core/include/numpy/npy_1_7_deprecated_api.h:17:2: warning: "Using deprecated NumPy API, disable it with "          "#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION" [-W#warnings]
        #warning "Using deprecated NumPy API, disable it with " \
         ^
        pandas/_libs/src/datetime/np_datetime.c:518:5: error: implicit declaration of function 'convert_datetimestruct_to_datetime' is invalid in C99 [-Werror,-Wimplicit-function-declaration]
            convert_datetimestruct_to_datetime(fr, d, &result);
            ^
        pandas/_libs/src/datetime/np_datetime.c:518:5: note: did you mean 'pandas_datetimestruct_to_datetime'?
        pandas/_libs/src/datetime/np_datetime.c:514:14: note: 'pandas_datetimestruct_to_datetime' declared here
        npy_datetime pandas_datetimestruct_to_datetime(PANDAS_DATETIMEUNIT fr,
                     ^
        pandas/_libs/src/datetime/np_datetime.c:530:5: error: implicit declaration of function 'convert_timedelta_to_timedeltastruct' is invalid in C99 [-Werror,-Wimplicit-function-declaration]
            convert_timedelta_to_timedeltastruct(fr, val, result);
            ^
        pandas/_libs/src/datetime/np_datetime.c:530:5: note: did you mean 'pandas_timedelta_to_timedeltastruct'?
        pandas/_libs/src/datetime/np_datetime.c:527:6: note: 'pandas_timedelta_to_timedeltastruct' declared here
        void pandas_timedelta_to_timedeltastruct(npy_timedelta val,
             ^
        1 warning and 2 errors generated.
        error: command 'gcc' failed with exit status 1
        ----------------------------------------[0m
    [?25h  Rolling back uninstall of pandas
      Moving to /opt/anaconda3/lib/python3.8/site-packages/pandas-1.1.3.dist-info/
       from /opt/anaconda3/lib/python3.8/site-packages/~andas-1.1.3.dist-info
      Moving to /opt/anaconda3/lib/python3.8/site-packages/pandas/
       from /opt/anaconda3/lib/python3.8/site-packages/~andas
    [31mERROR: Command errored out with exit status 1: /opt/anaconda3/bin/python -u -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pandas/setup.py'"'"'; __file__='"'"'/private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-install-7gi47j0v/pandas/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' install --record /private/var/folders/qg/s0hbzvy14hx1n7fvx1s6bm540000gn/T/pip-record-8nfssjdm/install-record.txt --single-version-externally-managed --compile --install-headers /opt/anaconda3/include/python3.8/pandas Check the logs for full command output.[0m
    Note: you may need to restart the kernel to use updated packages.


## Executando Exemplos de Código

É mais fácil criar primeiro um único diretório e salvar cada exemplo de código como *.py* dentro dele. Quando estiver pronto para executar o arquivo de código, navegue até esse diretório no prompt de comando e certifique-se de que seu ambiente virtual esteja ativado. Lembre-se de que você sempre pode ativar o ambiente com o seguinte comando apropriado para o seu sistema operacional.


```python
source activate bokeh-env #For Linux/MacOS
activate bokeh-env #For Windows
```

Dentro do ambiente virtual, você pode executar o código digitando:


```python
python nome_do_arquivo.py
```

Um Jupyter Notebook contendo o código utilizado neste tutorial também está [disponível](https://raw.githubusercontent.com/programminghistorian/ph-submissions/gh-pages/assets/visualizing-with-bokeh/visualizing-with-bokeh.ipynb) no caso de você preferir trabalhar ao longo do tutorial sem instalar um ambiente virtual. Você pode aprender mais sobre Jupyter Notebook [aqui](http://jupyter.org). Caso tenha criado um ambiente virtual utilizando Miniconda, como discutido acima, você pode instalar Jupyter Notebook no ambiente digitando `conda install jupyter`.

# O Básico de Bokeh

## O que é Bokeh?
