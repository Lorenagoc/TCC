import sqlite3
import os

# Nome do arquivo do banco de dados SQLite
nome_banco_de_dados = 'librariesMetrics.db'

# Conecta ao banco de dados (ele será criado se não existir)
conn = sqlite3.connect(nome_banco_de_dados)

# Cria um cursor para executar comandos SQL
cursor = conn.cursor()

# Cria uma tabela com uma coluna para o nome da biblioteca
cursor.execute('''CREATE TABLE IF NOT EXISTS metrics (
                    id INTEGER PRIMARY KEY,
                    library_name TEXT
                )''')

# Diretório onde os arquivos txt estão localizados
diretorio = '../Scripts'

# Itera pelos arquivos e inserir o nome da biblioteca na tabela de bibliotecas
for nome_arquivo in os.listdir(diretorio):
    if nome_arquivo.endswith('.txt'):
        nome_biblioteca = nome_arquivo.split(':')[0]  # Extrai o nome da biblioteca
        cursor.execute('INSERT INTO metrics (library_name) VALUES (?)', (nome_biblioteca,))

# Cria uma coluna para cada arquivo txt como colunas dinâmicas na tabela principal
cursor.execute('''
    CREATE TABLE IF NOT EXISTS libraries (
        id INTEGER PRIMARY KEY,
        library_name_id INTEGER,
        metric TEXT,
        FOREIGN KEY (library_name_id) REFERENCES metrics (id)
    )
''')

# Itera pelos arquivos novamente e inseri o conteúdo na tabela de dados
for nome_arquivo in os.listdir(diretorio):
    if nome_arquivo.endswith('.txt'):
        nome_biblioteca = nome_arquivo.split(':')[0]
        with open(os.path.join(diretorio, nome_arquivo), 'r') as arquivo:
            conteudo = arquivo.read()
            # Obtem o ID da biblioteca correspondente
            cursor.execute('SELECT id FROM metrics WHERE library_name = ?', (nome_biblioteca,))
            biblioteca_id = cursor.fetchone()[0]
            # Insere o conteúdo na tabela de dados
            cursor.execute('INSERT INTO metrics (library_name_id, metric) VALUES (?, ?)', (biblioteca_id, conteudo))

# Confirma as mudanças e fecha a conexão
conn.commit()
conn.close()
