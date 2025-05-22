# Integrantes do grupo
# Alice Ochoa
# Gabriela Raposo
# Isabela Clara
# Mychelle Ketlen
# Rafael Menezes
# Willian Almeida

import csv
import os

os.system("cls" if os.name == "nt" else "clear")  # Limpa o terminal
import sys

sys.stdout.reconfigure(
    encoding="utf-8"
)  # Configura a codificação do terminal para UTF-8


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


# Retirando None e espaços em branco e transformando em 0
def tratamento_de_nulos(dados_csv, indice_tempo):
    for linha in dados_csv:
        for index, _ in enumerate(linha):
            try:
                if index == indice_tempo and (
                    linha[index] == "" or linha[index] == None
                ):
                    linha[index] = 0
            except Exception as e:
                print(f"{e}: não foi possível alterar o valor para 0")

    return dados_csv


# Converte a coluna desejada para inteiro
def conversao_de_coluna_para_int(dados_csv, indice_coluna):
    for linha in dados_csv:
        for index, _ in enumerate(linha):
            try:
                if index == indice_coluna:
                    linha[index] = int(linha[index])
            except Exception as e:
                print(f"{e}: não foi possíel alterar o tipo para inteiro")

    return dados_csv


# Remove espaços desnecessários das strings
def remove_espacos_desnecessarios(cabecalho, dados_csv):
    if not all(col in cabecalho for col in cabecalho):
        raise ValueError("O cabeçalho não contém todas as colunas necessárias.")

    if len(linha) != len(cabecalho):
        raise IndexError(
            "Os dados em `dados_csv` não estão consistentes com as colunas identificadas em `cabecalho`"
        )

    for linha in dados_csv:
        for index, _ in enumerate(linha):
            if type(linha[index]) is str:
                linha[index] = linha[index].strip()

    return dados_csv


# Definindo o arquivo a ser lido
arquivo_globo = "interacoes_globo.csv"

# Passando para a função o arquivo a ser lido e armazenando os retornos da função
cabecalho, dados = carregar_dados_de_arquivo_csv(arquivo_globo)

# Verificando se foi possível carregar o código
if dados is None:
    print("Erro ao carregar os dados. O programa será encerrado.")
    exit()

# Passando os dados para remover espaços desnecessários ao início e ao fim da string
remove_espacos_desnecessarios(cabecalho, dados)

# Armazenando em variáveis o index das colunas necessárias
tempo_assistido_index = cabecalho.index("watch_duration_seconds")
tipo_interacao_index = cabecalho.index("tipo_interacao")
id_conteudo_index = cabecalho.index("id_conteudo")
id_usuario_index = cabecalho.index("id_usuario")

# Enviando para a função os dados a serem tratados
tratamento_de_nulos(dados, tempo_assistido_index)

# Enviando os dados para função para converter para inteiro
conversao_de_coluna_para_int(dados, tempo_assistido_index)
conversao_de_coluna_para_int(dados, id_conteudo_index)
conversao_de_coluna_para_int(dados, id_usuario_index)
