from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet

def gerar_pdf(resultados, empresa):
    doc = SimpleDocTemplate("relatorio_pgr.pdf")
    styles = getSampleStyleSheet()

    elementos = []

    elementos.append(Paragraph(f"Relatório Psicossocial - {empresa}", styles["Title"]))
    elementos.append(Spacer(1, 12))

    elementos.append(Paragraph(
        "Avaliação realizada com base na metodologia COPSOQ, conforme NR-1.",
        styles["Normal"]
    ))

    elementos.append(Spacer(1, 12))

    for dim, dados in resultados.items():
        texto = f"{dim}: Média {dados['media']} - Risco {dados['risco']}"
        elementos.append(Paragraph(texto, styles["Normal"]))
        elementos.append(Spacer(1, 8))

    elementos.append(Spacer(1, 20))
    elementos.append(Image("grafico.png", width=400, height=250))

    elementos.append(Spacer(1, 20))

    elementos.append(Paragraph("Conclusão:", styles["Heading2"]))
    elementos.append(Paragraph(
        "Os resultados indicam a necessidade de monitoramento e implementação de medidas preventivas conforme NR-1.",
        styles["Normal"]
    ))

    doc.build(elementos)
