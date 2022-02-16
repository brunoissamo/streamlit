import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


st.title('Dashboard de EDA')

# Personalizando o SideBar
st.sidebar.title('Menu')

#Setup do upload do arquivo
arquivo=st.sidebar.file_uploader(
    label='Selecione o arquivo csv ou excel',
    type=['csv', 'xslx']
)

if arquivo is not None:
    print(arquivo)

    try:
        df = pd.read_csv(arquivo)
        checkbox = st.sidebar.checkbox('Mostrar DataFrame')
        numeric_columns = df.select_dtypes(['float64', 'float32', 'int64', 'int32']).columns
        if checkbox:
            st.subheader('DataFrame')
            st.write('Dimensões do DataFrame: '+ str(df.shape[0]) + ' linhas e ' + str(df.shape[1]) + ' colunas')
            st.dataframe(df)
        corr = st.sidebar.checkbox('Mostrar Heatmap de correlação')
        if corr:
            st.subheader('Heatmap de correlação entre as variáveis')
            fig, ax = plt.subplots()
            sns.heatmap(df.corr())
            st.pyplot(fig)    
    except:
        df = pd.read_excel(arquivo)
        checkbox = st.sidebar.checkbox('Mostrar DataFrame')
        numeric_columns = df.select_dtypes(['float64', 'float32', 'int64', 'int32']).columns
        if checkbox:
            st.subheader('DataFrame')
            st.write('Dimensões do DataFrame: '+ str(df.shape[0]) + 'linhas e ' + str(df.shape[1]) + 'colunas')
            st.dataframe(df)
        corr = st.sidebar.checkbox('Mostrar Heatmap de correlação')
        if corr:
            st.subheader('Heatmap de correlação entre as variáveis')
            fig, ax = plt.subplots()
            sns.heatmap(df.corr())
            st.pyplot(fig)  


biblioteca = st.sidebar.selectbox('Selecione a biblioteca', ['Matplotlib', 'Seaborn', 'Plotly'])
tipo_grafico = st.sidebar.selectbox('Selecione o tipo de gráfico', ['Scatterplots', 'Lineplots', 'Barplots', 'Histogram', 'Boxplot'])

try:
    if biblioteca=='Matplotlib':
        st.write('## Matplotlib')
        if tipo_grafico == 'Scatterplots':
            st.subheader('Gráfico de Dispersão (Scatterplot)')
            st.sidebar.subheader('Configurações do Gráfico de Dispersão (Scatterplot)')
            xaxis = st.sidebar.selectbox('Selecione variável do eixo X', options=numeric_columns)
            yaxis = st.sidebar.selectbox('Selecione variável do eixo y', options=numeric_columns)

            fig, ax = plt.subplots()
            plt.scatter(data=df, x= xaxis, y=yaxis)
            plt.xlabel(xaxis)
            plt.ylabel(yaxis)

            st.pyplot(fig)

        elif tipo_grafico=='Lineplots':
            st.subheader('Gráfico de Linha')
            st.sidebar.subheader('Configurações do Gráfico de Linhas')
            xaxis = st.sidebar.selectbox('Selecione variável do eixo X', options=df.columns)
            yaxis = st.sidebar.selectbox('Selecione variável do eixo y', options=df.columns)

            fig, ax = plt.subplots()
            plt.plot(df[xaxis], df[yaxis])
            plt.xlabel(xaxis)
            plt.ylabel(yaxis)

            st.pyplot(fig)

        elif tipo_grafico=='Barplots':
            st.subheader('Gráfico de Barras')
            st.sidebar.subheader('Configurações do Gráfico de Barras')
            xaxis = st.sidebar.selectbox('Selecione variável do eixo X', options=df.columns)
            yaxis = st.sidebar.selectbox('Selecione variável do eixo y', options=numeric_columns)

            fig, ax = plt.subplots()
            plt.bar(df[xaxis], df[yaxis])
            plt.xlabel(xaxis)
            plt.ylabel(yaxis)

            st.pyplot(fig)
            
    elif biblioteca=='Plotly':
        st.write('## Plotly')
        if tipo_grafico == 'Scatterplots':
            st.subheader('Gráfico de Dispersão (Scatterplot)')
            st.sidebar.subheader('Configurações do Gráfico de Dispersão (Scatterplot)')
            xaxis = st.sidebar.selectbox('Selecione variável do eixo X', options=numeric_columns)
            yaxis = st.sidebar.selectbox('Selecione variável do eixo y', options=numeric_columns)

            plot = px.scatter(data_frame=df, x= xaxis, y=yaxis)
            st.plotly_chart(plot)
except:
    print('')

