import streamlit as st
import requests
import json
from questions import questions

st.title("Avaliação Psicossocial - COPSOQ (NR-1)")

# ==============================
# DADOS DO FUNCIONÁRIO
# ==============================

nome = st.text_input("Código do Funcionário (ou Nome)")
email = st.text_input("E-mail (opcional)")
empresa = st.text_input("Empresa")

st.write("Responda o questionário:")

# ==============================
# PERGUNTAS
# ==============================

respostas = []

for q in questions:
    resp = st.slider(q["text"], 1, 5, 3)

    respostas.append({
        "pergunta": q["text"],
        "dimensao": q["dimension"],
        "resposta": resp
    })

# ==============================
# ENVIO
# ==============================

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
                json=data
            )

            if response.status_code == 200:
                st.success("✅ Resposta enviada com sucesso!")
            else:
                st.error(f"Erro ao enviar. Código: {response.status_code}")
                st.write(response.text)

        except Exception as e:
            st.error(f"Erro de conexão: {e}")
