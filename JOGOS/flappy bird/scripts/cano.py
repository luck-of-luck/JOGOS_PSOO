import os
import pygame
import random  # importamos a função que gera números aleatórios

# caminho da pasta assets, calculado a partir da pasta deste arquivo,
# assim o jogo funciona rodando de qualquer diretorio
CAMINHO_ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets')

class Cano:
    def __init__(self, tela):
        self.imagem = pygame.image.load(os.path.join(CAMINHO_ASSETS, 'cano.png'))  # carregamos a imagem
        self.tela = tela                            # definimos a tela
        self.altura_base = random.randint(100, 300)  # geramos um número aleatório para a altura da base do cano
        self.x = self.tela.get_width()              # define a posicao x como a largura da tela, ou seja no lado direito
        self.distancia = 50                         # define a distancia entre o cano e a altura base
        # definimos a altura do cano de cima, como a altura base, menos a altura da imagem,
        # menos a distancia, que faz o cano ficar pra cima
        self.cano_cima = self.altura_base - self.imagem.get_height() - self.distancia
        # definimos a altura do cano de baixo como a altura base mais a distancia, que faz o cano ficar pra baixo
        self.cano_baixo = self.altura_base + self.distancia
        self.velocidade = 2                         # velocidade em que o cano se move para esquerda

    def atualizar(self):
        self.x -= self.velocidade                   # aplica velocidade na posicao
        if self.x < -self.imagem.get_width():       # verifica se a imagem toda saiu da tela
            self.x = self.tela.get_width()          # volta para a direita
            self.altura_base = random.randint(100, 300)  # usa a funcao randint para criar uma nova altura base aleatoria
            self.cano_cima = self.altura_base - self.imagem.get_height() - self.distancia
            self.cano_baixo = self.altura_base + self.distancia  # atualiza a posicao de ambos os canos

    def desenhar(self):
        imagem_invertida = pygame.transform.flip(self.imagem, False, True)  # faz o cano ficar invertido verticalmente
        self.tela.blit(imagem_invertida, (self.x, self.cano_cima))          # desenha o cano invertido na tela
        self.tela.blit(self.imagem, (self.x, self.cano_baixo))              # desenha o cano normal na tela

    def detectarColisao(self, rectJogador):
        # cria 2 Rects de colisao para cada cano, passando o x, a posicao y de cada e o tamanho da imagem
        rectCanoCima = pygame.Rect((self.x, self.cano_cima), self.imagem.get_size())
        rectCanoBaixo = pygame.Rect((self.x, self.cano_baixo), self.imagem.get_size())
        # para verificar colisao entre 2 rects usamos colliderect
        if rectJogador.colliderect(rectCanoCima) or rectJogador.colliderect(rectCanoBaixo):
            return True  # colliderect entre jogador e os canos
        return False
