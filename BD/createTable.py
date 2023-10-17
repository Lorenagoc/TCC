import pandas as pd
import psycopg2
from sqlalchemy import create_engine

pasta = '/home/lorena/Documentos/TCC/Scripts/Results'

dados_bibliotecas = pd.read_csv('/home/lorena/Documentos/TCC/Scripts/Results/result.txt', sep=";", header=None)

dados_bibliotecas.columns = ["Nomes", "Popularidade", "Downloads", "Frequência média de releases", "Issues abertos", "Qtde de perguntas", "Estrelas", "Última modificação", "Penúltima modificação", "Domínio"]

print(dados_bibliotecas)

# Substitua pelos seus detalhes de conexão
db_config = {
    'user': 'postgres',
    'password': 'root',
    'host': 'localhost',
    'port': '5432',  # Porta padrão do PostgreSQL
    'database': 'metrics'
}

# Crie uma conexão com o PostgreSQL
conn = psycopg2.connect(**db_config)

# Crie um motor SQLAlchemy
engine = create_engine(f'postgresql://{db_config["user"]}:{db_config["password"]}@{db_config["host"]}:{db_config["port"]}/{db_config["database"]}')

# Salve o DataFrame na tabela do PostgreSQL
dados_bibliotecas.to_sql('results', engine, if_exists='replace', index=False)

# Feche a conexão com o PostgreSQL
conn.close()