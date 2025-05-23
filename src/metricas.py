
from collections import Counter

def total_interacoes_por_conteudo(dados):
    # Conta o total de interações por conteúdo
    # Considera apenas os tipos de interação: like, share e comment
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
    # Conta a ocorrência de cada tipo de interação em cada conteúdo
    resultado = {}
    for id_conteudo, info in dados.items():
        contagem = Counter(i['tipo_interacao'] for i in info['interacoes'])
        resultado[id_conteudo] = {
            'nome_conteudo': info['nome_conteudo'],
            'contagem_por_tipo': dict(contagem)
        }
    return resultado

def tempo_total_visualizacao(dados):
    # Calcula o tempo total de visualização de cada conteúdo
    resultado = {}
    for id_conteudo, info in dados.items():
        total = sum(i['watch_duration_seconds'] for i in info['interacoes'] if i['watch_duration_seconds'])
        resultado[id_conteudo] = {
            'nome_conteudo': info['nome_conteudo'],
            'tempo_total_visualizacao': total
        }
    return resultado

def media_tempo_visualizacao(dados):
    # Calcula a média de tempo de visualização de cada conteúdo
    resultado = {}
    for id_conteudo, info in dados.items():
        tempos = [i['watch_duration_seconds'] for i in info['interacoes'] if i['watch_duration_seconds'] and i['watch_duration_seconds'] > 0]
        media = sum(tempos) / len(tempos) if tempos else 0
        resultado[id_conteudo] = {
            'nome_conteudo': info['nome_conteudo'],
            'media_tempo_visualizacao': media
        }
    return resultado



def top5_conteudos_visualizacao(dados):
    """Retorna os 5 conteúdos com mais tempo total de visualização."""
    totais = tempo_total_visualizacao(dados)
    ordenados = sorted(totais.items(), key=lambda x: x[1]['tempo_total_visualizacao'], reverse=True)
    return ordenados[:5]

def listar_comentarios(id_conteudo, dados):
    """Lista os comentários de um conteúdo específico."""
    comentarios = []
    if id_conteudo in dados:
        for interacao in dados[id_conteudo]["interacoes"]:
            if interacao["tipo_interacao"] == "comment" and interacao["comment_text"]:
                comentarios.append(interacao["comment_text"])
    return comentarios


def listar_comentarios_por_conteudo(dados):
    """
    Lista os comentários de todos os conteúdos, apenas do tipo 'comment'.
    """
    resultado = {}
    for id_conteudo, info in dados.items():
        if 'interacoes' in info and isinstance(info['interacoes'], list):
            comentarios_do_conteudo = [
                i['comment_text'] for i in info['interacoes']
                if i['tipo_interacao'] == 'comment' and i['comment_text']
            ]
            resultado[id_conteudo] = {
                'nome_conteudo': info['nome_conteudo'],
                'comentarios': comentarios_do_conteudo
            }
    return resultado

def converter_segundos_para_hms(segundos):
    """Converte segundos em formato HH:MM:SS."""
    
    if not isinstance(segundos, (int, float)):
        raise ValueError("O argumento deve ser um número")
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60

    return f"{int(horas):02d}:{int(minutos):02d}:{segundos_restantes:05.2f}"
