def estruturar_dados(dados):
    estrutura = {}
    for linha in dados:
        id_conteudo = linha[0]

        if id_conteudo not in estrutura:
            estrutura[id_conteudo] = {
                "nome_conteudo": linha[1],
                "interacoes": [],
            }

        estrutura[id_conteudo]["interacoes"].append(
            {
                "id_usuario": linha[2],
                "timestamp_interacao": linha[3],
                "plataforma": linha[4],
                "tipo_interacao": linha[5],
                "watch_duration_seconds": linha[6],
                "comment_text": linha[7],
            }
        )

    return estrutura
