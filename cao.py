# Pessoa 1: dados iniciais do cão.

from configuracoes import (
    CAMINHO_IMAGEM_CAO,
    POSICAO_INICIAL_CAO,
    TAMANHO_CAO,
    VELOCIDADE_CAO,
)

caminho_imagem = CAMINHO_IMAGEM_CAO
imagem = None
rect = None

# Posição pelo canto superior esquerdo, em pixels.
posicao = POSICAO_INICIAL_CAO
tamanho = TAMANHO_CAO
velocidade = VELOCIDADE_CAO

# Componentes de direção: -1, 0 ou 1. Começam sem movimento.
direcao_x = 0
direcao_y = 0
