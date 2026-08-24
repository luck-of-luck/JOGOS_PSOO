import pygame

class Texto:
    def __init__(self, tela, texto, x, y, cor, tamanho):
        self.tela = tela
        self.texto = texto
        self.posicao = (x, y)
        self.cor = cor
        self.tamanho = tamanho
        pygame.font.init()                          # inicia o sistema de Fontes
        self.fonte = pygame.font.Font(None, self.tamanho)  # cria uma fonte para utilizarmos
        self.imagemTexto = self.fonte.render(self.texto, False, self.cor)  # cria uma imagem com o texto e a cor

    def desenhar(self):
        self.tela.blit(self.imagemTexto, self.posicao)

    def atualizarTexto(self, novoTexto):
        self.imagemTexto = self.fonte.render(novoTexto, False, self.cor)

class Botao:
    def __init__(self, tela, texto, x, y, tamanho, corFundo, corTexto):
        self.tela = tela
        self.texto = Texto(tela, texto, x, y, corTexto, tamanho)
        self.posicao = (x, y)
        self.corFundo = corFundo

    def desenhar(self):
        rect = pygame.Rect(self.posicao, self.texto.imagemTexto.get_size())
        pygame.draw.rect(self.tela, self.corFundo, rect)
        self.texto.desenhar()

    def get_click(self):
        posicaoMouse = pygame.mouse.get_pos()
        rect = pygame.Rect(self.posicao, self.texto.imagemTexto.get_size())
        if rect.collidepoint(posicaoMouse) and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False
