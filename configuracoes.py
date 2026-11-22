# Configurações compartilhadas. Altere os valores deste arquivo para ajustar o jogo.
# Este projeto usa três ossos do mesmo tipo, conforme a ideia original.

from pathlib import Path

# Caminhos relativos ao projeto: funcionam mesmo se a pasta for movida.
PASTA_PROJETO = Path(__file__).resolve().parent
PASTA_ASSETS = PASTA_PROJETO / "assets"
PASTA_IMAGENS = PASTA_ASSETS / "imagens"
PASTA_SONS = PASTA_ASSETS / "sons"

CAMINHO_IMAGEM_CAO = PASTA_IMAGENS / "cao.png"
CAMINHO_IMAGEM_OSSO = PASTA_IMAGENS / "osso.png"
CAMINHO_IMAGEM_BOLINHA_TENIS = PASTA_IMAGENS / "bolinha_tenis.png"
CAMINHO_IMAGEM_SACO_RACAO = PASTA_IMAGENS / "saco_racao.png"
CAMINHO_IMAGEM_CASINHA = PASTA_IMAGENS / "casinha.png"
CAMINHO_SOM_LATIDO = PASTA_SONS / "latido.wav"

# Janela e ritmo do jogo.
TITULO_JANELA = "Cão e Ossos"
LARGURA_TELA = 800
ALTURA_TELA = 600
TAMANHO_TELA = (LARGURA_TELA, ALTURA_TELA)
FPS = 60
ALTURA_PAINEL = 80

# Cores RGB.
COR_FUNDO = (130, 185, 100)
COR_PAINEL = (245, 240, 225)
COR_TEXTO = (35, 35, 35)
COR_VITORIA = (20, 100, 45)

# Cão: posições em pixels e velocidade em pixels por segundo.
TAMANHO_CAO = (64, 64)
POSICAO_INICIAL_CAO = (60, 260)
VELOCIDADE_CAO = 240.0

# Três ossos estáticos, posicionados pelo canto superior esquerdo.
TOTAL_OSSOS = 3
TAMANHO_OSSO = (40, 40)
POSICOES_OSSOS = ((240, 140), (420, 340), (620, 160))

TOTAL_BOLINHAS_TENIS = 1
TAMANHO_BOLINHA_TENIS = (36, 36)
POSICOES_BOLINHAS_TENIS = ((340, 220),)

TOTAL_SACOS_RACAO = 1
TAMANHO_SACO_RACAO = (48, 56)
POSICOES_SACOS_RACAO = ((180, 440),)

# Casinha e região da entrada: x, y, largura e altura.
TAMANHO_CASINHA = (100, 130)
POSICAO_CASINHA = (670, 390)
AREA_ENTRADA_CASINHA = (702, 464, 36, 56)

# Fonte padrão do PyGame e tamanhos em pixels.
NOME_FONTE = None
TAMANHO_FONTE_TEXTO = 24
TAMANHO_FONTE_VITORIA = 36

# Volume entre 0.0 (mudo) e 1.0 (máximo).
VOLUME_LATIDO = 0.6

# Valores possíveis para o estado da partida.
ESTADO_JOGANDO = "jogando"
ESTADO_VITORIA = "vitoria"
