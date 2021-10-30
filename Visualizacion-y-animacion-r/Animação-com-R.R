# install.packages("tidyverse")

library(readxl)
library(tidyverse)

at59 <- read_excel("atentados1959.xlsx")

head(at59)

at59$objeto <- ifelse(at59$objeto == "bomba", "explosivo", at59$objeto)

at59$objeto <- ifelse(at59$objeto == "explosivo", "bomba", at59$objeto)

at59 <- tibble(map_df(at59[,c("fecha")], as.Date), map_df(at59[,c("ciudad", "objeto", "sitio","objetivo")], factor))

at59 <- arrange(at59, fecha)

head(at59)

table(at59$ciudad)

barplot(table(at59$ciudad))

table(at59$ciudad, at59$objeto)

# install.packages("kableExtra")
library(kableExtra)

at59k <- kable(table(at59$ciudad, at59$objeto), caption = "Objeto vinculado ao atentado por cidade")

kable_styling(at59k, font_size = 10)

# install.packages("htmltools")
library(htmltools)

ggplot(at59, aes(x = ciudad, y = objeto)) +
  geom_point()

ggplot(at59, aes(x = ciudad, y = objeto)) +
  geom_count() +
  labs(title = "Atentados durante 1959", subtitle = "Objeto utilizado por cidade", x = "CIDADE", y = "OBJETO") +
  theme_bw()

ggsave("nome-do-ficheiro.png")

ggplot(at59, aes(x = ciudad, y = objeto)) +
  geom_jitter(colour = as.numeric(at59$ciudad), size = 3) +
  labs(title = "Atentados durante 1959", subtitle = "Objeto utilizado por cidade", x = "CIDADE", y = "OBJETO") +
  theme_bw()

# install.packages("gganimate")
# install.packages("gifski")
library(gganimate)
library(gifski)

# não recomendo ficar rodando esse código pq ele fica criando todas as frames da
# animação em imagens diferentes (no caso, 100). É bem chatinho depois pra 
# organizar o diretório. Inclusive comentei o código pra eu poder fazer os meus 
# testes

#ggplot(at59, aes(x = ciudad, y = objeto)) +
  #geom_jitter(colour = as.numeric(at59$ciudad), size = 4) +
  #labs(title = "Atentados durante 1959", subtitle = "Objeto utilizado según ciudad - Fecha: {frame_time}", x = "CIUDAD", y = "OBJETO") +
  #theme_bw() +
  #transition_time(fecha) +
  #shadow_mark(past = TRUE)

# aqui segue normal como o autor fez: ele cria um objeto justamente pra salvar o 
# gráfico do código de cima
atentados <- ggplot(at59, aes(x = ciudad, y = objeto)) +
  geom_jitter(colour = as.numeric(at59$ciudad), size = 4) +
  labs(title = "Atentados durante 1959", subtitle = "Objeto utilizado por cidade - Data: {frame_time}", x = "CIDADE", y = "OBJETO") +
  theme_bw() +
  transition_time(fecha) + 
  shadow_mark(past = TRUE)


# adicionando renderer=gifski_render() a animação funcinou, mas não sei te 
# explicar o motivo. Achei no StackOverflow: 
# https://stackoverflow.com/questions/59592030/error-the-animation-object-does-not-specify-a-save-animation-method
animate(atentados, fps = 5, end_pause = 15, renderer = gifski_renderer())

# daí por fim ele salva normalmente
anim_save("nome-do-ficheiro.gif")

# Antes ele não conseguindo gerar pq, de fato, não tinha nenhum gif para ele se 
# basear, e aí dava um erro. Aliás, um problema dessa lição é apresentar a 
# função de salvar o gif (essa aí embaixo) antes de o gif ser gerado. Não sei 
# se é uma questão de atualização de pacote (ou seja, se antes precisava de 
# menos para gerar um gif), mas enfim... Sei que agora tá funcionando!

