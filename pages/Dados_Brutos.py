import streamlit as st
import requests
import pandas as pd

st.title("DADOS BRUTOS")

url2 = 'https://labdados.com/produtos'

response = requests.get(url2)

dados = pd.DataFrame.from_dict(response.json())

dados['Data da Compra'] = pd.to_datetime(dados['Data da Compra'], format = '%d/%m/%Y')

#Escolher colunas

with st.expander('Colunas'):
    colunas = st.multiselect('Selecione as colunas', list(dados.columns), list(dados.columns))

st.sidebar.title('Filtros')

with st.sidebar.expander('Nome do Produto'):
    produtos = st.multiselect('Selecione os produtos', dados['Produto'].unique(), dados['Produto'].unique() )
with st.sidebar.expander('Preço do Produto'):
    preco = st.slider('Selecione o preço', 0, 5000, (0, 5000))
with st.sidebar.expander('Data da Compra'):
    data_compra = st.date_input('Selecione a data', (dados['Data da Compra'].min(), dados['Data da Compra'].max()))
with st.sidebar.expander('Frete'):
    frete = st.slider("Selecione o Frete", 0 , 250, (0,250))
with st.sidebar.expander('Vendedor'):
    vendedores = st.multiselect("Selecione os vendedores", dados['Vendedor'].unique(), dados['Vendedor'].unique() )
with st.sidebar.expander('Avaliação da compra'):
    avaliacao = st.slider("Selecione a Avaliação", 1 , 5, (1, 5))
with st.sidebar.expander('Tipo do pagamento'):
    tipo_pagamento = st.multiselect("Selecione os tipos de pagamento", dados['Tipo de pagamento'].unique(), dados['Tipo de pagamento'].unique())
with st.sidebar.expander('Quantidade de parcelas'):
    qtd_parcelas = st.slider("Selecione a quantidade de parcelas", 1 , 24, (1,24))

st.dataframe(dados)
