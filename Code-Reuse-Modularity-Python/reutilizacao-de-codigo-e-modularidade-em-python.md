---
title: Reutilização de código e modularidade em Python
layout: lesson
slug: reutilizacao-de-codigo-e-modularidade-em-python
date: 2012-07-17
translation_date: 2021-05-21
authors:
- William J. Turkel
- Adam Crymble
reviewers:
- Jim Clifford
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
activity:
topics: [python]
abstract: "Programas de computador podem se tornar longos, pesados e confusos sem mecanismos especiais para gerenciar a complexidade. Esta lição mostrará como reutilizar partes do seu código escrevendo *funções* e dividindo seus programas em *módulos*, a fim de mantê-los concisos e fáceis de depurar."
redirect_from:
original: code-reuse-and-modularity
avatar_alt: Three caricature heads
---

{% include toc.html %}

## Objetivos da lição

Programas de computador podem se tornar longos, pesados e confusos sem mecanismos especiais para gerenciar a complexidade. Esta lição mostrará como reutilizar partes do seu código escrevendo funções e dividindo seus programas em módulos, a fim de mantê-los concisos e fáceis de depurar. A possibilidade de remover um único módulo disfuncional pode economizar tempo e esforço.

### Funções

Frequentemente você perceberá que quer reutilizar um determinado conjunto de comandos, geralmente porque há uma tarefa que precisa ser realizada repetidas vezes. Programas são majoritariamente compostos de comandos rotineiros que são poderosos e cujos usos são gerais o suficiente para serem reutilizados. Esses comandos são conhecidos como funções, e o Python possui mecanismos que permitem a definição de novas funções. Vamos trabalhar com um exemplo muito simples de função. Suponha que quer criar uma função de uso geral para cumprimentar pessoas. Copie a definição de função a seguir no Komodo Edit e salve o documento como `cumprimento.py`.

```
# cumprimento.py

def cumprimentar_entidade (x):
    print("Olá " + x)

cumprimentar_entidade("mundo")
cumprimentar_entidade("Programming Historian")
```

A linha que começa com `def` é a declaração da função. Definiremos ("def") uma função, que nesse caso nomeamos "cumprimentar_entidade". O `x` é o parâmetro da função. Seu funcionamento deve ficar claro num instante. A segunda linha contem o código da função. O número de linhas do código varia conforme a nossa necessidade, mas nesse caso é apenas uma linha.

Note que a *indentação* é importante em Python. O espaço vazio antes do comando `print` informa ao interpretador que esse comando é parte da função que está sendo definida. Você aprenderá mais sobre isso à medida que prosseguirmos; por ora, certifique-se de manter a indentação da maneira como foi mostrada. Ao executar o programa, deverá ver algo assim:

```
Olá mundo
Olá Programming Historian
```

Esse exemplo contem uma função: *cumprimentar_entidade*. Depois essa função é "chamada" (ou "invocada") duas vezes. Chamar ou invocar uma função apenas significa que dissemos ao programa para executar o código daquela função. Como dar ao cachorro sua guloseima com sabor de frango (\*au\* \*au\*). Nesse caso, para cada vez que chamamos a função informamos um parâmetro diferente. Tente editar `cumprimento.py` de forma que ele chame a função *cumprimentar_entidade* uma terceira vez utilizando seu próprio nome como parâmetro. Execute o código novamente. Agora deve perceber o que `x` faz na declaração da função.

Antes de prosseguirmos para o próximo passo, edite `cumprimento.py` para deletar os chamados da função, deixando apenas sua declaração. Agora aprenderá como chamar uma função através de outro programa. Quando terminar, seu ficheiro `cumprimento.py` deve estar assim:

```
# cumprimento.py

def cumprimentar_entidade (x):
    print("Olá " + x)
```

## Modularidade

Quando os programas são pequenos como o do exemplo acima, tipicamente ficam hospedados em um único ficheiro. Quando quiser executar um dos seus programas, pode simplesmente enviar o arquivo ao interpretador. À medida que os programas ficam maiores, faz sentido dividí-los em arquivos separados conhecidos como módulos. Essa modularidade torna mais fácil que trabalhe em seções de programas maiores. Aperfeiçoando cada seção do programa antes de unir todas as seções, torna-se mais fácil não apenas reutilizar módulos individuais em outros programas, como também torna mais fácil corrigir eventuais problemas ao ser capaz de identificar a origem do erro. Ao separar um programa em módulos, também se torna possivel ocultar os detalhes de como algo é feito dentro do módulo que o faz. Outros módulos não precisam saber 






