import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


def dados_origem(data):
    st.subheader("Dados de origem")
    st.dataframe(data)

def gender_agrupamento_data(data): 
    #gerando dataset de agrupamento de genero
    gender_counts = data['gender'].value_counts().rename_axis('gender').reset_index(name='counts')
    gender_counts.set_index('gender', inplace=True)
    #Gráfico do número de pessoas por gênero
    st.divider()
    st.subheader("Número de pessoas por gênero")
    st.bar_chart(gender_counts['counts'], x_label="Gêneros",y_label="Quantidade")


def exibir_agrupamento_geração(data):
    #gerando dataset de agrupamento de geração
    generation_counts = data['generation'].value_counts().rename_axis('generation').reset_index(name='counts')
    generation_counts.set_index('generation', inplace=True)
    #Gráfico do número de pessoas por geração (horizontal)
    st.divider()
    st.subheader("Número de pessoas por geração")
    st.bar_chart(generation_counts['counts'], color= "#ffaa00",x_label="Geração",y_label="Quantidade", horizontal=True)


def anos_educação_por_genero(data):
    #gerando dataset de agrupamento de média de anos de educação por gênero
    gender_education_mean = data.groupby('gender')['years_of_education'].mean().reset_index(name='means')
    gender_education_mean.set_index('gender', inplace=True)
    #histograma das faixas de idade
    st.divider()
    st.subheader("Média de anos trabalhados")
    st.bar_chart(gender_education_mean['means'], color= "#00aa00",x_label="Geração",y_label="Média de anos trabalhados")


def status_emprego(data):
    job_counts = data['employment_status'].value_counts().rename_axis('employment_status').reset_index(name='counts')
    job_counts.set_index('employment_status', inplace=True)
    #Gráfico da média de anos trabalhados
    st.divider()
    st.subheader("Distribuição do Status de Emprego")
    fig = px.pie(job_counts, values='counts', names=job_counts.index)
    st.plotly_chart(fig)


#configurando o titulo da janela
st.set_page_config(page_title="Indicadores referente ao arquivo CSV", page_icon="👁")

#abre o arquivo manualmente
file = 'persons.csv'
data = pd.read_csv(file)

#parte do código responsável pelo processamento dos dados

#renderizações no Streamlit
st.title("Indicadores referente ao arquivo CSV")




dados_origem(data)
gender_agrupamento_data(data)
exibir_agrupamento_geração(data)
anos_educação_por_genero(data)
status_emprego(data)