import pandas as pd 
import plotly.express as px
import streamlit as st
from pathlib import Path

# Lendo os dados
car_data = pd.read_csv('Data/vehicles.csv')

st.header('Aplicação web interativa para explorar e visualizar dados de anúncios de venda de veículos.')

# Botão para histograma
hist_button = st.button('Criar histograma')

if hist_button:
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    st.subheader("Histograma do Odômetro dos Veículos")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Novo botão para gráfico de dispersão
scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:
    st.write('Criando um gráfico de dispersão: preço vs odômetro')
    fig2 = px.scatter(car_data, x="odometer", y="price", title="Preço vc Odômetro")
    st.plotly_chart(fig2, use_container_width=True)