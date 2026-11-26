# Pessoa 1: dados iniciais do cão.

import pygame

from configuracoes import (
    ALTURA_PAINEL,
    ALTURA_TELA,
    LARGURA_TELA,
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

    def atualizar(self, teclas, dt):
        self.direcao_x = int(teclas[pygame.K_RIGHT]) - int(teclas[pygame.K_LEFT])
        self.direcao_y = int(teclas[pygame.K_DOWN]) - int(teclas[pygame.K_UP])

        direcao = pygame.Vector2(self.direcao_x, self.direcao_y)
        if direcao.length_squared() > 0:
            direcao = direcao.normalize()

        self.posicao += direcao * self.velocidade * dt
        self.posicao.x = max(0, min(self.posicao.x, LARGURA_TELA - self.rect.width))
        self.posicao.y = max(
            ALTURA_PAINEL, min(self.posicao.y, ALTURA_TELA - self.rect.height)
        )
        self.rect.topleft = (round(self.posicao.x), round(self.posicao.y))

    def desenhar(self, tela):
        tela.blit(self.imagem, self.rect)
