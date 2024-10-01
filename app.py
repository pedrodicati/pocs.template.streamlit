import streamlit as st
import pandas as pd
import time

st.set_page_config(
    page_title="Music OCR",
    page_icon="📃",
    layout="centered",
    menu_items={
        "Get Help": "https://www.linkedin.com/in/abhishek-kumar-annamraju/",
        "Report a bug": "https://www.linkedin.com/in/abhishek-kumar-annamraju/",
        "About": "# This is a simple Music OCR app that uses the power of AI to identify the music notes from the image of the music sheet. \n\n Developed by [Abhishek Kumar Annamraju](https://www.linkedin.com/in/abhishek-kumar-annamraju/)",
    },
)

st.title("📃 Music OCR")

st.write("Faça um upload de uma imagem para extrair as informações.")

uploaded_file = st.file_uploader("Escolha uma imagem...", type="jpg")

if uploaded_file:
    st.write("Processando...")

    # Processamento da imagem
    with st.spinner("Processando..."):
        time.sleep(10)
        st.success("Processamento concluído!")

    data = pd.DataFrame(
        {
            "Seguidores": 1000,
            "Não seguidores": 100,
            "Interações com stories": 50,
            "Respostas": 10,
            "Compartilhamentos": 5,
            "Cliques no link": 2,
            "Navegação": 1,
            "Avanço": 1,
            "Voltar": 1,
            "Saiu": 1,
            "Próximo story": 1,
            "Toques em figurinhas": 1,
        },
        index=[0],
    )

    st.write("Resultados:")
    st.dataframe(data)
