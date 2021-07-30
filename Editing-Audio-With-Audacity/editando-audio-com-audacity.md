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
abstract: "Nessa lição você aprenderá a utilizar o Audacity para carregar, gravar, editar, juntar e exportar ficheiros de áudio."
redirect_from: 
original: editing-audio-with-audacity
avatar_alt: Two gramophones facing each other
---

{% include toc.html %}

## Objetivos do Módulo

Para aqueles interessados em áudio, habilidades básicas de edição de som são muito úteis. Ser capaz de manusear e manipular esses materiais pode ajudar a assumir o controle do seu objeto de estudo: você pode ampliar e extrair momentos específicos para analisar, processar o áudio, e hospedar os materiais num servidor para complementar uma postagem de blog sobre o assunto. Num nível mais prático, essas habilidades também podem permitir que você grave e compile suas gravações ou de outras pessoas para distribuição. Aquela palestra acontecendo em seu departamento? Grave e edite você mesmo! Fazer isso é uma maneira leve de distribuir recursos entre várias instituições e também ajuda a tornar os materiais mais acessíveis para leitores e ouvintes com uma ampla variedade de necessidades de aprendizagem.

Nesta lição você aprenderá como utilizar o [*Audacity*](https://www.audacityteam.org/) para carregar, gravar, editar, juntar e exportar ficheiros de áudio. Plataformas de edição de som costumam ser caras e oferecem grandes quantidades de recursos, o que pode ser demais para um usuário iniciante. Mas o Audacity é uma alternativa gratuita e de código aberto que oferece recursos poderosos para edição de som com uma baixa barreira de entrada.

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

*Audacity* converte seu som em formas de onda, um modo comumente utilizado para representar som. O eixo x representa o tempo em segundos (ou minutos e segundos, dependendo da duração do clipe). O início do som ocorre na extremidade esquerda da interface e o Audacity marca os marcadores de tempo periódicos conforme a onda continua para a direita. Se clicarmos no botão 'Reproduzir', *Audacity* moverá da esquerda para a direita sobre o som, com uma linha vertical representando nosso ponto atual no clipe.

O eixo y representa amplitude, o que entendemos como intensidade ou volume. Por padrão, o eixo y mede o volume numa escala linear vertical de -1 a 1: os extremos -1 e 1 representam o som gravado mais alto possível sem distorção, enquanto 0 representa o silêncio. Portanto, o silêncio começa com uma linha plana e o som fica mais alto e mais profundo à medida que aumenta de intensidade. Para obter mais informações sobre por que alguns dos números são negativos, consulte a breve [introdução à acústica](https://web.archive.org/web/20161119231053/http://www.indiana.edu:80/~emusic/acoustics/amplitude.htm) de Jeffrey Hass.

As representações de tempo e amplitude do *Audacity* são os seus primeiros e mais simples pontos de referência para edição de sons, e a ferramenta oferece maneiras práticas de navegar entre eles. Eu continuo chamando isso de onda, mas ainda não se parece muito com uma. Vamos dar uma olhada mais de perto, selecionando uma parte da faixa de áudio.

* Clique em algum lugar sobre a onda para começar a selecionar.
* Arraste para destacar um pedaço da onda (qualquer parte com som funcionará). Se não estiver satisfeito com a seleção, você pode arrastar as bordas de sua seleção para ajustar os limites.
* Uma vez que tenha um recorte com que esteja satisfeito, selecione 'Zoom' e, em seguida, 'Aumentar Zoom' no menu de exibição.

Se você aumentar o zoom seis ou sete vezes, começará a ver algo que pode se parecer mais com uma onda senoidal:

{% include figure.html filename="editando-audio-com-audacity-2.png" caption="Visão ampliada da forma de onda de Bach" %}

Observe como os incrementos de tempo no Audacity também se ajustam conforme você aumenta o zoom. As frequências de pitch são medidas em ondas por segundo, e o programa precisa quebrar as coisas um pouco para fazer todo o clipe de som caber numa janela viável. O resultado é o formato de onda que vemos quando afastamos o zoom selecionando 'Zoom Normal' em 'Zoom', no menu Exibir. Cada visualização - a micro e a macro - possui seus próprios usos. Voltaremos a ambas.

{% include figure.html filename="editando-audio-com-audacity-3.png" caption="Paleta de reprodução do Audacity" %}

Antes de continuar, vale a pena observar as várias paletas que o *Audacity* oferece para as suas funções mais comuns. A paleta de reprodução oferece símbolos que provavelmente são familiares: botões que permitem pausar, reproduzir, parar, avançar rapidamente para o início ou fim dum clipe e gravar.

{% include figure.html filename="editando-audio-com-audacity-4.png" caption="Paleta de ferramentas do Audacity" %}

A paleta de ferramentas, por outro lado, provavelmente é novidade. Não discutiremos todas as funcionalidades que o *Audacity* oferece, então alguns desses botões não serão utilizados. No entanto, note: a 'Ferramenta Seleção' superior esquerda e a 'Ferramenta Mover' inferior central são as duas que usaremos nesta lição. Por padrão, ao abrir o *Audacity*, você estará utilizando a ferramenta de seleção.

## Gravando um Áudio

Nós carregamos a música de introdução do nosso podcast. Vamos continuar, agora gravando nossa própria voz.

* Por padrão, o *Audacity* irá reproduzir e regravar sua faixa original quando você tenta gravar uma nova. Para contornar isso, você pode silenciar temporariamente sua faixa de Bach enquanto grava sua voz. Para silenciar a faixa, clique no botão 'Silenciar' à esquerda das ondas sonoras de Bach. A faixa de Bach ficará cinza para mostrar que ela não será reproduzida.

* Para começar a gravar no *Audacity*, pressione o botão grande e vermelho na parte superior esquerda da janela do *Audacity*. Não se preocupe muito com a qualidade - trabalharemos na edição do ficheiro de som em seguida.

* Faça sua melhor impressão NPR na direção de seu computador e clique no quadrado para parar de gravar quando terminar.

Você verá algo parecido com isso:

{% include figure.html filename="editando-audio-com-audacity-5.png" caption="Duas faixas carregadas no Audacity" %}

Nossa gravação original do Bach permanece no topo da interface, enquanto nossa nova gravação é adicionada abaixo dela. Por padrão, *Audacity* não irá sobrescrever sua gravação anterior. Ao contrário, ele isola cada uma das gravações, ou faixas, nos permitindo manipular separamente os componentes antes de uní-los numa gravação final. Podemos fazer modificações num sem afetar o outro. Note como, em termos de tempo, a nova faixa, por padrão, foi gravada no início do projeto audacity. Por enquanto, as faixas Bach e vocal começam ao mesmo tempo. Existem potencialmente algumas outras imperfeições em sua gravação pessoal, algumas das quais podemos consertar.

Por fim, note como no meu exemplo há duas formas de onda para a gravação do Bach, mas apenas uma para a gravação da minha própria voz. A gravação do Bach foi feita em *estéreo*, o que significa que havia dois feeds de entrada, enquanto a minha gravação própria foi feita em mono. O Audacity permite que você grave em ambos, e qualquer um funcionará para esta lição, então não se preocupe se sua gravação aparecer em estéreo. Você pode mudar de gravação mono para estéreo e vice-versa na barra de ferramentas 'Editar'. Para obter mais informações sobre mono e estéreo, verifique esta [leitura](http://www.diffen.com/difference/Mono_vs_Stereo).

Um adendo: frequentemente pode ser útil transformar a saída de som do seu laptop em sua entrada, para que você possa gravar sons reproduzidos no seu computador sem se preocupar com ruídos externos ou regravar o áudio original. Para obter informações sobre como realizar este processo, consulte o [Soundflower](https://github.com/mattingalls/Soundflower).

## Editando Áudio

O tópico de engenharia de áudio é vasto e pode ser assunto duma carreira frutífera e longa - não podemos esperar esgotar todos os tópicos aqui. Mas podemos oferecer algumas técnicas básicas úteis para trabalhar com áudios digitais. Suas experiências podem variar de acordo com o caráter da sua própria gravação.

Para utilizar a faixa gravada, precisaremos limpá-la um pouco, isolando e refinando as partes que queremos. Nosso primeiro passo será remover o silêncio indesejado criado no intervalo entre quando comecei a gravar e quando comecei a falar.

* Aproximar o zoom no início do clipe nos dará uma visão do silêncio e, clicando e arrastando as seções da forma de onda, podemos eliminá-las pressionando a tecla delete. 

{% include figure.html filename="editando-audio-com-audacity-6.png" caption="Início da faixa vocal pronto para ser deletado" %}

{% include figure.html filename="editando-audio-com-audacity-7.png" caption="Início da faixa após o delete" %}

Essas pequenas pausas podem ser praticamente imperceptíveis, mas são elementos importantes de qualquer faixa de áudio. E queremos que os limites da nova faixa de áudio não contenha dados estranhos. Após a exclusão, você deve ter um clipe de áudio bonito e compacto com apenas um fio de silêncio em cada extremidade.

Para garantir transições suaves entre as faixas, precisaremos introduzir fades ou transições graduais em amplitude. É uma boa ideia incluir uma pequena suavização de áudio de entrada (*fade in*) no início e uma suavização de áudio de saída (*fade out*) no final que o leva ao silêncio. Isso pode ajudar a prevenir cliques e falhas, evitando que o som apareça ou suma de forma repentina.

* Aproxime o zoom no início da faixa, destaque o início da onda, incluindo apenas um fio de cabelo do seu som-alvo, e selecione 'Suavização de Entrada' no menu 'Efeitos'.

Se você selecionou apenas uma pequena parte do áudio, pode não ser capaz de ver as alterações que as suavizações causaram. Estas capturas de tela com ultra zoom ajudarão:

{% include figure.html filename="editando-audio-com-audacity-8.png" caption="Faixa antes da suavização de entrada" %}

{% include figure.html filename="editando-audio-com-audacity-9.png" caption="Faixa depois da suavização de entrada" %}

A suavização de entrada dimuiu dramaticamente a amplitude de início e introduziu algumas mudanças muito graduais na amplitude ao longo das seções da faixa que foram destacadas, suavizando as coisas e criando a percepção dum aumento de volume.

* Repita o processo ao final do clipe, mas agora com a 'Suavização de Saída'.

Seu clipe será configurado para ser inserido sem problemas em qualquer ponto do ficheiro.

Eliminar o silêncio e o som indesejado preparou o clipe, mas ainda precisamos movê-lo para o momento em que desejamos que ele seja reproduzido. Queremos posicioná-lo na parte apropriada do podcast, após a música de introdução ter tocado um pouco. Para mover o clipe horizontalmente no eixo x e reatribuí-lo a uma nova posição no tempo, use a 'Ferramenta Mover'. Com essa ferramenta selecionada, clicar num clipe de som permite movê-lo horizontalmente no tempo em relação às outras faixas.

* Mova nosso clipe vocal para a direita, de modo que ele comece após a música de introdução ter tocado por alguns segundos.


{% include figure.html filename="editando-audio-com-audacity-10.png" caption="Reposicionando o clipe de áudio no tempo" %}

Se o volume da sua voz em relação à música de introdução parecer desequilibrado, você pode reorganizá-los para serem mais equilibrados. O volume geral duma faixa particular pode ser ajustado usando o controle deslizante de volume da faixa à esquerda de cada painel de faixa. Parece uma pequena escala -/ +:


{% include figure.html filename="editando-audio-com-audacity-11.png" caption="Controle deslizante de volume" %}

Mas, eventualmente, desejaremos mudar totalmente o foco da música de introdução e dar uma nova ênfase à gravação da nossa voz. Um *crossfade* como este é fácil de implementar no *Audacity*.

* Primeiro, exclua tudo exceto os primeiros 5 segundos da introdução do Bach. Posicione seu cursor no local da faixa onde você quer começar a excluir e pressione 'Shift K', ou selecione 'Selecionar/Limites do clipe/Cursor no limite do próximo clipe'. Isso selecionará tudo entre a localização do seu cursor e o final da faixa.

* Alinhe o que sobrou com a sua faixa vocal usando a 'Ferramenta Mover' de modo que as duas faixas de sobreponham ligeiramente.

* Depois utilize a ferramenta de seleção para clicar e arrastar para destacar a seção na qual eles se sobrepõem, começando com a faixa superior e terminando na inferior. Ambas as faixas devem ser destacadas.

{% include figure.html filename="editando-audio-com-audacity-12.png" caption="Destacando as faixas para crossfading" %}

* Selecionar 'Crossfade de faixas...' no menu de Efeitos informará ao *Audacity* para suavizar a saída da faixa de cima e ao mesmo tempo suavizar a entrada da faixa de baixo - o posicionamento das faixas importa nesse caso.

*Audacity* irá apresentar opções para o seu crossfade, mas por enquanto está tudo bem utilizar a configuração padrão de 'Ganho Constante'. Esta configuração garante que ambas as faixas serão suavizadas na entrada ao linearmente (para mais informações, verifique a [documentação do Audacity sobre crossfades](http://manual.audacityteam.org/man/crossfade_tracks.html)).


{% include figure.html filename="editando-audio-com-audacity-13.png" caption="Pós-crossfade" %}

Quando as duas faixas forem combinadas, o resultado será uma transição perfeita entre os dois elementos.

## Exportando

Por padrão, tudo que você faz no *Audacity* é salvo no próprio tipo de ficheiro da ferramenta, .aup. Para concluir este mini-projeto, precisaremos exportá-lo num formato em que ele possa ser reproduzido pela maioria dos programas de áudio.

* Selecione 'Exportar' no menu de ficheiro.

Isto irá unir as várias faixas num único ficheiro de áudio e dará a você a oportunidade de fornecer metadados ao seu trabalho.

Existem várias opções diferentes para você refinar o processo de exportação, mas a mais importante é o tipo de ficheiro. MP3 e Ogg são boas opções de áudio para exibição na web, pois ambos compactam os ficheiros para que sejam carregados mais rapidamente. Para obter melhores resultados, você pode incluir os dois formatos e exibir um como substituto quando não for compatível com o navegador do usuário. Para obter mais informações, *NCH Software* fornece uma [boa análise técnica das diferentes opções](https://www.nch.com.au/acm/formats.html), enquanto Jonathan Sterne fez um [trabalho fascinante](https://www.dukeupress.edu/MP3/) sobre as implicações culturais de tais decisões de formato. E o W3Schools oferece uma [boa comparação](https://www.w3schools.com/html/html5_audio.asp) desses formatos de ficheiro para uso em desenvolvimento web.

Parabéns! Você produziu com sucesso um mini-podcast. Pode não parecer muito, mas eu frequentemente emprego esses mesmos truques para apresentações, sites e bolsas de estudo. Essa lição não começou de forma alguma a esgotar os muitos tópicos sob esse guarda-chuva. Mas deve ter dado a você algumas ferramentas básicas úteis para trabalhar com som em projetos de humanidades digitais.




