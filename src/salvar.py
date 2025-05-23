# Arquivo responsável por salvar os dados processados em arquivos CSV na pasta outputs.

# Módulo nativo do Python usado para manipulação de arquivos CSV.
import csv
import os


# Salva as métricas em um arquivo CSV.
def salvar_metricas_em_csv(nome_arquivo, dados, campos_extra):
    try:
        diretorio = os.path.dirname(nome_arquivo)
        if diretorio and not os.path.exists(diretorio):
            os.makedirs(diretorio, exist_ok=True)
    except Exception as e:
        print(f"{e}: não foi possível criar o diretório")
        return None
    try:
        with open(nome_arquivo, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["id_conteudo", "nome_conteudo"] + campos_extra)
            for id_conteudo, info in dados.items():
                linha = [id_conteudo, info["nome_conteudo"]]
                for campo in campos_extra:
                    linha.append(info[campo])
                writer.writerow(linha)
    except Exception as e:
        print(f"{e}: não foi possível salvar as métricas no arquivo CSV.")
        return None

    # Verifica se o diretório existe e cria se não existir
    diretorio = os.path.dirname(nome_arquivo)
    if diretorio and not os.path.exists(diretorio):
        os.makedirs(diretorio, exist_ok=True)


# Salva a contagem de interações por tipo em um arquivo CSV.
def salvar_contagem_por_tipo(nome_arquivo, dados):
    # Verifica se o diretório existe e cria se não existir
    try:
        diretorio = os.path.dirname(nome_arquivo)
        if diretorio and not os.path.exists(diretorio):
            os.makedirs(diretorio, exist_ok=True)
    except Exception as e:
        print(f"{e}: não foi possível criar o diretório")
        return None

    try:
        with open(nome_arquivo, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(
                ["id_conteudo", "nome_conteudo", "tipo_interacao", "quantidade"]
            )
            for id_conteudo, info in dados.items():
                for tipo, quantidade in info["contagem_por_tipo"].items():
                    writer.writerow(
                        [id_conteudo, info["nome_conteudo"], tipo, quantidade]
                    )
    except Exception as e:
        print(f"{e}: não foi possível salvar a contagem de interações no arquivo CSV.")
        return None


# Salva os 5 conteúdos com mais tempo total de visualização em um arquivo CSV.
def salvar_top5(nome_arquivo, dados):
    try:
        diretorio = os.path.dirname(nome_arquivo)
        if diretorio and not os.path.exists(diretorio):
            os.makedirs(diretorio, exist_ok=True)
    except Exception as e:
        print(f"{e}: não foi possível criar o diretório")
        return None
    try:
        with open(nome_arquivo, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(
                ["id_conteudo", "nome_conteudo", "tempo_total_visualizacao"]
            )
            for item in dados:
                id_conteudo = item[0]
                info = item[1]

                writer.writerow(
                    ["id_conteudo", "nome_conteudo", "tempo_total_visualizacao"]
                )

                for item in dados:
                    id_conteudo = item[0]
                    info = item[1]
                    writer.writerow(
                        [
                            id_conteudo,
                            info["nome_conteudo"],
                            info["tempo_total_visualizacao"],
                        ]
                    )
    except Exception as e:
        print(
            f"{e}: não foi possível salvar os 5 conteúdos com mais tempo de visualização em um arquivo CSV."
        )
        return None
