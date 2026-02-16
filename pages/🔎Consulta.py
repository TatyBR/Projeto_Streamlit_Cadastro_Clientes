import streamlit as st
import pandas as pd

dados = pd.read_csv("clientes.csv")

st.title("🔎Consulta Clientes Cadastrados")
st.divider()

st.header("Digite o nome do cliente a ser pesquisado:")
nome = st.text_input("",key="nome_cliente")

if nome:
        pesquisa = dados[dados['nome'].str.contains(nome, case=False, na=False)]
        
        if not pesquisa.empty:
            st.write("✔️ Cliente encontrado:")
            dados_consulta = st.dataframe(pesquisa)
        else:
            st.warning("❌Nenhum cliente com esse nome. Tente novamente.")

st.divider()

st.header("Clientes Cadastrados:")
st.dataframe(dados)