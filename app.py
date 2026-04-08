import streamlit as st
import requests
import json
from questions import questions

st.title("Avaliação Psicossocial - COPSOQ (NR-1)")

# Dados do funcionário
nome = st.text_input("Código do Funcionário (ou Nome)")
email = st.text_input("E-mail (opcional)")
empresa = st.text_input("Empresa")

st.write("Responda o questionário:")

respostas = []

# Perguntas
for q in questions:
    resp = st.slider(q["text"], 1, 5, 3)

    respostas.append({
        "pergunta": q["text"],
        "dimensao": q["dimension"],
        "resposta": resp
    })

# Botão enviar
if st.button("Enviar Respostas"):

    if not nome or not empresa:
        st.warning("Preencha o Código/Nome e Empresa")
    else:
        data = {
            "nome": nome,
            "email": email,
            "empresa": empresa,
            "respostas": respostas
        }

        try:
            url = "https://script.google.com/macros/s/AKfycbxHnnGxmDSWCO1GyI3ilRm1B7XfcLcGBlg-iSSKbJR92zeyT2KCQDcLQgBA45SS5wIo5g/exec"

            response = requests.post(
                url,
                data={"data": json.dumps(data)}
            )

            if response.status_code == 200:
                st.success("✅ Resposta enviada com sucesso!")
            else:
                st.error(f"Erro ao enviar. Código: {response.status_code}")

        except Exception as e:
            st.error(f"Erro de conexão: {e}")
