# Score Clientes
![image](https://github.com/JadsonDS/score_cliente/blob/main/logo.png)


# 1. Problema de negócio
Verificar as informações em uma base de dados de 100.000 clientes, verificando através do score (pontuação) se é um bom cliente ou não.

# 2. Premissas assumidas para a análise
  1. O objetivo é fazer um tratamento na base de dados e criar alguns algoritmos de classificação e verificar qual deles é o melhor.
  2. Escolher quais colunas vai ser utilizada para treinar o nosso modelo de classificação, que é o modelo que vai pegar algumas das informações que temos (vamos separar em treino e teste).
  3. Isso quer dizer que vamos separar nossa base de dados em 2, uma base de treino, para treinar o nosso modelo para que ele consiga fazer as previsões. E uma base de teste, que é a base que vamos utilizar para ver como está fazendo essa previsão.
  4. É importante fazer essa separação, porque não faz muito sentido utilizar a mesma base para treinar e para testar, pois isso pode levar o modelo a “gravar” os resultados e acabar não fazendo uma previsão correta.
   Com essa separação podemos de fato verificar quão bem o modelo prevê o score dos nossos clientes.
  5. y é a coluna que queremos que o modelo calcule ("score_credito")
  6. x vai todas as colunas que vamos usar para prever o score de credito, não vamos usar a coluna id_cliente porque ela é um numero qualquer que nao ajuda a previsao. 
  
# 3. Estratégia da solução
Propor uma solução para o banco se deve emprestar dinheiro, se ele vai ter crédito entre outros benefícios dentro do banco.

# 4. Principais insights 
O Resultados Para a Árvore de Decisão tivemos uma acurácia de 82% enquanto que para o modelo Modelo Vizinhos Mais Próximos tivemos 73% de acurácia.

Então para esse projeto em específico entre os dois modelos que nós temos, o modelo Árvore de Decisão teve o melhor resultado. podemos utilizar esse modelo para prever o score dos próximos clientes.

Claro, que não vai acertar em 100% dos casos, mas uma precisão de 82% já é um valor excelente. Com isso a empresa já conseguiria prever com uma boa acurácia o score dos clientes e com isso pode fazer suas decisões de forma mais eficiente.

# 5 O produto final do projeto:
Um dashboard iterativo hospedado em cloud que está disponível para acesso de qualquer dispositivo com conexão à internet. Para acessá-los basta clicar no link a seguir: https://score-cliente.streamlit.app/

# 6 Conclusão
Esse projeto foi muito importante para mostrar como podemos fazer tratamento e análise de dados e com isso, ser possível treinar dois modelos de classificação para auxiliar na previsão desses dados. 
Isso ajudaria a empresa a verificar com uma acurácia de 82% quais os clientes que possuem um bom score e quais as características mais importantes para definir esse score do cliente.

Algo bem importante e que podemos propor algumas soluções, criar modelos de classificação para verificar vários tipos de informação para diminuir prejuízos e aumentar os lucros. 
Nesse projeto a ideia era diminuir a quantidade de clientes com um score baixo, então foi criado um modelo para fazer uma previsão e ainda conseguir analisar quais os pontos importantes precisamos levar em consideração para análise do score.

# 7 Próximo passos
As informações juros_empréstimo, mix_credito e divida_total, são características bem importantes. elas vão ajudar bastante na hora de definir o score do cliente, mais do que as outras características, sendo que podemos aprofundar em 
outras informaões como idade_historico_credito e dias_atraso.




