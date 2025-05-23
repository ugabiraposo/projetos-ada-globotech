import os, sys

os.system("cls" if os.name == "nt" else "clear")
sys.stdout.reconfigure(encoding="utf-8")  # Corrige acentuação no terminal Windows
from src.limpeza import pipeline_limpeza
from src.estrutura import estruturar_dados
from src.metricas import (
    total_interacoes_por_conteudo,
    contagem_por_tipo,
    tempo_total_visualizacao,
    media_tempo_visualizacao,
    top5_conteudos_visualizacao,
    listar_comentarios,
    listar_comentarios_por_conteudo,
    converter_segundos_para_hms,
)
from src.salvar import salvar_metricas_em_csv, salvar_contagem_por_tipo, salvar_top5

# 📥 Pasta de saída
pasta_saida = "outputs/"

# 📦 Pipeline inicial
print("Limpando dados...")
dados_limpos = pipeline_limpeza()

print("Estruturando dados...")
dados_estruturados = estruturar_dados(dados_limpos)

print("Calculando métricas...")
metricas_interacoes = total_interacoes_por_conteudo(dados_estruturados)
metricas_tipos = contagem_por_tipo(dados_estruturados)
metricas_tempo_total = tempo_total_visualizacao(dados_estruturados)
metricas_media_tempo = media_tempo_visualizacao(dados_estruturados)
top5 = top5_conteudos_visualizacao(dados_estruturados)

#Criando pasta Outputs
criando_pasta = criar_pasta



# -----------------------------
# 🖥️ Menu Interativo
# -----------------------------
print("\n---------------------------")
print("Sistema de Interações GloboTech")
print("---------------------------")

while True:
    print("\nMenu de opções:")
    print("1. Visualizar métricas de interações por conteúdo")
    print("2. Visualizar contagem por tipo de interação")
    print("3. Visualizar tempo total de visualização por conteúdo")
    print("4. Visualizar média de tempo de visualização por conteúdo")
    print("5. Visualizar top 5 de conteúdos com mais tempo de visualização")
    print("6. Visualizar comentários de um conteúdo específico")
    print("7. Visualizar total de comentários por conteúdo")
    print("8. Salvar métricas em CSV")
    print("9. Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        print("\n📊 Métricas de interações por conteúdo: \n")
        for conteudo, metrica in metricas_interacoes.items():
            nome_conteudo = metrica["nome_conteudo"]
            print(
                f"📺 {conteudo} - {nome_conteudo}: {metrica['total_interacoes']} interações"
            )

    elif opcao == "2":
        print("\n Contagem por tipo de interação: \n")
        for id_conteudo, info in metricas_tipos.items():
            print(f"➡️  {info['nome_conteudo']}")
            for tipo, contagem in info["contagem_por_tipo"].items():
                if tipo == "view_start":
                    print(f"  👀  {tipo}: {contagem}")
                elif tipo == "like":
                    print(f"  ❤️   {tipo}: {contagem}")
                elif tipo == "comment":
                    print(f"  💬  {tipo}: {contagem}")
                elif tipo == "share":
                    print(f"  🤝  {tipo}: {contagem}")
            print("---------------------------------------")

    elif opcao == "3":
        print("\n⏱️ Tempo total de visualização por conteúdo: \n")
        for conteudo, metrica in metricas_tempo_total.items():
            tempo_formatado = converter_segundos_para_hms(
                metrica["tempo_total_visualizacao"]
            )
            nome_conteudo = metrica["nome_conteudo"]
            print(f"📺 {conteudo} - {nome_conteudo}: {tempo_formatado}")

    elif opcao == "4":
        print("\n⏱️ Média de tempo de visualização por conteúdo: \n")
        for conteudo, metrica in metricas_media_tempo.items():
            nome_conteudo = metrica["nome_conteudo"]
            tempo_formatado = converter_segundos_para_hms(
                metrica["media_tempo_visualizacao"]
            )
            print(f"📺 {conteudo} - {nome_conteudo}: {tempo_formatado}")

    elif opcao == "5":
        print("\n🏆 Top 5 de conteúdos com mais tempo de visualização: \n")
        for conteudo, info in top5:
            tempo_formatado = converter_segundos_para_hms(
                info["tempo_total_visualizacao"]
            )
            print(f"📺 {info['nome_conteudo']} - {tempo_formatado}")

    elif opcao == "6":
        id_conteudo = input("Digite o ID do conteúdo que deseja ver os comentários: \n")
        try:
            id_conteudo = int(id_conteudo)
            comentarios = listar_comentarios(id_conteudo, dados_estruturados)
            if comentarios:
                print(
                    f"\n💬 Comentários do conteúdo {id_conteudo} - {dados_estruturados[id_conteudo]['nome_conteudo']}:"
                )
                for comentario in comentarios:
                    print(f"➡️  {comentario}")
            else:
                print("❌ Nenhum comentário encontrado para este conteúdo.")
        except ValueError:
            print("❌ ID inválido. Digite um número inteiro.")

    elif opcao == "7":
        print("\n💬 Total de comentários por conteúdo: \n")
        comentarios_por_conteudo = listar_comentarios_por_conteudo(dados_estruturados)
        for conteudo, info in comentarios_por_conteudo.items():
            comentarios = info["comentarios"]
            print(f"Comentários do conteúdo {conteudo}: {info['nome_conteudo']}")
            print(f"Total de comentários: {len(comentarios)}")
            print()

    elif opcao == "8":
        print("💾 Salvando métricas em CSV...")
        salvar_metricas_em_csv(
            pasta_saida + "metricas_total_interacoes.csv",
            metricas_interacoes,
            ["total_interacoes"],
        )
        salvar_metricas_em_csv(
            pasta_saida + "metricas_tempo_total.csv",
            metricas_tempo_total,
            ["tempo_total_visualizacao"],
        )
        salvar_metricas_em_csv(
            pasta_saida + "metricas_media_tempo.csv",
            metricas_media_tempo,
            ["media_tempo_visualizacao"],
        )
        salvar_contagem_por_tipo(
            pasta_saida + "metricas_contagem_por_tipo.csv", metricas_tipos
        )
        salvar_top5(pasta_saida + "metricas_top5_visualizacao.csv", top5)
        print("✅ Métricas salvas na pasta outputs/")

    elif opcao == "9":
        print("👋 Saindo do sistema. Até logo! \n")
        break

    else:
        print("❌ Opção inválida. Tente novamente.")
    print("\n---------------------------")
