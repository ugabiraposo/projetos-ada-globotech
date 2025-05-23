
def estruturar_dados(dados):

    """Estrutura os dados de interações em um dicionário aninhado."""
    if not isinstance(dados, list):
        raise TypeError("Os dados devem ser uma lista de dicionários.")

    estrutura = {}
    for item in dados:
        try:
            id_conteudo = int(item.get('id_conteudo'))

            if id_conteudo not in estrutura:
                estrutura[id_conteudo] = {
                    'nome_conteudo': item.get('nome_conteudo', 'Desconhecido'),
                    'interacoes': []
                }

            estrutura[id_conteudo]['interacoes'].append({
                'id_usuario': int(item.get('id_usuario', 0)),
                'timestamp_interacao': item.get('timestamp_interacao', ''),
                'plataforma': item.get('plataforma', ''),
                'tipo_interacao': item.get('tipo_interacao', ''),
                'watch_duration_seconds': (
                    int(item['watch_duration_seconds'])
                    if item.get('watch_duration_seconds') not in [None, '', 'None']
                    else 0
                ),
                'comment_text': item.get('comment_text', '')
            })

        except Exception as e:
            print(f"Aviso: Erro ao processar item {item}. Erro: {e}")

    return estrutura

"""
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
"""