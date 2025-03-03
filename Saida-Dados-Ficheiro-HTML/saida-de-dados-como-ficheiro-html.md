---
title: Saída de Dados como um Ficheiro HTML com Python
layout: lesson
slug: saida-de-dados-como-ficheiro-html
date: 2012-07-17
translation_date: 2022-01-14
authors:
- William J. Turkel
- Adam Crymble
reviewers:
- Jim Clifford
- Frederik Elwert
editors:
- Miriam Posner
translator: 
- Felipe Lamarca
translation-editor:
- 
translation-reviewer:
- 
difficulty: 2
review-ticket: 
activity: transformar
topics: [python, website]
abstract: "Essa lição toma os pares de frequência criados na lição 'Contagem de Frequências' e os apresenta em um ficheiro HTML."
redirect_from: /licoes/saida-de-dados-como-ficheiro-html
original: output-data-as-html-file
avatar_alt: A woman wearing an elaborate dress accompanied by two putti
doi:
---

{% include toc.html %}

## Objetivos da Lição

Essa lição toma os pares de frequência criados na lição [Contagem de Frequências][] e os apresenta em um ficheiro HTML.

Aqui você aprenderá como apresentar dados como um ficheiro HTML usando Python. Você também aprenderá sobre formatação de strings. O resultado final é um ficheiro HTML que apresenta as palavras-chave encontradas na fonte original em ordem decrescente de frequência, junto com o número de vezes que cada palavra-chave aparece.

## Ficheiros Necessários para esta Lição

- `obo.py`

Caso não possua esses ficheiros da lição anterior, você pode fazer o *download* do programming-historian-6, um [ficheiro zip da lição anterior][]. 

## Construindo um *HTML wrapper*

Na lição anterior, você aprendeu como incorporar a mensagem "*Hello World!*" em *tags* HTML, escrever o resultado em um ficheiro e abrí-lo automaticamente no seu navegador. Um programa que coloca códigos de formatação em torno de algo de modo que ele possa ser usado por outro programa às vezes é chamado de *wrapper*. O que faremos agora é desenvolver um *HTML wrapper* para a saída do nosso código que computa frequências de palavras. Também adicionaremos alguns metadados dinâmicos e úteis para complementar os dados de frequência coletados em [Contagem de Frequências][].

## Metadados

A distinção entre dados e metadados é crucial para a ciência da informação. Metadados são dados sobre dados. Esse conceito já deve ser bastante familiar a você, ainda que você não tenha escutado esse termo anteriormente. Considere um livro tradicional. Se considerarmos que o texto do livro é um dado, há uma série de outras características associadas a esse texto, mas que podem ou não estar explicitamente exibidas no livro. O título da obra, o autor, a editora, o local e a data de publicação são metadados que tipicamente estão apresentados na obra. O local e a data de escrita, o nome do editor de texto, os dados de catalogação da Biblioteca do Congresso e o nome da fonte usada para formatar o livro às vezes são exibidos nele. A pessoa que comprou uma cópia particular pode ou não escrever seu nome no livro. Se o livro pertence à coleção de uma biblioteca, essa biblioteca manterá metadados adicionais, apenas alguns dos quais serão fisicamente anexados ao livro. Os registros de empréstimo, por exemplo, geralmente são mantidos em algum tipo de banco de dados conectado ao livro por um identificador único. Bibliotecas, arquivos e museus possuem sistemas elaborados para gerar e manter controle de metadados.

Quando estiver trabalhando com dados digitais, é uma boa ideia incorporar metadados nos seus próprios ficheiros sempre que possível. Nós agora desenvolveremos algumas estratégias básicas para tornar nossos ficheiros *autodocumentados*. No nosso *wrapper*, queremos incluir informações dinâmicas sobre o ficheiro, como o horário e a data em que foi criado, assim como um título HTML relevante para este ficheiro. Nesse caso poderíamos simplesmente nomeá-lo por conta própria, mas quando começarmos a trabalhar com múltiplos ficheiros, criar documentos *autodocumentados* automaticamente economizará muito tempo, então vamos praticar agora. E para isso, precisaremos aprender a tirar proveito de algumas opções mais poderosas de formatação de string.

## Formatação de string com Python

O Python inclui um operador de formatação especial que permite que você insira uma string dentro de outra. Ele é representado pelo sinal de percentual seguido de um "s". Abra um Python *shell* e tente os exemplos a seguir:


``` python

frame = 'Essa fruta é uma %s'
print(frame)
-> Essa fruta é uma %s

print(frame % 'banana')
-> Essa fruta é uma banana

print(frame % 'pera')
-> Essa fruta é uma pera
```

Há também uma maneira que permite que você interpole uma lista de strings em outra.

``` python

frame2 = 'Essas são %s, aquelas são %s'
print(frame2)
-> Essas são %s, aquelas são %s

print(frame2 % ('bananas', 'peras'))
-> Essas são bananas, aquelas são peras
```

Nesses exemplos, `%s` em uma string indica que outra string será incorporada naquele ponto. Há uma gama de outros códigos de formatação de string, dentre os quais a maioria permite que você incorpore números em strings de vários formatos, como `%i` para inteiro (ex.: 1, 2, 3), `%f` para decimal de ponto flutuante (ex.: 3.023, 4.59, 1.0) e assim por diante. Usando esse método, podemos inserir informações exclusivas do ficheiro. 

## Ficheiro de dados Autodocumentado

Vamos agrupar alguns dos códigos que já escrevemos na forma de função. Uma delas receberá uma URL e retornará uma string de texto em letras minúsculas a partir da página web. Copie esse código no módulo `obo.py`:


``` python
# Dada uma URL, retorna uma string em minúsculas da página

def webPageToText(url):
    import urllib.request, urllib.error, urllib.parse
    response = urllib.request.urlopen(url)
    html = response.read().decode('UTF-8')
    text = stripTags(html).lower()
    return text
```

Também vamos desejar uma função que tome uma string de qualquer tipo e a torne o corpo de um ficheiro HTML que é aberto automaticamente no Firefox. Essa função deve incluir alguns metadados básicos, como o horário e a data que foi criado e o nome do programa que o criou. Estude o código a seguir cuidadosamente e depois copie-o no módulo `obo.py`. 

### Instruções para Mac

Se estiver usando um Mac, certifique-se de incluir o caminho de ficheiro apropriado na variável `filename` na penúltima linha para refletir o local onde você está armazenando seus ficheiros.

``` python
# Dado o nome do programa, uma url e uma string a ser envolvida, 
# retorna uma string no corpo do html com metadados básicos e 
# abre numa guia do Firefox

def wrapStringInHTMLMac(program, url, body):
    import datetime
    from webbrowser import open_new_tab

    now = datetime.datetime.today().strftime("%Y%m%d-%H%M%S")
    filename = program + '.html'
    f = open(filename,'w')

    wrapper = """<html>
    <head>
    <title>%s output - %s</title>
    </head>
    <body><p>URL: <a href=\"%s\">%s</a></p><p>%s</p></body>
    </html>"""

    whole = wrapper % (program, now, url, url, body)
    f.write(whole)
    f.close()

    #Mude a variável filename abaixo para corresponder à localização do seu diretório
    filename = 'file:///Users/username/Desktop/programming-historian/' + filename

    open_new_tab(filename)
```

### Instruções de Windows

``` python
# Dado o nome do programa, uma url e uma string a ser envolvida, 
# retorna uma string no corpo do html com metadados básicos e 
# abre numa guia do Firefox

def wrapStringInHTMLWindows(program, url, body):
    import datetime
    from webbrowser import open_new_tab

    now = datetime.datetime.today().strftime("%Y%m%d-%H%M%S")

    filename = program + '.html'
    f = open(filename,'w')

    wrapper = """<html>
    <head>
    <title>%s output - %s</title>
    </head>
    <body><p>URL: <a href=\"%s\">%s</a></p><p>%s</p></body>
    </html>"""

    whole = wrapper % (program, now, url, url, body)
    f.write(whole)
    f.close()

    open_new_tab(filename)
```
\*\*\*

Note que essa função faz uso do operador de formatação de string sobre o qual acabamos de aprender. Caso ainda tenha problemas com essa ideia, verifique o ficheiro HTML que foi aberto numa nova guia do Firefox e verá como isso funcionou. Se ainda estiver preso nisso, dê uma olhada em

```
URL: http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33
```

no ficheiro HTML e investigue como o programa sabia colocar o valor da URL lá.

A função também chama a biblioteca Python `datetime` para determinar o horário e a data atuais. Como o operador de formatação de string `%s`, essa biblioteca usa `%` como substitutos para valores. Nesse caso, `%Y %m %d %H %M %S` representa ano (*year*), mês (*month*), data (*date*), hora (*hour*), minuto (*minute*) e segundo (*second*) respectivamente. Diferente de `%s`, o programa determinará o valor dessas variáveis usando o relógio do seu computador. É importante reconhecer essa diferença.

Esse metadado de data, junto com o nome do programa que chamou pela função, é armazenado no título da *tag* HTML. O ficheiro HTML que é criado possui o mesmo nome do programa Python que o criou, mas com uma extensão `.html` ao invés de uma `.py`.

## Juntando tudo

Agora podemos criar outra versão do nosso programa para computar frequências. Ao invés de enviar seu resultado a um ficheiro de texto ou uma janela de saída, ele envia o resultado para um ficheiro HTML que é aberto numa nova guia do Firefox. Daí em diante, as saídas do programa podem ser facilmente adicionadas como entradas bibliográficas no Zotero. Digite ou copie o comando a seguir no seu editor de texto, armazene-o como `html-to-freq-3.py` e execute-o para confirmar que ele funciona como esperado.

Use `obo.wrapStringInHTMLMac()` ou `obo.wrapStringInHTMLWindows()` de acordo com o que for apropriado para o seu sistema: 


``` python
# html-to-freq-3.py
import obo

# cria um dicionário ordenado de pares palavra-frequência
url = 'http://www.oldbaileyonline.org/browse.jsp?id=t17800628-33&div=t17800628-33'
text = obo.webPageToText(url)
fullwordlist = obo.stripNonAlphaNum(text)
wordlist = obo.removeStopwords(fullwordlist, obo.stopwords)
dictionary = obo.wordListToFreqDict(wordlist)
sorteddict = obo.sortFreqDict(dictionary)

# compila o dicionário em string e envolve com HTML
outstring = ""
for s in sorteddict:
    outstring += str(s)
    outstring += "<br />"
obo.wrapStringInHTMLMac("html-to-freq-3", url, outstring)
```

Note que intercalamos nossos pares palavra-frequência com a *tag* HTML de quebra `<br\>`, que atua como uma nova linha. Se tudo correu bem, você deverá ver as mesmas frequências de palavra que calculou na última seção, desta vez na janela do navegador.

### Leituras Sugeridas

-   Lutz, Learning Python
    -   Re-read and review Chs. 1-17

### Sincronização de Código

Para acompanhar lições futuras, é importante ter os ficheiros e programas corretos no seu diretório “programming-historian”. Ao final de cada capítulo você pode fazer o *download* do ficheiro zip "programming-historian" para garantir que possui o código correto. Caso esteja acompanhando com a versão para Mac / Linux, você deve ter que abrir o ficheiro `obo.py` e mudar "file:///Users/username/Desktop/programming-historian/" para o caminho até o diretório no seu próprio computador.

-   [python-lessons7.zip][zip sync]





  [Contagem de Frequências]: /licoes/contagem-frequencias
  [ficheiro zip da lição anterior]: https://programminghistorian.org/assets/python-lessons6.zip
  [zip sync]: https://programminghistorian.org/assets/python-lessons7.zip