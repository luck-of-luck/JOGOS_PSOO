import os
import pygame

# caminho da pasta assets, calculado a partir da pasta deste arquivo,
# assim o jogo funciona rodando de qualquer diretorio
CAMINHO_ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets')

class Jogador:  # cria uma classe jogador
    # def indica uma função, e __init__ é uma palavra reservada que sempre é chamada
    # quando usamos a classe. self tambem é reservado e indica que cada objeto criado tera
    # informações próprias, e x e y são variáveis que receberão a posição onde é criado o
    # jogador e tela é a tela em que desenhamos nosso jogador
    def __init__(self, tela, x, y):
        self.posicao = [x, y]                       # a posicao do jogador é o x e y que usamos ao criar a classe
        self.tamanho = [32, 32]                     # cria uma variavel que indica o tamanho do jogador
        self.rect = pygame.Rect(self.posicao, self.tamanho)  # rect é uma classe do pygame amplamente utilizada para detectar colisão
        self.contador = 0                           # cria uma variavel para contar quantas atualizações são necessarias antes de mudar de imagem
        self.imagemAtual = 0                        # variavel que indica qual a imagem atual
        self.tela = tela                            # define a tela da classe jogador como a tela que passamos

        # cria uma lista vazia que receberá as imagens do jogador
        self.listaImagens = []
        for i in range(3):                          # laço que vai pegar as 3 imagens do jogador e adicionar na lista
            imagem = pygame.image.load(os.path.join(CAMINHO_ASSETS, f'passaro-{i}.png'))  # a função load serve para pegar as imagens e guardar na variavel imagem
            imagem = pygame.transform.scale(imagem, self.tamanho)  # a função scale muda a imagem para o tamanho especificado
            self.listaImagens.append(imagem)        # por fim usamos a função append para inserir a imagem na lista de imagens

        # cria variaveis para gerenciar a velocidade, 1/60 serve para calcular em segundos
        self.velocidadeAtual = 0
        self.gravidade = 1/60 * 10
        self.velocidadeMaxima = 1/60 * 100

    def desenhar(self):                             # cria uma função que desenha o jogador
        self.contador += 1                          # soma 1 no contador
        if self.contador > 5:                       # verifica se o contador é maior que 5
            self.contador = 0                       # caso seja maior que 5, define como zero
            self.imagemAtual = (self.imagemAtual + 1) % 3  # adiciona 1 na variavel imagemAtual e pega o resto da divisão por 3, que pode ser 0, 1 ou 2
        self.tela.blit(self.listaImagens[self.imagemAtual], self.posicao)  # usa a função blit para desenhar a imagem na tela

    def atualizar(self):
        # adiciona a velocidade atual, limitada pela velocidadade máxima
        self.velocidadeAtual = min(self.velocidadeAtual + self.gravidade, self.velocidadeMaxima)
        self.posicao = [self.posicao[0], self.posicao[1] + self.velocidadeAtual]  # adiciona a velocidade atual ao Y
        self.rect = pygame.Rect(self.posicao, self.tamanho)  # atualiza a rect para a nova posicao do jogador
        self.teclas = pygame.key.get_pressed()      # pega todas as teclas pressionadas
        if self.teclas[pygame.K_SPACE]:             # verifica se a tecla espaço foi pressionada
            self.velocidadeAtual = -self.velocidadeMaxima * 2  # define a velocidade como negativa e multiplica por 2, fazendo o jogador subir

    def getRect(self):
        return pygame.Rect(self.posicao, self.tamanho)  # retorna a rect do jogador para fins de colisão
