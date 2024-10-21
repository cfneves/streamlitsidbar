import streamlit as st
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

import os
import yaml
import matplotlib.pyplot as plt  # Biblioteca para gráficos
import numpy as np

# Carregar a chave da API do arquivo config.yaml
with open('config.yaml', 'r') as config_file:
    config = yaml.safe_load(config_file)
os.environ['OPENAI_API_KEY'] = config['OPENAI_API_KEY']

# Inicializar o modelo ChatOpenAI
openai = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0)

# Definir o template do prompt
template = '''
Você é um analista financeiro.
Escreva um relatório financeiro detalhado para a empresa "{empresa}" para o período {periodo}.

O relatório deve ser escrito em {idioma} e incluir a seguinte análise:
{analise}.

Certifique-se de fornecer insights e conclusões para esta seção.
Formate o relatório utilizando Markdown.
'''

prompt_template = PromptTemplate.from_template(template=template)

# Opções para os selects
empresas = ['ACME Corp', 'Globex Corporation', 'Soylent Corp', 'Initech', 'Umbrella Corporation']
trimestres = ['Q1', 'Q2', 'Q3', 'Q4']
anos = [2021, 2022, 2023, 2024]
idiomas = ['Português', 'Inglês', 'Espanhol', 'Francês', 'Alemão']
analises = [
    "Análise do Balanço Patrimonial",
    "Análise do Fluxo de Caixa",
    "Análise de Tendências",
    "Análise de Receita e Lucro",
    "Análise de Posição de Mercado"
]

# Título da aplicação
st.title('Gerador de Relatório Financeiro:')

# Criando os controles
empresa = st.sidebar.selectbox('Selecione a empresa:', empresas)
trimestre = st.sidebar.selectbox('Selecione o trimestre:', trimestres)
ano = st.sidebar.selectbox('Selecione o ano:', anos)
periodo = f"{trimestre} {ano}"
idioma = st.sidebar.selectbox('Selecione o idioma:', idiomas)
analise = st.sidebar.selectbox('Selecione a análise:', analises)

# Função para gerar um gráfico de exemplo
def gerar_grafico_exemplo():
    fig, ax = plt.subplots()
    dados = np.random.rand(10)
    ax.plot(dados, marker='o')
    ax.set_title('Exemplo de Gráfico')
    ax.set_xlabel('Eixo X')
    ax.set_ylabel('Eixo Y')
    return fig

# Botão para gerar o relatório
if st.sidebar.button('Gerar Relatório'):
    # Gerar o prompt usando o template
    prompt = prompt_template.format(
        empresa=empresa,
        periodo=periodo,
        idioma=idioma,
        analise=analise
    )

    # Fazer a chamada ao modelo OpenAI
    response = openai.predict(prompt)

    # Exibir o relatório gerado
    st.subheader('Relatório Gerado:')
    st.markdown(response)  # Usando markdown para exibir o texto formatado

    # Gerar e exibir o gráfico
    st.subheader('Gráfico Gerado:')
    fig = gerar_grafico_exemplo()
    st.pyplot(fig)
