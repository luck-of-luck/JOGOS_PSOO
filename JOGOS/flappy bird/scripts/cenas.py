import pygame
from scripts.cano import Cano
from scripts.jogador import Jogador
from scripts.interfaces import Texto    # importando texto
from scripts.interfaces import Botao    # importando botão

class Partida:
    def __init__(self, tela):
        self.tela = tela
        self.jogador = Jogador(tela, 100, 100)
        self.cano = Cano(tela)
        self.estado = 'partida'                 # estado atual da partida, indicando se está no jogo ou se perdeu

        self.pontosValor = 0                    # valor dos pontos
        self.contador = 0                       # o contador que subirá os pontos
        self.pontosTexto = Texto(tela, str(self.pontosValor), 260, 20, (255, 255, 255), 30)  # texto dos pontos

    def atualizar(self):
        self.estado = 'partida'                 # redefinimos todo o estado para "partida" a cada atualização
        self.jogador.atualizar()
        self.cano.atualizar()
        # contador de pontos
        self.contador += 1
        if self.contador > 60:
            self.pontosValor += 1
            self.contador = 0
            self.pontosTexto.atualizarTexto(str(self.pontosValor))
        # desenhando os pontos
        self.pontosTexto.desenhar()

        if self.cano.detectarColisao(self.jogador.getRect()):  # detectamos a colisao com o jogador pegando o Rect pela função criada anteriormente
            self.estado = 'menu'                # muda a partida para o menu
            self.jogador.posicao = (100, 100)   # reinicia a posicao do jogador
            self.cano.x = self.tela.get_width() # reinicia a posicao do cano
            self.pontosValor = 0                # zerando os pontos

        self.jogador.desenhar()
        self.cano.desenhar()
        return self.estado

class Menu:
    def __init__(self, tela):
        self.tela = tela
        self.titulo = Texto(tela, "FlappyBird", 200, 80, (255, 255, 255), 60)
        self.estado = "menu"                    # estado atual da partida, indicando se está no jogo ou se perdeu
        # instanciando o botão
        self.botao_jogar = Botao(tela, "Jogar", 250, 200, 40, (200, 0, 0), (255, 255, 255))

    def atualizar(self):
        self.estado = "menu"                    # redefinimos todo o estado para "menu" a cada atualização
        self.titulo.desenhar()
        self.botao_jogar.desenhar()             # desenhando botão
        if self.botao_jogar.get_click():        # verifica o click
            self.estado = 'partida'             # muda o estado para partida
        return self.estado
