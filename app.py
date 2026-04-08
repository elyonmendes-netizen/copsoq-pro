import streamlit as st
import requests
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
                data={"data": str(data)}
            )

            if response.status_code == 200:
                st.success("✅ Resposta enviada com sucesso! Obrigado pela participação.")
            else:
                st.error("Erro ao enviar. Tente novamente.")

        except:
            st.error("Erro de conexão com o servidor.")
