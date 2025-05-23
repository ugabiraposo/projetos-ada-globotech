# Cria um dicionário onde a chave é o 'id_conteudo' e o valor é uma lista com todas as interações daquele conteúdo.


# Entrada: lista de dicionários (dados do CSV).
# Saída: dicionário onde a chave é id_conteudo e o valor é uma lista de dicionários (interações).
def agrupar_por_conteudo(dados):
    try:
        # Estrutura para agrupar os conteúdos em dicionário.
        agrupado = {}

        # Percorre cada linha/iteração do dataset.
        for linha in dados:
            # Pega o id_conteudo para usar como chave do agrupamento.
            id_conteudo = linha[0]

            # Se o id_conteudo ainda não está no dicionário, cria uma nova lista para ele.
            if id_conteudo not in agrupado:
                agrupado[id_conteudo] = {
                    "nome_conteudo": linha[1],
                    "interacoes": [],
                }

            # Adiciona a interação atual na lista correspondente.
            agrupado[id_conteudo]["interacoes"].append(
                {
                    "id_usuario": linha[2],
                    "timestamp_interacao": linha[3],
                    "plataforma": linha[4],
                    "tipo_interacao": linha[5],
                    "watch_duration_seconds": linha[6],
                    "comment_text": linha[7],
                }
            )

        # Retorna o dicionário agrupado.
        return agrupado
    except Exception as e:
        print(f"{e}: não foi possível estruturar os dados.")
        return None
