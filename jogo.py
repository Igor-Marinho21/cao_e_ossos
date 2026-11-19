# Pessoa 5: estado geral e integração.
# Na implementação com orientação a objetos, estas variáveis de estado
# poderão se tornar atributos da classe Jogo (por exemplo, self.tela).

from configuracoes import ESTADO_JOGANDO, TOTAL_OSSOS

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

# Contagem centralizada aqui, para ser consultada pela interface e pela vitória.
quantidades_coletadas = {"osso": 0}
quantidades_necessarias = {"osso": TOTAL_OSSOS}
