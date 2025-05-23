from src.leitura import carregar_dados_de_arquivo_csv


def tratamento_de_nulos(dados_csv, indice_tempo):
    # Percorrendo a tabela
    for linha in dados_csv:
        # Percorrendo cada elemento da tabela
        for index, _ in enumerate(linha):
            try:
                # Caso o index do elemento atual seja igual ao índice passado por parâmetro
                # E esteja "" ou None, então será setado o valor 0.
                # O valor 0 foi definido independente da coluna de tipo de duração por
                # Motivo de conveniência para facilitar a conversão da coluna para inteiro
                # Quando for necessário manipular interações do tipo 'like', 'share, 'comment'
                # Então será "olhado" diretamente para essa coluna de tipo de interação
                if index == indice_tempo and (
                    linha[index] == "" or linha[index] == None
                ):
                    linha[index] = 0
            except Exception as e:
                print(f"{e}: não foi possível alterar o valor para 0")

    return dados_csv


# Converte a coluna desejada para inteiro
def conversao_de_coluna_para_int(dados_csv, indice_coluna):
    # Percorrendo a tabela
    for linha in dados_csv:
        # Percorrendo cada elemento da tabela
        for index, _ in enumerate(linha):
            try:
                # Caso o index do elemento atual seja igual ao index da coluna que
                # irá ser convertida para inteiro, então é feita a transformação
                # para tipo inteiro.
                if index == indice_coluna:
                    linha[index] = int(linha[index])
            except Exception as e:
                print(f"{e}: não foi possíel alterar o tipo para inteiro")

    return dados_csv


# Remove espaços desnecessários das strings
def remove_espacos_desnecessarios(cabecalho, dados_csv):
    if not all(col in cabecalho for col in cabecalho):
        raise ValueError("O cabeçalho não contém todas as colunas necessárias.")

    for linha in dados_csv:
        for index, _ in enumerate(linha):
            if type(linha[index]) is str:
                linha[index] = linha[index].strip()

    return dados_csv


def pipeline_limpeza():
    # Definindo o arquivo a ser lido
    arquivo_globo = "data/interacoes_globo.csv"

    # Passando para a função o arquivo a ser lido e armazenando os retornos da função
    cabecalho, dados = carregar_dados_de_arquivo_csv(arquivo_globo)

    # Armazenando em variáveis o index das colunas necessárias
    tempo_assistido_index = cabecalho.index("watch_duration_seconds")
    id_conteudo_index = cabecalho.index("id_conteudo")
    id_usuario_index = cabecalho.index("id_usuario")

    # Passando os dados para remover espaços desnecessários ao início e ao fim da string
    remove_espacos_desnecessarios(cabecalho, dados)

    # Enviando para a função os dados com nulos a serem tratados
    tratamento_de_nulos(dados, tempo_assistido_index)

    # Enviando os dados para função para converter para inteiro
    conversao_de_coluna_para_int(dados, tempo_assistido_index)
    conversao_de_coluna_para_int(dados, id_conteudo_index)
    conversao_de_coluna_para_int(dados, id_usuario_index)

    return dados
