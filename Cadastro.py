import streamlit as st
import pandas as pd
from datetime import date

def gravar_dados(nome, sexo, cidade, estado, data_nasc, tipo, telefone):
    # nome = True, ou seja, não vazio e data_nasc "não futuro"
    if nome and cidade and data_nasc <= date.today():
        with open("clientes.csv","a",encoding="utf-8") as file:
            file.write(f"{nome},{sexo},{cidade},{estado},{data_nasc},{tipo},{telefone}\n")
        st.session_state["sucesso"] = True
    else:
        st.session_state["sucesso"] = False


st.set_page_config(
    page_title="Cadastro de clientes",
    page_icon="✍️"
)

st.title("Cadastro de clientes")
st.divider()

col1, col2 = st.columns([0.7,0.3])

nome = col1.text_input("Nome:",
                     key="nome_cliente")

sexo = col2.radio("Sexo:", ["Feminino","Masculino"], index=0)

st.write(" ")

col1, col2 = st.columns([0.8,0.2])

cidade = col1.text_input("Cidade:",
                     key="cidade_cliente")

estado = col2.selectbox("Estado:",
                   ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", 
                    "PA", "PB", "PR", "PB", "PI", "RJ", "RN", "RS", "RO", "RR","SC", "SP", "SE","TO"],
                   key="estado_cliente")

st.write(" ")

col1, col2, col3 = st.columns(3)

min_date = date(1970, 1, 1)   # mínimo permitido
max_date = date.today()       # máximo permitido (hoje)

dt_nasc = col1.date_input(
    "Data de Nascimento:",
    format="DD/MM/YYYY",
    min_value=min_date,
    max_value=max_date
)

tipo = col2.selectbox("Tipo:",
                    ["Pessoa Física", "Pessoa Jurídica"])


telefone = col3.text_input("📳Celular ((xx) xxxxx-xxxx):",
                     key="telefone_cliente")

st.write(" ")

btn_cadastrar = st.button("Cadastrar",
                          on_click = gravar_dados,
                          args=[nome,sexo,cidade,estado,dt_nasc,tipo,telefone])

if btn_cadastrar:
    if st.session_state["sucesso"]:
        st.success("Cliente cadastrado com sucesso!",
                  icon="✔️")
    else:
        st.error("Houve algum problema no cadastro!",
                 icon="❌")

