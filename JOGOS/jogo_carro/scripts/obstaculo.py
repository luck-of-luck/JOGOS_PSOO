import os
import pygame
import random  # importamos a função que gera números aleatórios

# caminho da pasta assets, calculado a partir da pasta deste arquivo,
# assim o jogo funciona rodando de qualquer diretorio
CAMINHO_ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets')

class Obstaculo:
    def __init__(self, tela):
        self.imagem = pygame.image.load(os.path.join(CAMINHO_ASSETS, 'cone.png'))  # carrega a imagem do obstáculo
        self.tamanho = [40, 40]                     # tamanho do obstáculo
        self.imagem = pygame.transform.scale(self.imagem, self.tamanho)
        self.tela = tela
        self.x = random.randint(0, tela.get_width() - self.tamanho[0])  # posicao x aleatoria
        self.y = -self.tamanho[1]                   # começa acima da tela
        self.velocidade = 3                         # velocidade em que cai

    def atualizar(self):
        self.y += self.velocidade                   # aplica a velocidade na posicao (caindo)
        if self.y > self.tela.get_height():         # se saiu da tela, reinicia no topo em posicao aleatoria
            self.x = random.randint(0, self.tela.get_width() - self.tamanho[0])
            self.y = -self.tamanho[1]

    def desenhar(self):
        self.tela.blit(self.imagem, (self.x, self.y))

    def detectarColisao(self, rectCarro):
        rect = pygame.Rect((self.x, self.y), self.imagem.get_size())  # rect do obstáculo
        if rectCarro.colliderect(rect):             # verifica colisão usando colliderect
            return True
        return False
