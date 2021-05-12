Relatório da lição "OCR and Machine Translation"
=================
1. Considerei inviável alterar os ficheiros utilizados pelo autor por outros em Língua Portuguesa. A utilização da API de tradução Yandex e a maior parte dos comandos utilizados na lição foram justificadas pela língua e pelo formato dos ficheiros escolhidos. Desse modo, alterar os ficheiros implicaria encontrar outros que fossem semelhantes aos originais em forma, além da provável necessidade de troca de API. Na prática, a lição sofreria muitas alterações e perderia sua identidade original;

2. A API de tradução utilizada pelo autor (_Yandex_) parece não estar funcionando bem, pelo menos no meu computador. Ao tentar fazer a tradução através dessa API, recebo como _output_ uma série de erros do tipo "Session is invalid", "Null response" ou "Oops! Something went wrong and I can't translate it for you :(". Acredito que não seja um problema do meu código, já que a alteração da API para Bing ou Google fez com que o processo automatizado de tradução transcorresse normalmente. Bastou a seguinte alteração no código:

    `trans -e google :eng file://INPUT_FILENAME > OUTPUT_FILENAME`

	Ou ainda
	
	`trans -e bing :eng file://INPUT_FILENAME > OUTPUT_FILENAME`

3. A princípio mantive a API _Yandex_ na tradução por dois motivos. Primeiro, para que o código original possa ser testado em outro computador, de modo a verificar se a API de fato está com problemas. Segundo, porque a mudança de API tornaria necessárias uma série de modificações no corpo da lição. Isso porque o autor da lição tenta consertar, no decorrer do texto, alguns erros de tradução típicos do Yandex, mas que não aparecem quando outras APIs são utilizadas. Por exemplo, o autor tenta modificar uma tradução incorreta (_COB._, do russo, havia sido traduzido para _owls_) no decorrer da lição. Mas esse mesmo erro de tradução não aparece quando utilizamos o Google ou Bing;

4. Algumas linhas de código pareceram não modificar em nada o documento. Mais especificamente o arquivo Nano a seguir:
```
#!/bin/bash
read -p "enter file name: " fl;
convert $fl -despeckle -despeckle -despeckle -despeckle -despeckle $fl
```
Ao rodar esse ficheiro Nano criado, não parece ter havido qualquer alteração no documento. 

Também não consegui fazer funcionar os códigos que movem os arquivos transcritos/traduzidos/editados para pastas diferentes. Melhor dizendo: os comandos não me retornaram erros, mas não fizeram o que supostamente deveriam ter feito. São eles:

   ```
mkdir $folder"_ocr"
mkdir $folder"_translation"
mv *_ocr.txt *_ocr
mv *_trans.txt *_translation
```

E também

 ```
#!/bin/bash 
read -p "enter archive name: " $archive_name;
read -p "enter  date of visit: " $visit;

ls -lt | awk '{if ($6$7==$visit) print $9}' >> list.txt
mkdir $archive_name

for i in $(cat list.txt);
do 
  mv $i $archive_name/$archive_name${i:3}; 
done
```

OBS.: Nos markdown com a lição traduzida, as variáveis, frases e os nomes de arquivos de _input_/_output_ foram traduzidos sem perda aparente de funcionalidade (considerando os casos que consegui testar).

Reforço que todos os pontos relatados acima podem ser decorrentes de problemas no meu próprio computador. Não está descartada a possibilidade de os códigos funcionarem normalmente se executados em outra máquina ou outro sistema operacional. Daí a manutenção, pelo menos em um primeiro momento, dos códigos e do conteúdo relativos à tradução. 

5. A palavra "archive", quando utilizada no sentido de um local em que são guardados os ficheiros e disponibilizados ao público, foi traduzida como "acervo";

6. _Input_ e _Output_ foram traduzidos para **Entrada** e **Saída**. Quando considerado conveniente, **Saída** foi substituído por **Resultado** ou variações; 

7. Sempre que possível, as linhas de código foram traduzidas, especialmente no caso dos nomes de variáveis ou nomes de arquivos. `INPUT_FILENAME` e `OUTPUT_FILENAME`, por exemplo, foram traduzidas para `NOME_FICHEIRO_ENTRADA` e `NOME_FICHEIRO_SAÍDA`, respectivamente. `folder` foi traduzido para `pasta`. `FILES` foi traduzido para `FICHEIROS`.

#### Felipe Marques Esteves Lamarca
