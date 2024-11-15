
import sqlite3

# Conectar ao banco de dados (será criado automaticamente se não existir)
conn = sqlite3.connect('src/model/insumos.db')  # Nome do banco de dados
cursor = conn.cursor()

# Criando a tabela 'clientes'
cursor.execute('''
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    material TEXT NOT NULL,
    quantidade INTEGER NOT NULL,
    data_de_vencimento TEXT NOT NULL,
    tipo_de_material TEXT NOT NULL,
    criticidade_do_material TEXT NOT NULL
)
''')


# LISTAR

# Consultando os dados da tabela 'clientes'
cursor.execute('SELECT * FROM produtos')

tabela_produtos = cursor.fetchall()

# # Imprimindo os resultados
for row in cursor.fetchall():
    print(row)

#print(tabela_produtos)


# INSERIR

# ATUALIZAR

# DELETAR


# Fechar a conexão com o banco de dados
conn.close()
