import csv


def salvar_metricas_em_csv(nome_arquivo, dados, campos_extra):
    """Salva as métricas em um arquivo CSV."""
    with open(nome_arquivo, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["id_conteudo", "nome_conteudo"] + campos_extra)
        for id_conteudo, info in dados.items():
            linha = [id_conteudo, info["nome_conteudo"]]
            for campo in campos_extra:
                linha.append(info[campo])
            writer.writerow(linha)


def salvar_contagem_por_tipo(nome_arquivo, dados):
    """Salva a contagem de interações por tipo em um arquivo CSV."""
    with open(nome_arquivo, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(
            ["id_conteudo", "nome_conteudo", "tipo_interacao", "quantidade"]
        )
        for id_conteudo, info in dados.items():
            for tipo, quantidade in info["contagem_por_tipo"].items():
                writer.writerow([id_conteudo, info["nome_conteudo"], tipo, quantidade])


def salvar_top5(nome_arquivo, dados):
    """Salva os 5 conteúdos com mais tempo total de visualização em um arquivo CSV."""
    with open(nome_arquivo, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["id_conteudo", "nome_conteudo", "tempo_total_visualizacao"])
        for item in dados:
            id_conteudo = item[0]
            info = item[1]
            writer.writerow(
                [id_conteudo, info["nome_conteudo"], info["tempo_total_visualizacao"]]
            )
