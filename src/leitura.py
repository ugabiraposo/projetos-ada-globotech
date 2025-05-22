
def carregar_csv(caminho_arquivo):
    dados = []
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            partes = linha.split(',', 7)

            if len(partes) == 8 and partes[0] != 'id_conteudo':
                dados.append({
                    'id_conteudo': partes[0],
                    'nome_conteudo': partes[1],
                    'id_usuario': partes[2],
                    'timestamp_interacao': partes[3],
                    'plataforma': partes[4],
                    'tipo_interacao': partes[5],
                    'watch_duration_seconds': partes[6],
                    'comment_text': partes[7]
                })

    return dados
