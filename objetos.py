# Pessoa 2: dados dos ossos.
# Na futura classe Osso, cada osso terá seu próprio rect e estado coletado.
# As posições fixas abaixo serão usadas para criar as três instâncias.

from configuracoes import (
    CAMINHO_IMAGEM_OSSO,
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
