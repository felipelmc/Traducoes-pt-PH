---
title: Editando Áudio com Audacity
layout: lesson
slug: editando-audio-com-audacity
date: 2016-08-05
translation_date: 2021-07-29
authors:
- Brandon Walsh
reviewers:
- Joanna Swafford
- Celeste Tường Vy Sharpe
editors:
- Jeri Wieringa
translator:
- Felipe Lamarca
translation-editor:
- 
translation-reviewer:
- 
difficulty: 1
review-ticket: 
activity: transformação
topics: [data-manipulation]
abstract: "In this lesson you will learn how to use Audacity to load, record, edit, mix, and export audio files."
redirect_from: 
original: editing-audio-with-audacity
avatar_alt: Two gramophones facing each other
---

{% include toc.html %}

## Objetivos do Módulo

Para aqueles interessados em áudio, habilidades básicas de edição de som são muito úteis. Ser capaz de manusear e manipular esses materiais podem ajudar a assumir o controle do seu objeto de estudo: você pode ampliar e extrair momentos específicos para analisar, processar o áudio, e hospedar os materiais em um servidor para complementar uma postagem de blog sobre o assunto. Num nível mais prático, essas habilidades também podem permitir que você grave e compile suas gravações ou de outras pessoas para distribuição. Aquela palestra acontecendo em seu departamento? Grave e edite você mesmo! Fazer isso é uma maneira leve de distribuir recursos entre várias instituições e também ajuda a tornar os materiais mais acessíveis para leitores e ouvintes com uma ampla variedade de necessidades de aprendizagem.

Nesta lição você aprenderá como utilizar o [*Audacity*](https://www.audacityteam.org/) para carregar, gravar, editar, mixar e exportar ficheiros de áudio. Plataformas de edição de som costumam ser caras e oferecem grandes quantidades de recursos, o que pode ser demais para um usuário iniciante. Mas o Audacity pe uma alternativa gratuita e de código aberto que oferece recursos poderosos para edição de som com uma baixa barreira de entrada.

Para esta lição, utilizaremos dois ficheiros de áudio: uma gravação das [Variações Goldberg de Bach](https://programminghistorian.org/assets/editing-audio-with-audacity/bach-goldberg-variations.mp3) e outra gravação da sua própria voz que será feita no decorrer da lição.

Esse tutorial utiliza *Audacity 2.3.3*, lançado em novembro de 2019.

## Trabalhando com o Audacity

Primeiro, faça o download dos ficheiros necessários.

Você precisará do ficheiro mp3 das [Variações Goldberg de Bach](https://programminghistorian.org/assets/editing-audio-with-audacity/bach-goldberg-variations.mp3). Para fazer o download, clique com o botão direito [aqui](https://programminghistorian.org/assets/editing-audio-with-audacity/bach-goldberg-variations.mp3) e selecione 'Salvar link como...' para fazer o download do ficheiro para dentro do seu computador como um MP3.

Em seguida, faça o download e instale o *Audacity*, disponível no [site do projeto](https://www.audacityteam.org/). *Audacity* pode ser usado no Mac OSX, Windows ou Linux.

Faça o download do programa e clique duas vezes para instalar.

Para começar, abra a gravação do Bach que você acabou de baixar utilizando o menu de ficheiros do *Audacity*.

A interface mudará para apresentar os dados carregados:

{% include figure.html filename="editando-audio-com-audacity-1.png" caption="Forma de onda de Bach no Audacity" %}

*Audacity* converte seu som em formas de onda, um modo comumente utilizado para representar som. O eixo x representa o tempo em segundos (ou minutos e segundos, dependendo da duração do clipe). O início do som ocorre na extremidade esquerda da interface e o Audacity marca os marcadores de tempo periódicos conforme a onda continua para a direita. Se clicarmos no botão 'Reproduzir', *Audacity* moverá da esquerda para a direita sobre o som, coim uma linha vertical representando nosso ponto atual no clipe.

O eixo y representa amplitude, o que entendemos como intensidade ou volume. Por padrão, o eixo y mede o volume numa escala linear vertical de -1 a 1: os extremos -1 e 1 representam o som gravado mais alto possível sem distorção, enquanto 0 representa o silêncio. Portanto, o silêncio começa com uma linha plana e o som fica mais alto e mais profundo à medida que aumenta de intensidade. Para obter mais informações sobre por que alguns dos números são negativos, consulte a breve [introdução à acústica](https://web.archive.org/web/20161119231053/http://www.indiana.edu:80/~emusic/acoustics/amplitude.htm) de Jeffrey Hass.

As representações de tempo e amplitude do *Audacity* são os seus primeiros e mais simples pontos de referência para edição de sons, e a ferramenta oferece maneiras práticas de navegar entre eles. Eu continuo chamando isso de onda, mas ainda não se parece muito com uma. Vamos dar uma olhada mais de perto, selecionando uma parte da trilha de áudio.

- Clique em algum lugar sobre a onda para começar a selecionar
- Arraste para destacar um pedaço da onda (qualquer parte com som funcionará). Se não estiver satisfeito com a seleção, você pode arrastar as bordas de sua seleção para ajustar os limites.
- Uma vez que tenha um recorte com que esteja satisfeito, selecione 'Zoom' e, em seguida, 'Aumentar Zoom' no menu de exibição.

Se você aumentar o zoom seis ou sete vezes, começará a ver algo que pode se parecer mais com uma onda senoidal:

{% include figure.html filename="editando-audio-com-audacity-2.png" caption="Visão ampliada da forma de onda de Bach" %}

