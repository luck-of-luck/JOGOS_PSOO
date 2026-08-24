import pygame
from scripts.cenas import Partida
from scripts.cenas import Menu

pygame.init()

tamanhoTela = [600, 500]                            # define o tamanho da janela do jogo
tela = pygame.display.set_mode(tamanhoTela)         # cria a janela que utilizaremos
pygame.display.set_caption("Jogo do Carro")         # define o titulo da janela

relogio = pygame.time.Clock()                       # cria um relogio para controlar a velocidade do jogo
corFundo = (60, 60, 60)                             # cria uma cor de fundo (asfalto) em formato RGB

# criamos um dicionario que associa uma 'cena' (indicada por uma string) com a sua classe
listaCenas = {
    'partida': Partida(tela),
    'menu': Menu(tela)
}

cenaAtual = 'menu'                                  # criamos uma variavel para indicar a cena atual

while True:                                         # cria um laço infinito para manter o jogo aberto
    for e in pygame.event.get():                    # laço que passa em cada evento do pygame
        if e.type == pygame.QUIT:                   # verifica se é do tipo sair (quando fechamos a tela)
            pygame.quit()                           # finaliza o pygame
            exit()                                  # encerra o programa

    tela.fill(corFundo)                             # pinta a tela de fundo

    # chama o dicionario de cenas, escolhe a 'cenaAtual' e chama a função atualizar da cena
    cenaAtual = listaCenas[cenaAtual].atualizar()

    relogio.tick(60)                                # controla a tela para atualizar 60 vezes por segundo
    pygame.display.flip()                           # atualiza a tela, mostrando as figuras
