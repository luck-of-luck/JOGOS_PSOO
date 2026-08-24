import pygame
from scripts.carro import Carro
from scripts.obstaculo import Obstaculo
from scripts.interfaces import Texto    # importando texto
from scripts.interfaces import Botao    # importando botão

class Partida:
    def __init__(self, tela):
        self.tela = tela
        self.carro = Carro(tela, 260, 360)          # cria o carro do jogador
        self.obstaculo = Obstaculo(tela)            # cria o obstáculo
        self.estado = 'partida'                     # estado atual da partida

        self.pontosValor = 0                        # valor dos pontos
        self.contador = 0                           # o contador que subirá os pontos
        self.pontosTexto = Texto(tela, str(self.pontosValor), 260, 20, (255, 255, 255), 30)  # texto dos pontos

    def atualizar(self):
        self.estado = 'partida'                     # redefinimos o estado para "partida" a cada atualização
        self.carro.atualizar()
        self.obstaculo.atualizar()

        # contador de pontos
        self.contador += 1
        if self.contador > 30:
            self.pontosValor += 1
            self.contador = 0
            self.pontosTexto.atualizarTexto(str(self.pontosValor))
        # desenhando os pontos
        self.pontosTexto.desenhar()

        if self.obstaculo.detectarColisao(self.carro.getRect()):  # detectamos a colisao do carro com o obstáculo
            self.estado = 'menu'                    # muda a partida para o menu
            self.pontosValor = 0                    # zerando os pontos

        self.obstaculo.desenhar()
        self.carro.desenhar()
        return self.estado

class Menu:
    def __init__(self, tela):
        self.tela = tela
        self.titulo = Texto(tela, "Jogo do Carro", 180, 120, (255, 255, 255), 60)
        self.instrucao = Texto(tela, "Desvie dos cones!", 190, 200, (255, 255, 255), 30)
        self.estado = "menu"                        # estado atual da partida
        # instanciando o botão
        self.botao_jogar = Botao(tela, "Jogar", 250, 300, 40, (0, 150, 0), (255, 255, 255))

    def atualizar(self):
        self.estado = "menu"                        # redefinimos o estado para "menu" a cada atualização
        self.titulo.desenhar()
        self.instrucao.desenhar()
        self.botao_jogar.desenhar()                 # desenhando botão
        if self.botao_jogar.get_click():            # verifica o click
            self.estado = 'partida'                 # muda o estado para partida
        return self.estado
