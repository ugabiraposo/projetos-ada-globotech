
from src.leitura import carregar_csv
from src.limpeza import limpar_dados
from src.estrutura import estruturar_dados
from src.metricas import (
    total_interacoes_por_conteudo,
    contagem_por_tipo,
    tempo_total_visualizacao,
    media_tempo_visualizacao,
    top5_conteudos_visualizacao
)
from src.salvar import (
    salvar_metricas_em_csv,
    salvar_contagem_por_tipo,
    salvar_top5
)

caminho_csv = 'data/interacoes_globo.csv'
pasta_saida = 'outputs/'

print('Carregando dados...')
dados = carregar_csv(caminho_csv)

print('Limpando dados...')
dados_limpos = limpar_dados(dados)

print('Estruturando dados...')
dados_estruturados = estruturar_dados(dados_limpos)

print('Calculando métricas...')
metricas_interacoes = total_interacoes_por_conteudo(dados_estruturados)
metricas_tipos = contagem_por_tipo(dados_estruturados)
metricas_tempo_total = tempo_total_visualizacao(dados_estruturados)
metricas_media_tempo = media_tempo_visualizacao(dados_estruturados)
top5 = top5_conteudos_visualizacao(dados_estruturados)

print('Salvando métricas...')
salvar_metricas_em_csv(pasta_saida + 'metricas_total_interacoes.csv', metricas_interacoes, ['total_interacoes'])
salvar_metricas_em_csv(pasta_saida + 'metricas_tempo_total.csv', metricas_tempo_total, ['tempo_total_visualizacao'])
salvar_metricas_em_csv(pasta_saida + 'metricas_media_tempo.csv', metricas_media_tempo, ['media_tempo_visualizacao'])
salvar_contagem_por_tipo(pasta_saida + 'metricas_contagem_por_tipo.csv', metricas_tipos)
salvar_top5(pasta_saida + 'metricas_top5_visualizacao.csv', top5)

print('Processo finalizado!')
