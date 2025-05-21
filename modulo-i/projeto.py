# Integrantes do grupo
# Alice Ochoa
# Gabriela Raposo
# Isabela Clara
# Mychelle Ketlen
# Rafael Menezes
# Willian Almeida

import csv


# Função para realizar o tratamento do arquivo .csv
def carregar_dados_de_arquivo_csv(nome_arquivo):
    dados = []
    try:
        with open(nome_arquivo, mode="r", encoding="utf-8", newline="") as arquivo_csv:
            leitor_csv = csv.reader(arquivo_csv)

            # Pegando apenas o cabeçalho da lista
            cabecalho = next(leitor_csv)

            # Adiciona todas as linhas (exceto o cabeçalho) à lista
            for linha in leitor_csv:
                dados.append(linha)

        if not dados:
            print(f"Aviso: O arquivo CSV '{nome_arquivo}' está vazio.")
            return None
        return cabecalho, dados
    except FileNotFoundError:
        print(
            f"Erro: Arquivo '{nome_arquivo}' não encontrado. Certifique-se de que ele está na mesma pasta do script."
        )
        return None
    except Exception as e:
        print(f"Erro ao ler o arquivo CSV '{nome_arquivo}': {e}")
        return None


def tratamento_de_nulos(
    lista_listas,
    indice_coluna,
    valor_substituicao1,
    indice_comparacao,
    valor_comparacao,
    valor_substituicao2,
):
    return [
        [
            (
                valor_substituicao1
                if i == indice_coluna
                and linha[indice_coluna] is None
                and linha[indice_comparacao] == valor_comparacao
                else (
                    valor_substituicao2
                    if i == indice_coluna and linha[indice_coluna] is None
                    else x
                )
            )
            for i, x in enumerate(linha)
        ]
        for linha in lista_listas
    ]  # melhorar aqui!


# Converte a coluna desejada para Inteiro
def conversao_de_coluna_para_int(dados_csv, coluna):
    for linha in dados_csv:
        for index in range(len(linha)):
            if index == coluna and linha[index - 1] == "view_start":
                linha[index] = int(linha[index])

    return dados_csv


def remove_espacos_desnecessarios():
    pass


# Definindo o arquivo a ser lido
arquivo_globo = "interacoes_globo.csv"

# Passando para a função o arquivo a ser lido e armazenando os retornos da função
cabecalho, dados = carregar_dados_de_arquivo_csv(arquivo_globo)

# Armazenando em variáveis o index das colunas necessárias
tempo_assistido_index = cabecalho.index("watch_duration_seconds")
tipo_interacao_index = cabecalho.index("tipo_interacao")

# Definindo variáveis para a função tratamento_de_nulos()
consumo_video = "view_start"
assistiu_s = 0
assistiu_n = None

# Enviando para a função os dados a serem tratados
tratando_nulos = tratamento_de_nulos(
    dados,
    tempo_assistido_index,
    assistiu_s,
    tipo_interacao_index,
    consumo_video,
    assistiu_n,
)

# Enviando os dados para função para converter o tempo assistido para inteiro
conversao_de_tempo_para_int = conversao_de_coluna_para_int(dados, tempo_assistido_index)
