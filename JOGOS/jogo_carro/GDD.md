# GDD — Game Design Document (Documento de Design de Jogo)

## Jogo do Carro ❄️

> Exercício final do Estudo Dirigido de Desenvolvimento de Jogos com Pygame.

---

## 1. Visão Geral

**Nome:** Jogo do Carro

**Gênero:** Arcade / Reflexo

**Plataforma:** PC (Windows) — feito com Python e Pygame

**Público-alvo:** Iniciantes em programação de jogos e jogadores casuais.

**Descrição:** O jogador controla um carro que se move para a esquerda e para a
direita, no sentido vertical da pista, com o objetivo de **desviar dos cones**
(obstáculos) que caem do topo da tela. Quanto mais tempo sobreviver, mais pontos
acumula.

---

## 2. Mecânicas

### 2.1 Controles
| Tecla            | Ação                     |
|------------------|--------------------------|
| `←` (ou `A`)     | Mover o carro para a esquerda |
| `→` (ou `D`)     | Mover o carro para a direita  |
| Clique do mouse  | Apertar os botões do menu     |

### 2.2 Regras
1. O carro fica na parte inferior da tela e se move apenas no eixo X.
2. Cones surgem no topo em posições aleatórias e caem em direção ao carro.
3. Se o carro colidir com um cone, a partida termina e volta ao menu.
4. A pontuação aumenta conforme o tempo de sobrevivência.

### 2.3 Condições de vitória / derrota
- **Derrota:** colisão com qualquer cone.
- **Vitória:** não há fim — é um jogo de pontuação (high score), quanto mais
  tempo sobreviver, melhor.

---

## 3. Fluxo de Telas (Cenas)

1. **Menu:** mostra o título, uma instrução e o botão **Jogar**.
2. **Partida:** mostra o carro, os cones caindo e a pontuação.
3. **Fim de partida:** ao colidir, retorna automaticamente ao menu (pontuação zerada).

---

## 4. Arte e Som

- **Arte:** sprites simples fornecidos na pasta *assets exercício final*
  (`carro.png` e `cone.png`).
- **Som:** o jogo pode ser ampliado com efeitos sonoros de colisão e música de
  fundo (não implementado nesta versão).

---

## 5. Tecnologias

- **Linguagem:** Python 3
- **Biblioteca gráfica:** Pygame
- **Estrutura de código:** separada em módulos (classes) para organização:
  - `main.py` — gerencia a janela e o laço principal
  - `scripts/cenas.py` — cenas `Menu` e `Partida`
  - `scripts/carro.py` — classe do jogador
  - `scripts/obstaculo.py` — classe dos obstáculos
  - `scripts/interfaces.py` — classes `Texto` e `Botao`

---

## 6. Ideias futuras (Room for Improvement)

- Adicionar mais de um cone caindo ao mesmo tempo.
- Aumentar a velocidade dos cones conforme a pontuação sobe.
- Incluir efeitos sonoros e música.
- Sistema de recorde (high score) salvo em arquivo.
- Uma tele (game over) com o botão de "Jogar novamente".

---

*Como fazer um GDD:* <https://www.gamedeveloper.com/business/how-to-write-a-game-design-document>
