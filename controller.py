class ProdutoController:
    def conectar(self, model, view):
        self.model = model
        self.view = view

        # Associar a view ao controller
        self.view.listar_produtos = self.listar_produtos

    def listar_produtos(self):
        # Buscar os produtos no Model
        produtos = self.model.listar_produtos()

        # Atualizar a View com os dados dos produtos
        self.view.display_produtos(produtos)

    def inserir_produto(self, material, quantidade, data_de_vencimento, tipo_de_material, criticidade_do_material):
        # Inserir o produto no Model
        self.model.inserir_produto(material, quantidade, data_de_vencimento, tipo_de_material, criticidade_do_material)

        # Recarregar a lista de produtos
        self.listar_produtos()
