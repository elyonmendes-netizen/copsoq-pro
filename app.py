import streamlit as st
from questions import questions
from scoring import calcular

st.title("Avaliação Psicossocial - COPSOQ (NR-1)")

nome = st.text_input("Nome")
email = st.text_input("E-mail")
empresa = st.text_input("Empresa")

st.write("Responda o questionário:")

respostas = {}

for q in questions:
    resp = st.slider(q["text"], 1, 5, 3)

    dim = q["dimension"]

    if dim not in respostas:
        respostas[dim] = []

    respostas[dim].append(resp)

if st.button("Gerar Resultado"):
    resultado = calcular(respostas)

    st.subheader("Resultado")

    for dim, dados in resultado.items():
        st.write(f"**{dim}**")
        st.write(f"Média: {dados['media']}")
        st.write(f"Classificação: {dados['classificacao']}")
        st.write("---")
