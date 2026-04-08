import pandas as pd
from report_generator import calcular_empresa
from charts import gerar_grafico
from pdf_report import gerar_pdf
import streamlit as st
import requests
import json
from questions import questions
from scoring import calcular

st.title("Avaliação Psicossocial - COPSOQ (NR-1)")

# Dados do funcionário
nome = st.text_input("Código do Funcionário (ou Nome)")
email = st.text_input("E-mail (opcional)")
empresa = st.text_input("Empresa")

st.write("Responda o questionário:")

respostas = {}

# Perguntas
for q in questions:
    resp = st.slider(q["text"], 1, 5, 3)

    dim = q["dimension"]

    if dim not in respostas:
        respostas[dim] = []

    respostas[dim].append(resp)

# Botão enviar
if st.button("Enviar Respostas"):

    if not nome or not empresa:
        st.warning("Preencha o Código/Nome e Empresa")
    else:
        resultado = calcular(respostas)

        data = {
            "nome": nome,
            "email": email,
            "empresa": empresa,
            "resultado": resultado
        }

        try:
            url = "https://script.google.com/macros/s/AKfycbxHnnGxmDSWCO1GyI3ilRm1B7XfcLcGBlg-iSSKbJR92zeyT2KCQDcLQgBA45SS5wIo5g/exec"

            response = requests.post(
                url,
                data={"data": json.dumps(data)}
            )

            if response.status_code == 200:
                st.success("✅ Resposta enviada com sucesso! Obrigado pela participação.")
            else:
                st.error(f"Erro ao enviar. Código: {response.status_code}")

        except Exception as e:
            st.error(f"Erro de conexão: {e}")
            st.divider()
st.subheader("📊 Relatório da Empresa (PGR)")

empresa_relatorio = st.text_input("Nome da empresa para o relatório")

if st.button("Gerar Relatório da Empresa"):

    if not empresa_relatorio:
        st.warning("Informe o nome da empresa")
    else:
        try:
            # 📥 IMPORTANTE:
            # Aqui você deve usar um CSV exportado da sua planilha Google
            # Nome da coluna deve ser: Resultado

            df = pd.read_csv("dados_exportados.csv")

            # 🧠 Calcular médias por dimensão
            resultados = calcular_empresa(df)

            # 📊 Gerar gráfico
            gerar_grafico(resultados)

            # 📄 Gerar PDF
            gerar_pdf(resultados, empresa_relatorio)

            # 📥 Download
            with open("relatorio_pgr.pdf", "rb") as file:
                st.success("✅ Relatório gerado com sucesso!")
                st.download_button(
                    label="📄 Baixar Relatório em PDF",
                    data=file,
                    file_name=f"relatorio_{empresa_relatorio}.pdf",
                    mime="application/pdf"
                )

        except Exception as e:
            st.error(f"Erro ao gerar relatório: {e}")
