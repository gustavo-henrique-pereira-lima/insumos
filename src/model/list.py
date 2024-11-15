import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('src/model/insumos.db')
cursor = conn.cursor()

# Consultar todos os registros da tabela 'produtos'
cursor.execute("SELECT * FROM produtos")

# Obter todos os resultados da consulta
registros = cursor.fetchall()

# # Exibir os registros
# for registro in registros:
#     print(registro)  # Cada 'registro' é uma tupla com os valores das colunas


################################################################################

# Consultar todos os registros da coluna 'nome' da tabela 'produtos'
# cursor.execute("SELECT id FROM produtos")
# id = cursor.fetchall()
# cursor.execute("SELECT material FROM produtos")
# material = cursor.fetchall()
# cursor.execute("SELECT quantidade FROM produtos")
# id = cursor.fetchall()
# cursor.execute("SELECT data_de_vencimento FROM produtos")
# id = cursor.fetchall()
# cursor.execute("SELECT tipo_de_material FROM produtos")
# id = cursor.fetchall()
# cursor.execute("SELECT criticidade_do_material FROM produtos")
# id = cursor.fetchall()
# Obter todos os resultados da consulta


print(registros)

# Exibir os registros
# for registro in registros:
#     print(registro[0])  # registro[0] contém o valor da coluna 'nome'


# Fechar a conexão com o banco de dados
conn.close()