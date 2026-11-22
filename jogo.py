# Pessoa 5: estado geral e integração.

from configuracoes import (
    ESTADO_JOGANDO,
    TOTAL_OSSOS,
    TOTAL_BOLINHAS_TENIS,
    TOTAL_SACOS_RACAO,
)

# Recursos do PyGame que serão criados posteriormente.
tela = None
relogio = None

# Controle de execução e intervalo entre quadros, em segundos.
executando = False
estado_jogo = ESTADO_JOGANDO
tempo_delta = 0.0

# Referências às futuras instâncias das classes do projeto.
cao = None
casinha = None
interface = None

# Lista que receberá as instâncias dos ossos ainda presentes na tela.
ossos = []
bolinhas_tenis = []
sacos_racao = []

# Contagem centralizada aqui, para ser consultada pela interface e pela vitória.
quantidades_coletadas = {"osso": 0, "bolinha_tenis": 0, "saco_racao": 0}
quantidades_necessarias = {
    "osso": TOTAL_OSSOS,
    "bolinha_tenis": TOTAL_BOLINHAS_TENIS,
    "saco_racao": TOTAL_SACOS_RACAO,
}
