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
        # cria uma imagem com o texto e a cor que passamos, False serve para o pygame deixar
        # as bordas mais suaves, porém nao utilizaremos esse recurso
        self.imagemTexto = self.fonte.render(self.texto, False, self.cor)

    def desenhar(self):
        # funcao que exibe o texto na tela, note que é o mesmo comando que desenha o cano e o jogador
        self.tela.blit(self.imagemTexto, self.posicao)

    def atualizarTexto(self, novoTexto):            # funcao para atualizar o texto
        self.imagemTexto = self.fonte.render(novoTexto, False, self.cor)  # atualiza a imagem com o novo texto

class Botao:
    def __init__(self, tela, texto, x, y, tamanho, corFundo, corTexto):
        self.tela = tela
        self.texto = Texto(tela, texto, x, y, corTexto, tamanho)
        self.posicao = (x, y)
        self.corFundo = corFundo

    def desenhar(self):
        # o desenhar do botao, consiste em fazer duas partes, o fundo e o texto
        # o fundo precisa ter um tamanho e posicao, vamos usar o pygame.Rect para criar isso
        rect = pygame.Rect(self.posicao, self.texto.imagemTexto.get_size())  # o rect usa a posicao que passamos no __init__
        # para o fundo vamos usar draw.rect, que desenha um simples retangulo na tela
        pygame.draw.rect(self.tela, self.corFundo, rect)
        # para o texto vamos usar o metodo desenhar da classe Texto, que já desenha o texto na tela
        self.texto.desenhar()

    def get_click(self):                            # funcao para saber se o botao teve um clique
        # para isso vamos usar o metodo collidepoint do Rect que verifica se um determinado ponto esta dentro do retangulo
        posicaoMouse = pygame.mouse.get_pos()       # primeiro vamos pegar a posicao do mouse
        rect = pygame.Rect(self.posicao, self.texto.imagemTexto.get_size())  # depois vamos pegar o rect do botao
        # e por fim vamos verificar se o mouse esta dentro do rect do botao e foi pressionado com o metodo mouse.get_pressed()
        if rect.collidepoint(posicaoMouse) and pygame.mouse.get_pressed()[0]:  # [0] indica qual botao do mouse, da esquerda pra direita
            return True
        else:
            return False
