#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 16:56:08 2021

@author: Felipe Marques Esteves Lamarca

Script teste dos códigos da tradução para o português da lição 
"Manipulating Strings in Python" do The Programming Historian.

"""
# -------------------------------------
mensagem = "Olá Mundo"


# -------------------------------------
mensagem1 = 'olá' + ' ' + 'mundo'
print(mensagem1)


# -------------------------------------
mensagem2a = 'olá ' * 3
mensagem2b = 'mundo'
print(mensagem2a + mensagem2b)


# -------------------------------------
mensagem3 = 'oi'
mensagem3 += ' '
mensagem3 += 'mundo'
print(mensagem3)


# -------------------------------------
mensagem4 = 'olá' + ' ' + 'mundo'
print(len(mensagem4))


# -------------------------------------
mensagem5 = "olá mundo"
mensagem5a = mensagem5.find("mun")
print(mensagem5a)


# -------------------------------------
mensagem6 = "olá mundo"
mensagem6b = mensagem6.find("esquilo")
print(mensagem6b)


# -------------------------------------
mensagem7 = "OLÁ MUNDO"
mensagem7a = mensagem7.lower()
print(mensagem7a)


# -------------------------------------
mensagem8 = "OLÁ MUNDO"
mensagem8a = mensagem8.replace("O", "pizza")
print(mensagem8a)


# -------------------------------------
mensagem9 = "Olá Mundo"
mensagem9a = mensagem9[1:7]
print(mensagem9a)


# -------------------------------------
loc_inicial = 2
loc_final = 7
mensagem9b = mensagem9[loc_inicial:loc_final]
print(mensagem9b)


# -------------------------------------
mensagem9 = "Olá Mundo"
print(mensagem9[:5].find("d"))


# -------------------------------------
print(len(mensagem7))


# -------------------------------------
mensagem7 = "OLÁ MUNDO"
mensagem7a = mensagem7.lower()
print(mensagem7a)


# -------------------------------------
print('\"')


# -------------------------------------
print('O programa imprimiu \"olá mundo\"')


# -------------------------------------
print('olá\tolá\tolá\nmundo')