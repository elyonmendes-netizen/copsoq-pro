import streamlit as st
import requests
from questions import questions
from scoring import calcular

st.title("Avaliação Psicossocial - COPSOQ (NR-1)")

# Dados do funcionário
nome = st.text_input("Nome ou Código")
email = st.text_input("E-mail")
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
        st.warning("Preencha pelo menos Nome/Código e Empresa")
    else:
        resultado = calcular(respostas)

        # Dados que serão enviados
        data = {
            "nome": nome,
            "email": email,
            "empresa": empresa,
            "resultado": resultado
        }

        try:
            # 🔗 SEU LINK DO GOOGLE SCRIPT
            url = "https://script.google.com/macros/s/AKfycbw3C4JjqnLpyAlI3IdCCB6e-9KSpH4rKqKHTpsUIPairOFZhrPdV0ZCrfOzjVENslZI3g/exec"

            response = requests.post(
    url,
    data={"data": str(data)}
)

            if response.status_code == 200:
                st.success("✅ Respostas enviadas com sucesso!")
            else:
                st.error("Erro ao enviar dados.")

        except:
            st.error("Erro de conexão com a planilha.")

# Mostrar resultado na tela também (opcional)
    resultado = calcular(respostas)

    st.subheader("Resultado")

    for dim, dados in resultado.items():
        st.write(f"**{dim}**")
        st.write(f"Média: {dados['media']}")
        st.write(f"Classificação: {dados['classificacao']}")
        st.write("---")
