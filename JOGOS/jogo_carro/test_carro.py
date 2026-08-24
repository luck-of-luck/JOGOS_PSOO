import os, sys

# Muda o diretório de trabalho para a raiz do jogo do carro (pasta onde este teste está)
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.environ['SDL_VIDEODRIVER'] = 'dummy'

import pygame
pygame.init()
tela = pygame.display.set_mode([600, 500])

from scripts.cenas import Partida, Menu
from scripts.carro import Carro
from scripts.obstaculo import Obstaculo
from scripts.interfaces import Texto, Botao

# Testa a partida do jogo do carro
p = Partida(tela)
for _ in range(1200):
    estado = p.atualizar()
assert estado in ('partida', 'menu')
print('[OK] Jogo do Carro - Partida atualizou 1200x, estado =', estado)

# Testa o menu
m = Menu(tela)
for _ in range(30):
    m.atualizar()
print('[OK] Jogo do Carro - Menu atualizou sem erros')

# Testa classes
car = Carro(tela, 260, 360)
for _ in range(100):
    car.atualizar()
    car.desenhar()
ob = Obstaculo(tela)
for _ in range(200):
    ob.atualizar()
    ob.desenhar()
print('[OK] Jogo do Carro - Carro e Obstaculo OK')
pygame.quit()
print('JOGO DO CARRO TESTE PASSED')
