import os, sys, csv
os.system('cls' if os.name == 'nt' else 'clear')
sys.stdout.reconfigure(
    encoding="utf-8"
)  # Configura a codificação do terminal para UTF-8


def carregar_csv(caminho_arquivo):
    """Carrega um arquivo CSV e retorna uma lista de dicionários."""
    if not os.path.exists(caminho_arquivo):
        print(f"Erro: Arquivo '{caminho_arquivo}' não encontrado.")
        return None

    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            leitor = csv.DictReader(arquivo)
            for linha in leitor:
                dados.append({
                    'id_conteudo': linha.get('id_conteudo', ''),
                    'nome_conteudo': linha.get('nome_conteudo', ''),
                    'id_usuario': linha.get('id_usuario', ''),
                    'timestamp_interacao': linha.get('timestamp_interacao', ''),
                    'plataforma': linha.get('plataforma', ''),
                    'tipo_interacao': linha.get('tipo_interacao', ''),
                    'watch_duration_seconds': linha.get('watch_duration_seconds', ''),
                    'comment_text': linha.get('comment_text', '')
                })
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return None

    return dados