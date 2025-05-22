
from collections import Counter

def total_interacoes_por_conteudo(dados):
    resultado = {}
    for id_conteudo, info in dados.items():
        interacoes = info['interacoes']
        total = sum(1 for i in interacoes if i['tipo_interacao'] in ('like', 'share', 'comment'))
        resultado[id_conteudo] = {
            'nome_conteudo': info['nome_conteudo'],
            'total_interacoes': total
        }
    return resultado

def contagem_por_tipo(dados):
    resultado = {}
    for id_conteudo, info in dados.items():
        contagem = Counter(i['tipo_interacao'] for i in info['interacoes'])
        resultado[id_conteudo] = {
            'nome_conteudo': info['nome_conteudo'],
            'contagem_por_tipo': dict(contagem)
        }
    return resultado

def tempo_total_visualizacao(dados):
    resultado = {}
    for id_conteudo, info in dados.items():
        total = sum(i['watch_duration_seconds'] for i in info['interacoes'] if i['watch_duration_seconds'])
        resultado[id_conteudo] = {
            'nome_conteudo': info['nome_conteudo'],
            'tempo_total_visualizacao': total
        }
    return resultado

def media_tempo_visualizacao(dados):
    resultado = {}
    for id_conteudo, info in dados.items():
        tempos = [i['watch_duration_seconds'] for i in info['interacoes'] if i['watch_duration_seconds'] and i['watch_duration_seconds'] > 0]
        media = sum(tempos) / len(tempos) if tempos else 0
        resultado[id_conteudo] = {
            'nome_conteudo': info['nome_conteudo'],
            'media_tempo_visualizacao': media
        }
    return resultado

def listar_comentarios(id_conteudo, dados):
    if id_conteudo not in dados:
        return []
    comentarios = [i['comment_text'] for i in dados[id_conteudo]['interacoes'] if i['tipo_interacao'] == 'comment' and i['comment_text']]
    return comentarios

def top5_conteudos_visualizacao(dados):
    totais = tempo_total_visualizacao(dados)
    ordenados = sorted(totais.items(), key=lambda x: x[1]['tempo_total_visualizacao'], reverse=True)
    return ordenados[:5]
