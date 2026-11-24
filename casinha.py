# Pessoa 3: dados iniciais da casinha.

import pygame

from configuracoes import ( #VALORES JÁ PREDEFINIDOS NO configuracoes.py
    AREA_ENTRADA_CASINHA,
    CAMINHO_IMAGEM_CASINHA,
    POSICAO_CASINHA,
    TAMANHO_CASINHA,
)

caminho_imagem = CAMINHO_IMAGEM_CASINHA
imagem = None
posicao = POSICAO_CASINHA #(670,390)
tamanho = TAMANHO_CASINHA #(100,130)

rect = pygame.Rect(posicao, tamanho) #RETANGULO DA CASINHA INTEIRA
area_entrada = AREA_ENTRADA_CASINHA #(702, 464, 36, 56)
rect_entrada = pygame.Rect(area_entrada) #AREA DE ENTRADA QUE O BYTE PRECISA PASSAR


def carregar_imagem():
    imagem_carregada = pygame.image.load(str(caminho_imagem)).convert_alpha() #CONVERTE O CAMINHO_IMAGEM_CASINHA, QUE ESTÁ EM PNG, PARA ALGO QUE DÊ PARA TRABALHAR 
    imagem_carregada = pygame.transform.scale(imagem_carregada, tamanho) #AJUSTE NA ESCALA DO CAMINHO DA CASINHA DE ACORDO COM O TAMANHO
    
    return imagem_carregada 


def desenhar(tela):
    tela.blit(imagem, rect) #RECEBE A TELA DO JOGO E DESENHA A UMAGEM DA CASINHA NELA (COPIANDO A IMAGEM PARA A TELA NA POSIÇÃO DO RECT)


def todos_coletados(quantidades_coletadas, quantidades_necessarias): #RECEBE OS 2 DICIONARIOS DO jogo.py PARA A VERIFICAÇÃO NA FUNÇÃO 
    
    for tipo in quantidades_necessarias:
        if (quantidades_coletadas[tipo] < quantidades_necessarias[tipo]): #VERIFICA SE CADA OBJETO REALMENTE FOI DEVIDAMENTE COLETADO, DADO SUAS QUANTIDADES NECESSARIAS
            
            return False #SE FALTAR ALGUMA QUANTIDADE, RETORNA FALSE E ACABA A FULÇÃO
            
    return True #APENAS RETORNA TRUE SE TODOS OS OBJETOS FORAM DEVIDAMENTE ATENDIDOS


#VERIFICA SE O CAO CHEGOU NA PORTA DEPOIS DE COLETAR TUDO
def verificar_vitoria(rect_cao, quantidades_coletadas, quantidades_necessarias):
    if ((todos_coletados(quantidades_coletadas, quantidades_necessarias)) and (rect_entrada.collidepoint(rect_cao.center))): #CONDIÇÃO DA VITÓRIA: VERIFICA SE A FUNÇÃO DOS COLETÁVEIS É TRUE E VERIFICA SE O (x, y) CENTRAL DO CÃO ESTÁ DENTRO DO RECT DA ENTRADA  
        
        return True
        
    return False
