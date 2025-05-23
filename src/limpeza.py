
def limpar_dados(lista_dados):
    dados_limpos = []

    for item in lista_dados:
        try:
            id_conteudo = int(item['id_conteudo'].strip())
            nome_conteudo = item['nome_conteudo'].strip()
            id_usuario = int(item['id_usuario'].strip())
            timestamp = item['timestamp_interacao'].strip()
            plataforma = item['plataforma'].strip()
            tipo_interacao = item['tipo_interacao'].strip().lower()
            comment_text = item['comment_text'].strip() if item['comment_text'] else ''

            raw_duracao = item['watch_duration_seconds'].strip()
            if raw_duracao == '':
                duracao = 0 if tipo_interacao == 'view_start' else None
            else:
                duracao = int(raw_duracao)

            dados_limpos.append({
                'id_conteudo': id_conteudo,
                'nome_conteudo': nome_conteudo,
                'id_usuario': id_usuario,
                'timestamp_interacao': timestamp,
                'plataforma': plataforma,
                'tipo_interacao': tipo_interacao,
                'watch_duration_seconds': duracao,
                'comment_text': comment_text
            })

        except (ValueError, TypeError) as e:
            print(f"Erro ao processar item {item}: {e}")
            continue

    return dados_limpos
