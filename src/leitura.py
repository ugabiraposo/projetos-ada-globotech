# Função responsável por ler um arquivo CSV e transformar em uma lista de dicionários.


# Importações dos módulos nativos 'os', 'csv' e 'sys'.
import os, sys, csv

# Limpa o terminal
os.system("cls" if os.name == "nt" else "clear")

# Configura a codificação do terminal para UTF-8
sys.stdout.reconfigure(encoding="utf-8")


# Função padrão para carregamento de dados
def carregar_dados_de_arquivo_csv(nome_arquivo):
    dados = []

    try:
        with open(nome_arquivo, mode="r", encoding="utf-8", newline="") as arquivo_csv:
            leitor_csv = csv.reader(arquivo_csv)

            # Pegando apenas o cabeçalho da lista
            cabecalho = next(leitor_csv)

            # Problema:  Comentários com vírgula estão se tornando uma nova coluna no csv
            # Resolução: Pegando o tamanho padrão da tabela através do cabeçalho
            #            Em cada linha compara o tamanho da linha com o tamanho do cabeçalho
            #            Caso o tamanho da linha seja maior que o tamanho do cabeçalho
            #            Então será enviado para a função de tratamento de comentários com vírgula.
            num_colunas = len(cabecalho)

            # Adiciona todas as linhas (exceto o cabeçalho) à lista
            for linha in leitor_csv:
                # Caso o tamanho da linha seja maior que o número de colunas,
                # Significa que há vírgula no comentário, então será enviado
                # Para a função para tratar o caso
                if len(linha) > num_colunas:
                    linha = tratamento_de_comentario_com_virgula(linha)
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


# Função para tratar os comentários com vírgula
# Tratando antes de enviar para a pipeline de limpeza
def tratamento_de_comentario_com_virgula(linha):
    try:
        # Inicializando o comentário de forma vazia
        comentario = ""

        # Percorrendo a linha enviada por parâmetro a partir da coluna de comentários
        # Ou seja, independente da quantidade de vírgulas que haja no comentário,
        # Tudo se tornará apenas 1 coluna, removendo as vírgulas
        for c in linha[7:]:
            comentario += c

        # Após o tratamento do comentário, será retornado uma concatenação até uma coluna
        # Anterior à coluna de comentário, que foi passado por parâmetro, juntamente
        # Com o comentário gerado no for
        return linha[:7] + [comentario]
    except Exception as e:
        print(f"{e}: não foi possível tratar o comentário")
        return None
