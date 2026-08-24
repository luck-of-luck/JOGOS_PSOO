import os, sys

# Muda o diretório de trabalho para a raiz do projeto Flappy Bird (pasta onde este teste está)
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.environ['SDL_VIDEODRIVER'] = 'dummy'

import pygame
pygame.init()
tela = pygame.display.set_mode([600, 400])

from scripts.cenas import Partida, Menu
from scripts.jogador import Jogador
from scripts.cano import Cano
from scripts.interfaces import Texto, Botao

# Testa a partida do Flappy Bird (simula várias atualizações)
p = Partida(tela)
for _ in range(1200):
    estado = p.atualizar()
assert estado in ('partida', 'menu')
print('[OK] Flappy Bird - Partida atualizou 1200x, estado =', estado)

# Testa o menu
m = Menu(tela)
for _ in range(30):
    m.atualizar()
print('[OK] Flappy Bird - Menu atualizou sem erros')

# Testa classes unitárias
j = Jogador(tela, 100, 100)
for _ in range(200):
    j.atualizar()
    j.desenhar()
c = Cano(tela)
c.desenhar()
t = Texto(tela, 'T', 0, 0, (255, 255, 255), 20)
t.desenhar()
b = Botao(tela, 'B', 0, 0, 20, (255, 0, 0), (255, 255, 255))
b.desenhar()
print('[OK] Flappy Bird - Jogador, Cano, Texto e Botao OK')
pygame.quit()
print('FLAPPY BIRD TESTE PASSED')
