import os
import pygame

# caminho da pasta assets, calculado a partir da pasta deste arquivo,
# assim o jogo funciona rodando de qualquer diretorio
CAMINHO_ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets')

class Carro:
    def __init__(self, tela, x, y):
        self.posicao = [x, y]
        self.tamanho = [40, 60]                     # tamanho do carro (imagem ampliada)
        self.imagem = pygame.image.load(os.path.join(CAMINHO_ASSETS, 'carro.png'))  # carrega a imagem do carro
        self.imagem = pygame.transform.scale(self.imagem, self.tamanho)  # amplia a imagem para o tamanho desejado
        self.tela = tela
        self.velocidade = 6                         # velocidade de movimento do carro

    def desenhar(self):
        self.tela.blit(self.imagem, self.posicao)

    def atualizar(self):
        teclas = pygame.key.get_pressed()           # pega todas as teclas pressionadas
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            self.posicao[0] -= self.velocidade      # move para a esquerda
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
            self.posicao[0] += self.velocidade      # move para a direita
        # impede que o carro saia da tela
        if self.posicao[0] < 0:
            self.posicao[0] = 0
        if self.posicao[0] + self.tamanho[0] > self.tela.get_width():
            self.posicao[0] = self.tela.get_width() - self.tamanho[0]

    def getRect(self):
        return pygame.Rect(self.posicao, self.tamanho)  # retorna a rect do carro para fins de colisão
