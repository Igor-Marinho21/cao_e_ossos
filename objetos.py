# Pessoa 2: dados dos ossos.

from configuracoes import (
    CAMINHO_IMAGEM_OSSO,
    CAMINHO_IMAGEM_BOLINHA_TENIS,
    CAMINHO_IMAGEM_SACO_RACAO,
    POSICOES_BOLINHAS_TENIS,
    POSICOES_SACOS_RACAO,
    TAMANHO_BOLINHA_TENIS,
    TAMANHO_SACO_RACAO,
    POSICOES_OSSOS,
    TAMANHO_OSSO,
)

# A mesma imagem estática poderá ser compartilhada pelos três ossos.
caminho_imagem = CAMINHO_IMAGEM_OSSO
imagem = None
tamanho = TAMANHO_OSSO
posicoes_iniciais = POSICOES_OSSOS

# Dados iniciais de um osso; não representam três instâncias já criadas.
tipo = "osso"
posicao = None
rect = None
coletado = False

caminho_imagem_bolinha_tenis = CAMINHO_IMAGEM_BOLINHA_TENIS
imagem_bolinha_tenis = None
tamanho_bolinha_tenis = TAMANHO_BOLINHA_TENIS
posicoes_iniciais_bolinhas_tenis = POSICOES_BOLINHAS_TENIS
tipo_bolinha_tenis = "bolinha_tenis"
posicao_bolinha_tenis = None
rect_bolinha_tenis = None
bolinha_tenis_coletada = False

caminho_imagem_saco_racao = CAMINHO_IMAGEM_SACO_RACAO
imagem_saco_racao = None
tamanho_saco_racao = TAMANHO_SACO_RACAO
posicoes_iniciais_sacos_racao = POSICOES_SACOS_RACAO
tipo_saco_racao = "saco_racao"
posicao_saco_racao = None
rect_saco_racao = None
saco_racao_coletado = False
