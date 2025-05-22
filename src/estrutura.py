
def estruturar_dados(dados):
    estrutura = {}
    for item in dados:
        id_conteudo = item['id_conteudo']

        if id_conteudo not in estrutura:
            estrutura[id_conteudo] = {
                'nome_conteudo': item['nome_conteudo'],
                'interacoes': []
            }

        estrutura[id_conteudo]['interacoes'].append({
            'id_usuario': item['id_usuario'],
            'timestamp_interacao': item['timestamp_interacao'],
            'plataforma': item['plataforma'],
            'tipo_interacao': item['tipo_interacao'],
            'watch_duration_seconds': item['watch_duration_seconds'],
            'comment_text': item['comment_text']
        })

    return estrutura
