# ==================================================
# Bibliotecas Necessárias
# ==================================================
import pandas as pd
import streamlit as st
from PIL import Image
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


#-------------------------------------Início das Funções-----------------------------------

st.set_page_config(page_title='score_clientes', page_icon='📈', layout='wide') 

# ==================================================
# 
# Import Dataset
# ==================================================
df=pd.read_csv('clientes.csv')

# ==================================================
# Logo
# ==================================================
image=Image.open('logo.png')
st.sidebar.image(image, width=350)

# ==================================================
# Layout no Streamliy
# ==================================================
with st.container():
    st.markdown('# Projeto Score de Crédito de Clientes- Dashbord')
    st.markdown('''___''')
    
    st.markdown(
        """
        ## - Análise de Score dos Clientes em um Banco
        <span style="font-size:22px;">
        Vamos verificar as informações em uma base de dados de 100.000 clientes,  verificando através do score (pontuação) se é um bom cliente ou não.<br>
        Com isso vamos poder propor uma solução para o banco se deve emprestar dinheiro, se ele vai ter crédito entre outros benefícios dentro do banco.<br>
        É importante fazer de fato uma análise de dados para que possa tirar conclusões utilizando os números como referência, sendo um passo muito importante essa análise de dados para tomadas de decisões.<br>
        O objetivo é fazer um tratamento na base de dados e criar alguns algoritmos de classificação e verificar qual deles é o melhor.<br>
        Temos algumas colunas com o tipo de informação “object”. Isso na verdade é um texto, só que os modelos de classificação não conseguem trabalhar com
        textos. Vai ser feito um tratamento nessas colunas antes de continuar com o nosso projeto.</span>
        """,unsafe_allow_html=True)
st.markdown('''___''')
   

with st.container():
    
    st.markdown("## - Visualização das Colunas")
    
    st.success(
    """
   - Um ponto importante para se observar, é que tem algumas colunas com o tipo de informação “object” como podemos vizualizar na primeira tabela. 
   Isso na verdade é um texto, só que os modelos de classificação não conseguem trabalhar com textos. (profissao, mix_credito, comportamento_pagamento e score_credito)
   
   - Então vai ser necessario fazer um tratamento nessas colunas antes de continuar com o projeto, podemos vizualizar o tratamento na segunda tabela.
   
   - Só não vai ser aplicado na coluna de score_credito que é o objetivo do projeto.
    """)

def info_all_columns(df):
    data = []
    for col in df.columns:
        data.append({
            'Coluna': col,
            'Tipo': df[col].dtype,
            'Valores únicos': df[col].nunique(),
            'Valores ausentes': df[col].isnull().sum(),
            'Valores não nulos': df[col].count()
        })
    
    info_df = pd.DataFrame(data)
    return info_df

col1, col2 = st.columns(2)

with col1:
    # Exibir informações antes da modificação
    st.markdown("### 1 - Informações das colunas antes da modificação")
    st.dataframe(info_all_columns(df), height=910, width=710)


# Copiar o DataFrame original para preservá-lo
df_original = df.copy()

# Codificar as colunas 'profissao', 'mix_credito' e 'comportamento_pagamento'
codificador = LabelEncoder()
colunas_a_codificar = ['profissao', 'mix_credito', 'comportamento_pagamento']
for coluna in colunas_a_codificar:
    if df[coluna].dtype == 'object':
        df[coluna] = codificador.fit_transform(df[coluna])

with col2:
    # Exibir informações após a modificação
    st.markdown("### 2 - Informações das colunas após a modificação")
    st.dataframe(info_all_columns(df), height=910, width=710)
    
st.markdown('''___''')
  
st.markdown("## - Treinar o Modelo")  
st.success(
""" - Escolher quais colunas vai ser utilizada para treinar o nosso modelo de classificação, que é o modelo que vai
pegar algumas das informações que temos (vamos separar em treino e teste).

- Isso quer dizer que vamos separar nossa base de dados em 2, uma base de treino, para treinar o nosso modelo para que ele
consiga fazer as previsões. E uma base de teste, que é a base que vamos utilizar para ver como está fazendo essa previsão.

- É importante fazer essa separação, porque não faz muito sentido utilizar a mesma base para treinar e para testar, pois isso pode
levar o modelo a “gravar” os resultados e acabar não fazendo uma previsão correta. Com essa separação podemos de fato verificar
quão bem o modelo prevê o score dos nossos clientes.

- y é a coluna que queremos que o modelo calcule ("score_credito")

- x vai todas as colunas que vamos usar para prever o score de credito, não vamos usar a coluna id_cliente porque ela é um numero qualquer que nao ajuda a previsao.
""" )
      
# Treinar o Modelo
x=df.drop(['score_credito', 'id_cliente'], axis=1)
y=df['score_credito']
x_treino, x_teste, y_treino, y_teste=train_test_split(x, y, test_size=0.3, random_state=1)

st.markdown('''___''')

st.markdown("## - Treinando os Modelos")

st.success(
""" - Depois de ter feito o passo para separar a base de dados em treino e teste vai ser importado 2 modelos de classificação para
treiná-los e verificar qual deles tem o melhor resultado para esse caso.

- Não quer dizer que um modelo sendo melhor nesse caso, vai ser melhor para todos os casos. Como cada projeto é
diferente eles terão resultados diferentes.

- Para esse projeto vai ser utilizado o Modelo Árvore de Decisão (RandomForestClassifier) e o Modelo Vizinhos Mais Próximos (KNeighborsClassifier).

- Depois de importar os modelos, nós vamos treinar cada uma deles utilizando a nossa base de treino. Com isso eles estarão
preparados para serem testados com a nossa base de teste e poderemos comparar o resultado entre os dois modelos.
""" )

# Treinando os Modelos
modelo_arvore=RandomForestClassifier()
modelo_knn=KNeighborsClassifier()

modelo_arvore.fit(x_treino, y_treino)
modelo_knn.fit(x_teste, y_teste)

st.markdown('''___''')


with st.container():
    
    st.markdown("## - Acurácia do Modelo")

    st.success(
      """
    - Acurácia e uma das métricas de avaliação que utilizamos para verificar se um modelo é bom em relação a outro.
      
    - A acurácia é a performance do modelo, ou seja, vai verificar quantas informações foram classificadas de forma correta.
     
    - Esse exemplo abaixo, vai fazer uma verificação de acurácia do modelo se ele tivesse “chutado” todos os scores dos clientes como
    standard. Lembrando que temos 3 tipos de score: Poor, Standard e Good. (Nessa ordem, do menor para o maior). 
    
    - Veja que a acurácia seria de 53%. Isso quer dizer que ele acertou 53% das classificações que fez. Só que se você analisar esse
    número sozinho não faz tanto sentido.
    
    - Por isso que quando trabalhamos em problemas de classificação vamos utilizar pelo menos 2 modelos para verificar qual deles
    tem o melhor resultado. E é exatamente isso que vamos fazer no próximo passo.    
    """ )

    contagem_score=df['score_credito'].value_counts()
    valor_porcent=(contagem_score['Standard']/sum(contagem_score))*100
    st.markdown(f'### Acurácia: {valor_porcent:.2f}%')
    
    st.markdown('''___''')
        
        
with st.container():

    st.markdown("## - Calculando as Previsões")
    
    st.success(
      """
      - Agora de fato vai ser calculado as previsões utilizando os modelos Árvore de Decisão e o Modelo Vizinhos Mais Próximos. 
      Para isso vamos utilizar o .predict com cada um dos modelos para fazer essa previsão.
      
      - Feita a previsão, vai ser utilizado a métrica de acurácia para verificar quanto cada um dos modelos acertou.
      
      - Como Podemos ver nos resultados abaixo, Para a Árvore de Decisão tivemos uma acurácia de 82% enquanto que para o
      modelo Modelo Vizinhos Mais Próximos tivemos 73% de acurácia.
      
      - Então para esse projeto em específico entre os dois modelos que nós temos, o modelo Árvore de Decisão teve o melhor resultado.
      podemos utilizar esse modelo para prever o score dos próximos clientes.
      
      - Claro, que não vai acertar em 100% dos casos, mas uma precisão de 82% já é um valor excelente. Com isso a empresa já conseguiria prever
      com uma boa acurácia o score dos clientes e com isso pode fazer suas decisões de forma mais eficiente.
      
      """)
     
    previsao_arvore=modelo_arvore.predict(x_teste)
    previsao_knn=modelo_knn.predict(x_teste.to_numpy())

    acuracia_arvore = accuracy_score(y_teste, previsao_arvore)*100 
    acuracia_knn = accuracy_score(y_teste, previsao_knn)*100 

    st.markdown(f'### Acurácia da Árvore de Decisão: {acuracia_arvore:.2f}%')
    st.markdown(f'### Acurácia Modelo Vizinhos Mais Próximos: {acuracia_knn:.2f}%')
    
    st.markdown('''___''')
    
    
with st.container():
    
    st.markdown("## - Características Importantes para Definir o Score")
    
    st.success(
    """
    - Além de definir qual o modelo é melhor para fazer a classificação, ainda pode ser utilizado esse mesmo modelo para verificar 
    quais as características mais importantes para definir o score de crédito. Melhorando a análise e mostrar para a empresa as 
    características mais importantes para definir o score do cliente.
    
    - Na Tatela podemos notar que as informações  **juros_empréstimo, mix_credito e divida_total,** são características bem importantes.
    elas vão ajudar bastante na hora de definir o score do cliente, mais do que as outra características.
    
    - São mais pontos a serem analisados e conversados para que a empresa consiga fazer uma melhor avaliação dos seus
    clientes, com o objetivo de minimizar os clientes com um score pobre (Poor), por exemplo.
    """)
    
    # Colunas e importância dos recursos
    colunas = list(x_teste.columns)
    importancia = pd.DataFrame(index=colunas, data=modelo_arvore.feature_importances_ * 100)

    # Adicionando título acima da coluna 'Características'
    importancia.index.name = 'Características'

    # Criando uma função para estilizar linhas específicas
    def destaque_cor(s):
        destaque = ['background-color: yellow' if s.name in ['juros_emprestimo', 'mix_credito', 'divida_total'] else '' for _ in s]
        return destaque

    # Aplicando a função de destaque de cor ao DataFrame
    importancia_styled = importancia.style.apply(destaque_cor, axis=1)

    # Exibindo a tabela com ajustes de largura e altura
    st.dataframe(importancia_styled, width=350, height=840)
    
    st.markdown('''___''')
    
st.markdown("## - Conclusão")

st.success(
"""
- Esse projeto foi muito importante para mostrar como podemos fazer tratamento e análise de dados e 
com isso, ser possível treinar dois modelos de classificação para auxiliar na previsão desses dados. 
Isso ajudaria a empresa a verificar com uma acurácia de 82% quais os clientes que possuem um bom score e 
quais as características mais importantes para definir esse score do cliente.

- Algo bem importante e que podemos propor algumas soluções, criar modelos de classificação para verificar vários tipos de informação para
diminuir prejuízos e aumentar os lucros. Nesse projeto a ideia era diminuir a quantidade de clientes com um score baixo, então
foi criado um modelo para fazer uma previsão e ainda conseguir analisar quais os pontos importantes precisamos levar em consideração para análise do score.
""")           

st.sidebar.subheader('', divider='gray')                
st.sidebar.subheader('Powered by: Jadson N Santos')
st.sidebar.subheader('Discord: jadson')
st.sidebar.subheader('Linkedin: https://www.linkedin.com/in/jadson-nascimento-santos/')
st.sidebar.subheader('GitHub: https://github.com/JadsonDS') 
st.sidebar.subheader('Portfolio de Projetos: https://jadsonds.github.io/portfolio_projetos/')