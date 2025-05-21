# Integrantes do grupo
# Alice Ochoa
# Gabriela Raposo
# Isabela Clara
# Mychelle Ketlen
# Rafael Menezes
# Willian Almeida

import csv
import os
os.system("cls" if os.name == "nt" else "clear") #Limpa o terminal
import sys
sys.stdout.reconfigure(encoding='utf-8') #Configura a codificação do terminal para UTF-8


# Cabecalho do arquivo CSV
# id_conteudo,nome_conteudo,id_usuario,timestamp_interacao,plataforma,tipo_interacao,watch_duration_seconds,comment_text
cabecalho = [
    "id_conteudo",
    "nome_conteudo",
    "id_usuario",
    "timestamp_interacao",
    "plataforma",
    "tipo_interacao",
    "watch_duration_seconds",
    "comment_text",
]



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

# Remove espaços desnecessários dos dados
def remove_espacos_desnecessarios(cabecalho, dados_csv):
    
    required_columns = ["nome_conteudo", "timestamp_interacao", "plataforma", "tipo_interacao", "watch_duration_seconds", "comment_text"]
    if not all(col in cabecalho for col in required_columns):
        raise ValueError("O cabeçalho não contém todas as colunas necessárias.")
    
    # Identifica os índices das colunas de texto
    nome_conteudo_index = cabecalho.index("nome_conteudo")
    timestamp_interacao_index = cabecalho.index("timestamp_interacao")
    plataforma_index = cabecalho.index("plataforma")
    tipo_interacao_index = cabecalho.index("tipo_interacao")
    watch_duration_seconds_index = cabecalho.index("watch_duration_seconds")
    comentario_index = cabecalho.index("comment_text")


    for linha in dados_csv:
        if len(linha) != len(cabecalho):
            raise IndexError("Os dados em `dados_csv` não estão consistentes com as colunas identificadas em `cabecalho`")

        # Remove espaços desnecessários de cada coluna de texto
        linha[nome_conteudo_index] = linha[nome_conteudo_index].strip()
        linha[timestamp_interacao_index] = linha[timestamp_interacao_index].strip()
        linha[plataforma_index] = linha[plataforma_index].strip()
        linha[tipo_interacao_index] = linha[tipo_interacao_index].strip()
        linha[watch_duration_seconds_index] = linha[watch_duration_seconds_index].strip()
        linha[comentario_index] = linha[comentario_index].strip()
        
        return dados_csv
    #pass
    
# Função para exibir os dados formatados e tabulados no terminal
def exibir_dados_formatados(cabecalho, dados, coluna_ordenacao=None, reverso=False):
    # Filtra linhas que não tenham o mesmo tamanho que o cabeçalho
    dados_validos = [linha for linha in dados if len(linha) == len(cabecalho)]

    if not dados_validos:
        print("Nenhum dado válido para exibir.")
        return

    # Se for solicitada ordenação, aplica
    if coluna_ordenacao and coluna_ordenacao in cabecalho:
        indice_ordenacao = cabecalho.index(coluna_ordenacao)

        def ordenar_num_ou_str(valor):
            try:
                return int(valor[indice_ordenacao])
            except (ValueError, TypeError):
                return str(valor[indice_ordenacao])

        dados_validos = sorted(
            dados_validos,
            key=ordenar_num_ou_str,
            reverse=reverso,
        )

    # Calcula o tamanho máximo de cada coluna para formatação
    tamanhos_colunas = [len(col) for col in cabecalho]
    for linha in dados_validos:
        for i, valor in enumerate(linha):
            tamanhos_colunas[i] = max(tamanhos_colunas[i], len(str(valor)))

    # Monta o cabeçalho formatado
    linha_cabecalho = " | ".join(
        col.ljust(tamanhos_colunas[i]) for i, col in enumerate(cabecalho)
    )
    separador = "-+-".join("-" * tamanhos_colunas[i] for i in range(len(cabecalho)))

    print(linha_cabecalho)
    print(separador)

    # Monta as linhas de dados
    for linha in dados_validos:
        linha_formatada = " | ".join(
            str(valor).ljust(tamanhos_colunas[i]) for i, valor in enumerate(linha)
        )
        print(linha_formatada)

    print()  # Linha em branco no final para separação



# Definindo o arquivo a ser lido
arquivo_globo = "interacoes_globo.csv"


# Passando para a função o arquivo a ser lido e armazenando os retornos da função
cabecalho, dados = carregar_dados_de_arquivo_csv(arquivo_globo)

# Verifica se o arquivo foi carregado corretamente
if dados is None:
    print("Erro ao carregar os dados. O programa será encerrado.")
    exit()

# Verifica se o cabeçalho está correto
if cabecalho != ["id_conteudo", "nome_conteudo", "id_usuario", "timestamp_interacao", "plataforma", "tipo_interacao", "watch_duration_seconds", "comment_text"]:
    print("Erro: O cabeçalho do arquivo CSV não está correto.")
    exit()
dados = remove_espacos_desnecessarios(cabecalho, dados)

# Exibindo os dados formatados

exibir_dados_formatados(cabecalho, dados, coluna_ordenacao="id_conteudo")


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

