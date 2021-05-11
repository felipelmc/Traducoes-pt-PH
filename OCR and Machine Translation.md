OCR e Tradução Automática
=========================
Sumário
-------------
* Introdução
	* Objetivos da Lição
* Configurações
	* Linha de Comando e Bash
	* Obtenha os Dados
	* Processamento de Imagem                                
		* Instalando ImageMagick
			* Instalação no Mac
			* Instalação no Windows
		* Conversão de PDFs em TIFFs com ImageMagick
* OCR
* Tradução
* Unindo tudo em um laço de repetição
* Resultados
* Outras Possibilidades com Scripting e ImageMagick
	* Editando seus documentos com ImageMagick
	* Organize seus documentos
* Conclusões

Introdução
=========

Essa lição trata dos benefícios e dos desafios de se aplicar técnicas de reconhecimento óptico de caracteres (OCR) e tradução automática em pesquisas da área de humanidades. Muitos dos meus colegas historiadores são céticos quanto a investir tempo no aprendizado de técnicas digitais porque não veem benefícios em suas pesquisas. Mas vivemos em um mundo onde nosso alcance digital muitas vezes ultrapassa nossa compreensão. Investigadores podem acessar milhares de páginas de coleções digitais _online_ ou usar seus próprios celulares para capturar milhares de páginas de documentos em um único dia. O acesso a esse volume e variedade de documentos, no entanto, também apresenta problemas. Gerenciar e organizar milhares de ficheiros de imagem não é uma tarefa fácil utilizando uma interface gráfica de usuário (_graphical user interface_). Além do mais, ainda que o acesso aos documentos dependa menos da proximidade geográfica, a linguagem na qual o texto está escrito é capaz de restaurar as fronteiras. Ter acesso aos documentos não é a mesma coisa que entendê-los. Ferramentas de linhas de comando, como simples _scripts_ Bash, nos oferecem soluções para esses problemas comuns e podem tornar muito mais fácil a organização e a edição de ficheiros de imagem. A combinação de reconhecimento óptico de caracteres (OCR) e tradução automática (APIs), como Google Tradutor e Bing, nos promete um mundo onde qualquer texto pode ser pesquisado através de palavras-chave e traduzido. Mesmo que os programas específicos demonstrados nessa lição não sejam do seu interesse, o poder da programação ficará evidente. Combinar múltiplas ferramentas de linha de comando e desenvolver projetos a partir delas é essencial para fazer as ferramentas digitais trabalharem para você.

Objetivos da Lição
----------------
1. Aprender como preparar documentos para OCR
2. Criar um _script_ Bash que irá preparar, executar o OCR e traduzir todos os documentos em uma pasta
3. Aprender como criar _scripts_ para organizar e editar seus documentos
4. Entender as limitações do OCR e da tradução automática

Configurações
===========

Linhas de Comando e Bash
-------------------------------
Esse tutorial usa a [linguagem Bash de script](https://en.wikipedia.org/wiki/Bash_%28Unix_shell%29). Caso não esteja confortável com Bash, tire um momento para revisar o tutorial do _Programming Historian_ "[Introduction to the Bash Command Line](https://programminghistorian.org/en/lessons/intro-to-bash)" (para usuários de Linux e Mac) ou "[Introduction to the Windows Command Line with PowerShell](https://programminghistorian.org/en/lessons/intro-to-powershell)" (para usuários de Windows). Bash vem instalado no sistema operacional do Linux e do Mac.

Será necessário instalar mais alguns programas. O resto desta seção ensinará como instalar os programas requeridos através de linhas de comando.

Agora está na hora do nosso primeiro comando. Abra o Terminal e insira o comando `cd Desktop` para mover o seu [diretório de trabalho](https://en.wikipedia.org/wiki/Working_directory) para a Área de Trabalho.

Obtenha os dados 
----------------------
Para esse tutorial, serão utilizados dois documentos da Coleção do Arquivo Digital do Wilson Center sobre as relações entre Irã e União das Repúblicas Socialistas Soviéticas (URSS). Baixe a "[Mensagem de Bagirov para Aleksanriv sobre as impressoras](https://digitalarchive.wilsoncenter.org/document/120500)" (Exemplo Um) e a "[Carta, Dimitrov para Molotov, A Situação do Partido do Povo do Irã](https://digitalarchive.wilsoncenter.org/document/119105)" (Exemplo Dois). Esses documentos são originalmente do Arquivo de Partidos Políticos e Movimentos Sociais do Estado do Azerbaijão. Ambos os documentos estão em russo e abordam principalmente a [Crise do Irã de 1946](https://en.wikipedia.org/wiki/Iran_crisis_of_1946). Selecionei esses documentos por duas razões. Um, os documentos estão escaneados em alta qualidade, mas possuem defeitos comuns a muitos documentos em arquivos. Dois, cada documento possui uma tradução para o inglês, de modo que poderemos julgar a qualidade/acurácia das nossas traduções automáticas.

Salve ambos os documentos em uma pasta na sua Área de Trabalho. De agora em diante, irei me referir aos dois documentos como Exemplo Um e Exemplo Dois. O Exemplo Um possui muitos ruídos, isto é, variações indesejadas de cor e brilho. Como é possível perceber, a imagem está distorcida e há escrita em diferentes fontes e tamanhos, marcações erradas e danos visíveis ao documento. Embora não possamos remover todos os ruídos, podemos minimizá-los com o pré-processamento da imagem.

Processamento da Imagem
---------------------------------
O fator que mais importa para a acurácia do OCR é a qualidade da imagem que utilizada. Uma vez que a foto é tirada, é impossível melhorar sua resolução. Além disso, uma vez que a resolução da imagem é diminuída, é impossível restaurá-la. É por isso que você deve manter uma cópia de cada ficheiro de imagem que utilizará. O ideal é que a cópia do ficheiro esteja no formato TIFF, porque outros formatos de ficheiro (especialmente JPG) comprimem os dados de modo que uma parte da qualidade da fotografia original é perdida. Consequentemente, ficheiros JPG são muito menores que ficheiros TIFF, o que não é necessariamente um problema. Caso esteja trabalhando com documentos datilografados que sejam claramente legíveis, não é necessário que se preocupe. Mas se estiver trabalhando com documentos mais antigos, danificados ou manuscritos, você deve precisar de resolução extra nas suas imagens.

Ao escanear ou fotografar um documento, tenha certeza de que há luz suficiente ou que o _flash_ está ativado, para evitar que a imagem fique muito escura (ex.: use o _flash_ da câmera ou luzes externas adicionais) e evite fotografar de um ângulo inclinado. Em outras palavras, as linhas do texto no documento devem aparecer retas na imagem.

Frequentemente ficamos presos a imagens que possuem ruídos significativos. Por exemplo, não podemos remover danos do documento original. Há passos que podemos tomar para otimizar a imagem para OCR e melhorar a taxa de acurácia. A primeira coisa que teremos que fazer é instalar uma ferramenta gratuita de linha de comando chamada [ImageMagick](https://imagemagick.org).

### Instalando ImageMagick

#### Instalação no Mac
Usuários de Mac precisarão instalar um gerenciador de pacotes chamado Homebrew. Instruções de instalação podem ser encontradas no [_website_ do Homebrew](https://brew.sh). Para o sistema operacional do Mac, a instalação requer que você entre com dois comandos simples na janela do terminal: `brew install imagemagick` `brew install ghostscript`

#### Instalação no Windows

As instruções de instalação do ImageMagick no Windows podem ser encontradas no [_website_ do ImageMagick](http://imagemagick.sourceforge.net/http/www/windows.html).

### Conversão de PDFs em TIFFs com ImageMagick

Com o ImageMagick instalado, podemos agora converter nossos ficheiros de PDF para TIFF e fazer algumas alterações nos ficheiros que nos ajudarão a melhorar a acurácia do OCR. Programas OCR aceitarão somente ficheiros de imagem (JPG, TIFF, PNG) como entrada, então você precisará fazer a conversão de PDFs. O seguinte comando fará a conversão de um PDF e tornar mais fácil a execução do OCR:

  `convert -density 300 NOME_FICHEIRO_ENTRADA.pdf -depth 8 -strip -background white -alpha off NOME_FICHEIRO_SAÍDA.tiff`

O comando executa várias ações que melhoram significativamente a taxa de acurácia do OCR. Os comandos `density` e `depth` garantem que o ficheiro tenha os pontos por polegada [(DPI)](https://en.wikipedia.org/wiki/Dots_per_inch) apropriados para OCR. Os comandos `strip`, `backgroud` e `alpha` garantem que o ficheiro tenha o plano de fundo correto. Mais importante: esse comando converte  o ficheiro PDF em TIFF. Ainda que você não esteja utilizando um PDF, você ainda deve usar o comando acima para assegurar que a imagem está pronta para OCR.

Após essas mudanças, a imagem pode ainda ter problemas. Por exemplo, é possível que haja alguma inclinação ou brilho desigual. Felizmente, ImageMagick é uma ferramenta poderosa que pode nos ajudar a limpar ficheiros de imagem. Para outras opções do ImageMagick que podem melhorar a qualidade do OCR, revise esta útil [coleção de scripts](http://www.fmwconcepts.com/imagemagick/textcleaner/index.php). Uma vez que OCR é uma ferramenta de linha de comando, é possível escrever um script que faz um laço de repetição que passa por todas as suas imagens (centenas e milhares) de uma vez só. Você aprenderá a escrever esse tipo de script mais a frente nessa lição.

OCR
====

Essa lição utilizará o programa [Tesseract](https://github.com/tesseract-ocr/tesseract), o programa que executa OCR mais popular entre os projetos de Humanidades Digitais. O Google mantem o Tesseract como um software gratuito e lançado sob a licença Apache, Versão 2.0. O Tesseract suporta mais de 100 idiomas diferentes, mas caso haja um script particularmente difícil ou único (caligrafia ou outro tipo de manuscrito), pode valer a pena treinar seu próprio modelo de OCR. Para documentos datilografados, é necessário um programa que reconhecerá várias fontes similares e identificar corretamente letras imperfeitas. Tesseract 4.1 faz exatamente isso. O Google já treinou o Tesseract para reconhecer uma variedade de fontes de dezenas de idiomas. Os comandos a seguir farão a instalação do Tesseract, assim como do pacote do idioma russo, que será necessário para o resto dessa lição:

`sudo port install tesseract` `sudo port install tesseract-rus`

Instruções de instalação no Windows podem ser encontradas na [documentação do GitHub do Tesseract](https://github.com/UB-Mannheim/tesseract/wiki).

Os comandos para o Tesseract são relativamente simples. Apenas digite: 

`tesseract NOME_FICHEIRO_ENTRADA NOME_FICHEIRO_SAÍDA -l rus`

Nossa saída é a transcrição do ficheiro de entrada como um ficheiro de texto simples em russo. O parâmetro `-l` especifica o idioma de origem do documento. Outras opções de parâmetro podem ser encontradas na [documentação do GitHub do Tesseract](https://github.com/UB-Mannheim/tesseract/wiki).

Tradução
=======
[Translate Shell](https://www.soimort.org/translate-shell/#translate-shell) é um programa gratuito que permite que você acesse a API de ferramentas de tradução automática como [Google Translate](https://translate.google.com), [Bing Translator](https://www.bing.com/translator), [Yandex.Translate](https://translate.yandex.com) e [Apertium](https://www.apertium.org/index.eng.html?dir=arg-cat#translation) através da linha de comando, ao invés de um navegador na web. Para esse exercício, utilizaremos o Yandex em função da boa reputação desse programa em traduções do russo para o inglês e um alto limite de solicitações. No entanto, Yandex não suporta tantas linguagens quanto outros tradutores. Embora as APIs de tradução não cobrem per se, elas limitam de várias formas o quanto é possível acessar através das linhas de comando. Por exemplo, há um limite de 5.000 caracteres por solicitação para o Google Translate. Portanto, caso você envie ao API um ficheiro de texto de 10.000 caracteres, o Google Translate traduzirá os primeiros 5.000 e parar. Caso faça uma quantidade muito grande de solicitações dentro de um curto intervalo de tempo, o API bloqueará temporariamente o endereço de IP. É preciso experimentar para decidir qual API de tradução funciona melhor para cada caso.

Para instalar o Translate Shell, é necessário fazer o download e rodar o pacote de instalação. Entre com os comandos a seguir no terminal:

`wget git.io/trans`

E depois

`chmod +x ./trans`

Usar o Translate Shell é relativamente fácil. A linha abaixo pega um ficheiro, o traduz para o inglês e salva o resultado.

`trans -e yandex :eng file://NOME_FICHEIRO_ENTRADA > NOME_FICHEIRO_SAÍDA`

O [parâmetro](https://en.wikipedia.org/wiki/Parameter_%28computer_programming%29) `-e` especifica o tradutor que deseja-se utilizar.

Unindo tudo em um laço de repetição
===============================

Até agora, passamos pelos comandos individuais de pré-processamento, execução do OCR e tradução dos nossos documentos. Essa seção cobrirá como automatizar esse processo com um script e iterar comandos sobre todos os documentos em uma pasta.

Primeiro, é necessário abrir o [Nano](https://en.wikipedia.org/wiki/GNU_nano) e começar a escrever o script. Nano é um editor de texto gratuito e disponível nos sistemas Linux e MacOS. É simples de usar, mas tem alguns dos recursos de edição que seriam vistos em [Emacs](https://en.wikipedia.org/wiki/Emacs) ou [Vim](https://en.wikipedia.org/wiki/Vim_%28text_editor%29). Qualquer editor de texto servirá. Não é possível utilizar o seu cursor no Nano. Em vez disso, você terá que navegar utilizando as teclas de seta e `enter`. Nosso script será bem pequeno, então os recursos de edição limitados do Nano não serão um problema. Quando escrever programas mais longos, recomenda-se que utilize editores de texto mais avançados. Abra o Nano digitando `nano NOME_DESEJADO` na linha de comando.

Em seguida, você deve entrar em uma [_shebang_](https://en.wikipedia.org/wiki/Shebang_%28Unix%29). Essa linha de comando dirá ao computador em qual linguagem o seu script está escrito. Para um script Bash, a linha é `#!/bin/bash`.

O script que iremos escrever possui três partes. Primeiro, ele solicitará que entre em uma pasta onde os ficheiros de imagem estão armazenados. Em segundo lugar, ele irá preparar, executar o OCR e traduzir as imagens nesse ficheiro. Em terceiro lugar, ele irá salvar as transcrições e as traduções em ficheiros separados.

Para incorporar uma entrada do usuário, adicione `read -p` seguido por uma solicitação para o usuário. Por exemplo, as próximas duas linhas de código solicitarão que seja indicado o nome de uma pasta em sua área de trabalho e, em seguida, criarão uma variável contendo o caminho completo do ficheiro dessa pasta.

````
read -p "Informe o nome da pasta: " pasta;
FICHEIROS=/Users/andrewakhlaghi/Desktop/test_dir/$pasta/*
````

O nome da pasta que você indicar é atribuído à uma variável chamada `pasta` e depois é passada à variável `ficheiro` para completar o caminho do ficheiro.

Em seguida, precisaremos criar um laço de repetição para iterar sobre todos os ficheiros na pasta.

```
for f in $FICHEIROS;
do
  tiff=${f%.*}.tiff
  convert -density 300 $f -depth 8 -strip -background white -alpha off $tiff
  ocr=${f%.*}_ocr
  tlate=${f%.*}_trans
  tesseract $tiff $ocr -l rus
  trans -e yandex :eng file://$ocr.txt > $tlate.txt
  sleep 1m
done
```

A maior parte desse código deve ser familiar com o código de exemplo nas seções anteriores sobre ImageMagick, Tesseract e Translate Shell. Há três adições importantes para a iteração desses processos:

1. Há um laço de repetição. A primeira linha cria uma nova variável, `f`, que irá receber o nome de cada ficheiro no nosso diretório.
2. Nós usamos o nome do ficheiro de imagem para criar os nomes dos ficheiros transcritos e traduzidos. O comando `${VARIABLE%.*}` pega um ficheiro e remove a sua extensão. O comando `%` remove o sufixo. O comando `.*` especifica que o sufixo é um "." e qualquer coisa que o acompanhar.
3. O comando `sleep 1m` impede que o programa inice o mesmo processo para o ficheiro seguinte por um minuto. Isso permite que o ficheiro anterior termine de ser traduzido e escrito, assim como garante um espaçamento entre as requisições de tradução aos APIs, de modo que eles não irão bloquear o IP do usuário. Talvez seja necessário ajustar o tempo de suspensão à medida que as APIs mudam suas políticas sobre o que constitui "muitas" solicitações.

O terceiro e último bloco de código criará duas pastas para as transcrições e traduções e moverá todas as transcrições para uma pasta e todas as traduções para outra.

```
mkdir $pasta"_ocr"
mkdir $pasta"_translation"
mv *_ocr.txt *_ocr
mv *_trans.txt *_translation
```

Adicione todos os blocos juntos no seu ficheiro Nano. Lembre-se de incluir a _shebang_ correta no início do script. Uma vez que o ficheiro nano for salvo, é preciso torná-lo executável. Isto é, é necessário mudar as permissões no ficheiro para que ele seja tratado como um script. Insira o comando `chmod a+x NOME_FICHEIRO`. Para executar o ficheiro, escreva `./NOME_FICHEIRO`.

Resultados
=========
Ao observar a saída, você verá que a tradução automática e o OCR requerem uma edição significativa de alguém com conhecimento dos idiomas de origem e de destino, bem como do assunto em discussão.

Os resultados para o Exemplo Um mostram o quão importante é a qualidade da imagem de entrada. A imagem do Exemplo Um sofre tanto de angulação ruim quanto de uma quantidade significativa de ruídos. A presença de manchas, listras escuras e letras quebradas dificultam a classificação das letras pelo programa. A inclinação torna difícil para o programa reconhecer as linhas de texto. A combinação das duas fontes de erro produz uma transcrição muito pobre.

{% include figure.html filename="OCR-e-traducao-automatica-1.png" caption="Figura 1: Transcrição do Exemplo Um" %}

Os resultados do Exemplo Dois demonstram que, mesmo com uma boa imagem, nossa transcrição e tradução iniciais ainda irão conter erros. O Exemplo Dois possui caligrafia errônea, mas, no geral, é livre de ruídos e não está inclinado. Mesmo que a conversão da imagem em texto tenha uma quantidade relativamente pequena de erros, a máquina pode não entender como traduzir todas as palavras corretamente. Por exemplo, a tradução da segunda página do Exemplo Dois contem erros de tradução, “The party’s connection to the owls.” (ver Figura 2). Esse erro vem da abreviação de “советский” (soviético), que é "COB.". Um leitor humano poderia reconhecer esse ponto como um sinal de que a palavra é uma abreviação e completar o resto da palavra se baseando no contexto. Embora o programa OCR tenha transcrito corretamente o ponto, o tradutor não entendeu o que fazer com ele.

{% include figure.html filename="OCR-e-traducao-automatica-2.png" caption="Figura 2: A frase com "coruja" (owl) em russo" %}

{% include figure.html filename="OCR-e-traducao-automatica-3.png" caption="Figura 3: A frase com "coruja" (owl) está traduzida" %}

Outro problema na tradução são os hífens. Enquanto o Tesseract transcreve os hífens corretamente, nem o Tesseract nem o Yandex entenderam seus propósitos. Embora o hífen diga ao leitor para seguir a palavra até a próxima linha, os dois programas trataram as duas metades como palavras separadas. Obviamente é possível deletar os hífens individualmente, mas isso é tedioso. Uma forma de lidar com isso é criando um pequeno script de expressões regulares (ver o tutorial do Programming Historian ["Cleaning OCR’d text with Regular Expressions"](https://programminghistorian.org/en/lessons/cleaning-ocrd-text-with-regular-expressions)) para deletar o hífen e unir as duas linhas.

Além dos hífens e das abreviações, o Tesseract identificou dois "a"s como "@"s na nossa frase sobre corujas (_owls_). Considerando que [email](https://en.wikipedia.org/wiki/Email) não existia até o início dos anos 1960, é seguro assumir que qualquer "@" que apareça no documento é, na verdade, um "a" reconhecido incorretamente. Desse modo, podemos utilizar um script de expressões regulares ou as funções Find e Replace do seu editor de texto para fazer as substituições.

Você também pode utilizar o comando `sed` do Bash para editar seu documento. Por exemplo, o script `sed s/@/а/g FICHEIRO.txt` encontrará todos os caracteres "@" e irá substituí-los por "a".

Se a frase terminar com um hífen, o script `sed` abaixo deletará todos os hífens e unirá as duas linhas:

`sed -e :a -e '/-$/N; s/-\n//; ta' FICHEIRO.txt` 

{% include figure.html filename="OCR-e-traducao-automatica-4.png" caption="Figura 4: A mudança após algumas edições" %}

De modo bastante similar com os outros comandos mostrados anteriormente, é possível manter uma lista de comandos `sed` em um script mais longo e aplicá-los a outros documentos nos quais você queira executar OCR.

Após fazer as edições acima, coloque sua transcrição editada de volta na API de tradução. Veja a melhora na frase sobre corujas (_owls_). Fica evidente como algumas poucas edições podem melhorar radicalmente a qualidade das nossas traduções.

{% include figure.html filename="OCR-e-traducao-automatica-5.png" caption="Figura 5: A tradução melhorada" %}

Outras Possibilidades com Scripting e ImageMagick
===================

Editando seus documentos com ImageMagick
------------------------------------------------------

Também é possível escrever um script para editar as próprias imagens. Você já aprendeu como utilizar o ImageMagick para preparar um ficheiro para OCR, mas ImageMagick também possui mais opções para edição de imagens. Ao olhar para o Exemplo Um, três tarefas serão executadas para melhorar a acurácia do OCR:

1. Recortar a imagem e remover o excesso de espaço nas margens ao redor do documento.
2. Endireitar a imagem para que as linhas de texto fiquem paralelas à parte inferior do documento.
3. Remover todos os ruídos, especialmente as manchas escuras, que aparecem ao longo do documento.

Todas as três tarefas podem ser iteradas em um script.

Os comandos de recorte serão específicos para cada documento. Há programas capazes de detectar e cortar ao redor do texto. No entanto, esses programas inteligentes de recorte são significativamente mais complicados e estão fora do escopo deste tutorial. Felizmente, esses programas podem não ser necessários para editar seus documentos. Ao tirar fotos dos documentos, você provavelmente fará isso uma mesma angulação e altura. A posição relativa do texto em diferentes fotos será similar. Consequentemente, desejará aparar partes semelhantes da imagem de locais relativamente semelhantes na fotografia. Lembre-se: os documentos recortados não precisam ser perfeitos para que o Tesseract funcione. Mas remover anotações marginais ou descolorações irá aumentar a acurácia do OCR. Após alguma experimentação, você perceberá que, para as imagens de entrada fornecidas no Exemplo Um, deseja-se remover 200 _pixels_ da parte superior do documento, 250 _pixels_ da direita, 250 _pixels_ da parte inferior e 800 _pixels_ da esquerda.

O script a seguir permite cortar e enquadrar todos os documentos de uma determinada pasta:

````
#!/bin/bash 
read -p "Informe o nome da pasta: " pasta;

FICHEIROS=/CAMINHO_FICHEIRO/$pasta/*
for f in $FICHEIROS;
do
  convert $f -gravity north -chop 0x200 -gravity east -chop 250x0 -gravity south -chop 0x800 -gravity west -chop 800x0 $f
  convert $f -deskew 80% $f
done 
```` 

O segundo parâmetro também irá enquadrar cada imagem. Isto é, o parâmetro `deskew` irá garantir que o corpo do texto está paralelo com o final da página. Lembre-se de que o parâmetro `chop` removerá a quantidade de pixels especificada independentemente de haver texto neles. Portanto, seja cuidadoso em relação ao conteúdo da pasta usada com este script. O script não só removerá a mesma quantidade do mesmo local em cada imagem, como também irá salvar a edição editada sobre a imagem original. Para evitar sobrescrever o original, altere o segundo nome do ficheiro `$f`. Por exemplo, se os ficheiros estivessem nomeados no formato `IMG_XXXX.JPG`, o segundo `$f` seria substituído por `${f%.*}_EDITED.jpg`. Isso removerá a extensão do nome do ficheiro de cada ficheiro e irá inserir `EDITED.jpg` para distinguir as versões editadas.

Finalmente, podemos escrever outra seção de código para reduzir os ruídos na imagem. Como foi discutido anteriormente, ruídos se referem a variações indesejadas no brilho e na cor da imagem digital. No caso do Exemplo Um, podemos ver um número grande de pontos pretos de tamanhos e formatos variados espalhados por todo o documento. Esse ruído pode ser resultado de problemas com o dispositivo de captura de imagem ou danos ao documento original. O comando `despeckle` do ImageMagick detecta e reduz esses pontos. No entanto, o comando `despeckle` não possui parâmetros. Para reduzir de forma significativa o tamanho dos pontos no Exemplo Um, você terá que executar o comando `despeckle` repetidas vezes no seu documento. Reescrever comandos continuamente seria entendiante, mas, felizmente, podemos escrever um script que repetirá o comando várias vezes.

````
#!/bin/bash
read -p "Informe o nome do ficheiro: " fl;
convert $fl -despeckle -despeckle -despeckle -despeckle -despeckle $fl
````

Esse script pegará o nome do ficheiro fornecido e executará a operação `despeckle` sobre ele cinco vezes. A saída substituirá o ficheiro de entrada original. Assim como antes, tenha certeza de que você está no diretório de trabalho correto, pois o ficheiro especificado deve estar no seu diretório de trabalho.

A figura a seguir ilustra como ficará a aparência do Exemplo Um após o corte, o enquadramento e as repetidas remoções de manchas:

{% include figure.html filename="OCR-e-traducao-automatica-6.png" caption="Figura 6: A versão nova e melhorada do Exemplo Um" %}

Organize seus documentos
---------------------------------
Os scripts também podem auxiliar na organização dos seus documentos. Por exemplo, problemas comuns de trabalho com acervos envolvem gerenciar e organizar as milhares de imagens tiradas durante uma viagem a um acervo. Provavelmente o maior problema é catalogar ficheiros por localização do acervo. Câmeras digitais e smartphones atribuem às fotos um nome de ficheiro semelhante a `IMG_XXXX.JPG`. Esse nome de ficheiro não informa de onde a foto veio nem o seu conteúdo. Em vez disso, você pode querer que cada foto seja rotulada de acordo com o acervo onde foi tirada. Você pode utilizar os metadados de um ficheiro para escrever um script que renomeia ficheiros de acordo com o acervo de onde eles vieram.

O script a seguir irá comparar a data da última modificação de um ficheiro com a data de sua visita ao acervo e renomear o ficheiro a partir disso.

```
#!/bin/bash 
read -p "Informe o nome do acervo: " $nome_acervo;
read -p "Informe a data de visita ao acervo: " $visita;

ls -lt | awk '{if ($6$7==$visita) print $9}' >> list.txt
mkdir $nome_acervo

for i in $(cat list.txt);
do 
  mv $i $nome_acervo/$nome_acervo${i:3}; 
done
```
O script irá renomear todos os ficheiros modificados por último em 30 de agosto com `[NOME_ACERVO_ENTRADA]_XXXX.jpg` .

Conclusão
=========
Nenhum programa ou script único irá revolucionar a sua pesquisa. Por outro lado, aprender a como combinar uma variedade de ferramentas diferentes pode alterar radicalmente o modo como utiliza ficheiros e que tipo de ficheiros você pode utilizar. Essa lição usou a linguagem Bash de script para agrupar ferramentas, mas é possível escolher entre uma variedade de linguagens de programação diferentes para criar seus próprios fluxos de trabalho. Mais importante do que aprender a usar qualquer comando específico é aprender a conduzir sua pesquisa para aproveitar ao máximo as ferramentas digitais.

A [página das lições](https://programminghistorian.org/en/lessons/) do Programming Historian oferece uma boa ideia de quais ferramentas estão disponíveis.

Saber as capacidades e limitações de ferramentas digitais ajudará a conduzir sua pesquisa a aproveitá-las ao máximo.

Mesmo que não esteja interessado em OCR e tradução automática, os scripts ainda são úteis. A habilidade de mover e renomear ficheiros pode ajudar a gerenciar a sua pesquisa. Linhas de comando serão pontos fundamentais de qualquer projeto de humanidades digitais. Esse artigo deu uma introdução à criação de scripts e ao fluxo de trabalho necessário para realmente começar a utilizar as ferramentas de humanidades digitais.
