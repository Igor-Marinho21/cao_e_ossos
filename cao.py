# Pessoa 1: dados iniciais do cão.

import pygame

from configuracoes import (
    CAMINHO_IMAGEM_CAO,
    POSICAO_INICIAL_CAO,
    TAMANHO_CAO,
    VELOCIDADE_CAO,
)


class Cao:
    def __init__(self):
        self.caminho_imagem = CAMINHO_IMAGEM_CAO
        self.tamanho = TAMANHO_CAO
        self.imagem = pygame.image.load(str(self.caminho_imagem))
        self.imagem = pygame.transform.scale(self.imagem, self.tamanho)

        # Posição pelo canto superior esquerdo, em pixels.
        self.posicao = pygame.Vector2(POSICAO_INICIAL_CAO)
        self.rect = self.imagem.get_rect(topleft=self.posicao)
        self.velocidade = VELOCIDADE_CAO

        # Componentes de direção: -1, 0 ou 1. Começam sem movimento.
        self.direcao_x = 0
        self.direcao_y = 0

    def desenhar(self, tela):
        tela.blit(self.imagem, self.rect)
