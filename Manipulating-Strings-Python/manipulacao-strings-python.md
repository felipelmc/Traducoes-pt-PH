---
title: Manipulação de strings em Python
layout: lesson
slug: manipulacao-de-strings-em-python
date: 2012-07-17
translation_date: 2021-06-01
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
abstract: "Esta lição é uma breve introdução às técnicas de manipulação de strings em Python."
redirect_from:
original: 
avatar_alt: A man playing a guitar
---

{% include toc.html %}

Objetivos da lição
-----------------------
Essa lição é uma breve introdução às técnicas de manipulação de [strings](https://pt.wikipedia.org/wiki/Cadeia_de_caracteres) em Python. O conhecimento sobre manipulação de strings é crucial na maior parte das tarefas de processamento de texto. Se quiser experimentar as lições a seguir, você pode escrever e executar programas curtos como fizemos nas lições anteriores da série ou pode abrir um Python shell / Terminal para testá-los na linha de comando.

# Manipulando strings Python

Se já tiver tido contato com outras linguagens de programação, deve ter aprendido que é necessário *declarar* ou *digitar* variáveis antes de armazenar qualquer coisa nelas. Isso não é necessário ao trabalhar com strings em Python. Podemos criar uma string simplesmente colocando o conteúdo entre aspas com um sinal de igual (=):

```
mensagem = "Olá Mundo"
```
# Operadores de string: Adicionando e Multiplicando

Uma string é um tipo de objeto que consiste em uma série de caracteres. Python já sabe como lidar com várias representações poderosas e de uso geral, incluindo strings. Uma forma de manipular strings é utilizando *operadores de string*. Esses operadores são representados por símbolos associados à matemática, tais como +, -, \*, / e =. Quando utilizandos com strings, eles executam ações semelhantes, mas não iguais, às suas contrapartes matemáticas.

# Concatenar

Esse termo significa unir strings. O processo é conhecido como *concatenando* strings e é executado utilizando o operador de soma (+). Note que é necessário ser explícito quanto ao local onde deseja que os espaços em branco ocorram, colocando-os também entre aspas simples.

Nesse exemplo, a strings "mensagem1" recebe o conteúdo "olá mundo":

```
mensagem1 = 'olá' + ' ' + 'mundo'
print(mensagem1)
-> olá mundo
```

# Multiplicar

Se quiser multiplas cópias de uma strings, use o operador de multiplicação (\*). Nesse exemplo, a string *mensagem2a* recebe o conteúdo "olá" três vezes; a string *message2b* recebe o conteúdo "mundo"; depois imprimimos (*print*) as duas strings.

```
mensagem2a = 'olá ' * 3
mensagem2b = 'mundo'
print(mensagem2a + mensagem2b)
-> olá olá olá mundo
```

# Append

E se quiser adicional material ao final de uma string sucessivamente? Há um operador especial para isso (+=).

```
mensagem3 = 'oi'
mensagem3 += ' '
mensagem3 += 'mundo'
-> oi mundo
```

# Métodos de string: Encontrando, Modificando

Além dos operadores, Python vem pré-instalado com dezenas de métodos de string que permitem fazer coisas com strings. Utilizandos sozinhos ou combinados, esses métodos podem fazer com strings qualquer coisa que você imaginar. A boa notícia é que é possível consultar uma lista de Métodos de String no [site do Python](https://docs.python.org/2/library/stdtypes.html#string-methods), incluindo informações sobre como usar cada um corretamente. Para garantir que você tenha uma compreensão básica dos métodos de string, o que se segue é uma breve visão geral de alguns dos mais comumente usados.


