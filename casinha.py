# Pessoa 3: dados iniciais da casinha.

import pygame

from configuracoes import (
    AREA_ENTRADA_CASINHA,
    CAMINHO_IMAGEM_CASINHA,
    POSICAO_CASINHA,
    TAMANHO_CASINHA,
)

caminho_imagem = CAMINHO_IMAGEM_CASINHA
imagem = None
posicao = POSICAO_CASINHA
tamanho = TAMANHO_CASINHA

# RETANGULO DA IMAGEM E RETANGULO ESPECIFICO DA PORTA
rect = pygame.Rect(posicao, tamanho)
area_entrada = AREA_ENTRADA_CASINHA
rect_entrada = pygame.Rect(area_entrada)


# CARREGA A IMAGEM E AJUSTA O TAMANHO (CHAMAR DEPOIS DE CRIAR A JANELA)
def carregar_imagem():
    imagem_carregada = pygame.image.load(str(caminho_imagem)).convert_alpha()
    imagem_carregada = pygame.transform.scale(imagem_carregada, tamanho)
    return imagem_carregada


# DESENHA A CASINHA NA TELA
def desenhar(tela):
    tela.blit(imagem, rect)


# CONFERE SE TODOS OS ITENS JA FORAM COLETADOS
def todos_coletados(coletadas, necessarias):
    for tipo in necessarias:
        if (coletadas[tipo] < necessarias[tipo]):
            return False
    return True


# VERIFICA SE O CAO CHEGOU NA PORTA DEPOIS DE COLETAR TUDO
def verificar_vitoria(rect_cao, coletadas, necessarias):
    if ((todos_coletados(coletadas, necessarias)) and (rect_entrada.collidepoint(rect_cao.center))):
        return True
    return False
