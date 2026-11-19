# Pessoa 4: textos, posições da interface e áudio.
# A contagem real pertence a jogo.py; não há outro contador neste arquivo.

from configuracoes import (
    CAMINHO_SOM_LATIDO,
    NOME_FONTE,
    TAMANHO_FONTE_TEXTO,
    TAMANHO_FONTE_VITORIA,
    VOLUME_LATIDO,
)

# Fontes e textos renderizados: serão criados na implementação.
nome_fonte = NOME_FONTE
tamanho_fonte_texto = TAMANHO_FONTE_TEXTO
tamanho_fonte_vitoria = TAMANHO_FONTE_VITORIA
fonte_texto = None
fonte_vitoria = None
superficie_contador = None
superficie_instrucoes = None
superficie_vitoria = None

# Modelo de texto; os campos serão preenchidos com os dados da partida.
texto_contador = "Ossos: {coletados}/{total}"
texto_instrucoes = "Use as setas. Pegue os três ossos e vá para a casinha!"
texto_vitoria = "Você venceu!"

# Posições dos textos em pixels. Vitória usa alinhamento pelo centro.
posicao_contador = (20, 12)
posicao_instrucoes = (20, 44)
centro_mensagem_vitoria = (400, 300)

# O som será carregado uma vez e acionado a cada coleta, futuramente.
caminho_som_latido = CAMINHO_SOM_LATIDO
som_latido = None
volume_latido = VOLUME_LATIDO
