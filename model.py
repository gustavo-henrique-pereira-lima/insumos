import sqlite3

class ProdutoModel:
    def connect(self):
        # Conectar ao banco de dados
        return sqlite3.connect('insumos.db')

    def listar_produtos(self):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM produtos")
        produtos = cursor.fetchall()
        conn.close()
        return produtos

    def inserir_produto(self, material, quantidade, data_de_vencimento, tipo_de_material, criticidade_do_material):
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO produtos (material, quantidade, data_de_vencimento, tipo_de_material, criticidade_do_material)
            VALUES (?, ?, ?, ?, ?)
        ''', (material, quantidade, data_de_vencimento, tipo_de_material, criticidade_do_material))
        conn.commit()
        conn.close()
