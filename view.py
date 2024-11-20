from tkinter import *
import tkinter as tk
from ttkbootstrap import Style, ttk
from PIL import Image, ImageTk
from model import ProdutoModel

class ProdutoView:

    def setup(self, root): 
        self.root = root
        self.root.title("Sistema de Estoque Odontologia")
        self.root.geometry("1000x700")

        #cabecalho
        cabecalho = ttk.Frame(self.root, height=100, bootstyle='secondary')
        cabecalho.pack(fill=X, expand=False)

        # Chama a função para criar a barra de navegação
        self.barra_de_navegacao()
        self.criar_tabela()
        self.listar_produtos()

    def barra_de_navegacao(self):
        # Criar a barra de navegação
        navegacao = ttk.Frame(self.root, bootstyle='light')
        navegacao.pack(fill=tk.X, pady=10)

        # Configura cada coluna para ser responsiva
        for i in range(6):
            navegacao.grid_columnconfigure(i, weight=1, uniform="group1")

        # Carregar os ícones usando o Pillow
        img_menu = Image.open("imagens/botao-de-menu.png")
        icone_menu = ImageTk.PhotoImage(img_menu)
        botao_menu = ttk.Button(navegacao, text='Menu', image=icone_menu, bootstyle='light', compound=tk.TOP)
        botao_menu.grid(column=0, row=0, padx=5, sticky="ew")

        img_relatorio = Image.open("imagens/botao_relatorio.png")
        icone_relatorio = ImageTk.PhotoImage(img_relatorio)
        botao_relatorio = ttk.Button(navegacao, text='Relatório', image=icone_relatorio, bootstyle='light', compound=tk.TOP)
        botao_relatorio.grid(column=1, row=0, padx=5, sticky="ew")

        img_add = Image.open("imagens/lista-de-protudos.png")
        icone_add = ImageTk.PhotoImage(img_add)
        botao_adicionar = ttk.Button(navegacao, text='Adicionar', image=icone_add, bootstyle='light', compound=tk.TOP)
        botao_adicionar.grid(column=2, row=0, padx=5, sticky="ew")

        img_alerta = Image.open("imagens/botao_alerta.png")
        icone_alerta = ImageTk.PhotoImage(img_alerta)
        botao_alerta = ttk.Button(navegacao, text='Alerta', image=icone_alerta, bootstyle='light', compound=tk.TOP)
        botao_alerta.grid(column=3, row=0, padx=5, sticky="ew")

        # Campo de busca centralizado com o texto "Pesquisa"
        busca = ttk.Entry(navegacao, width=30, bootstyle="light")
        busca.grid(column=4, row=0, padx=5, sticky="ew")
        busca.insert(0, "Pesquisa")  # Adiciona o texto "Pesquisa" no campo

        # Função para limpar o texto de pesquisa ao clicar
        def on_click(event):
            if busca.get() == "Pesquisa":
                busca.delete(0, "end")  # Limpa o campo ao clicar

        # Associa o evento de clique à função on_click
        busca.bind("<FocusIn>", on_click)

        # Botão de notificação à direita (estilo light)
        img_notifc = Image.open("imagens/botao_notificacao.png")
        icone_notific = ImageTk.PhotoImage(img_notifc)
        botao_notificacao = ttk.Button(navegacao, text='Notificação', image=icone_notific, bootstyle='light', compound=tk.TOP)
        botao_notificacao.grid(column=5, row=0, padx=5, sticky="ew")

        # Configura a coluna central para expandir conforme o redimensionamento da janela
        navegacao.grid_columnconfigure(4, weight=2)  # Campo de busca terá mais espaço

    def criar_tabela(self):
        # Cria a tabela para listar os produtos
        tela_interna = ttk.Frame(self.root, bootstyle='light')
        tela_interna.pack(pady=20, padx=20, fill='both', expand=True)

        # Criação do Treeview para a tabela
        self.tabela = ttk.Treeview(tela_interna, columns=("ID", "Material", "Quantidade", "Data de Vencimento", "Tipo de Material", "Criticidade"), show='headings')

        # Definindo os cabeçalhos das colunas
        for col in self.tabela["columns"]:
            self.tabela.heading(col, text=col)
            self.tabela.column(col, width=150, anchor="center")

        # Exibe a tabela na tela
        self.tabela.pack(expand=True, fill='both')

    def listar_produtos(self):
        # Buscar os produtos no Model
        produtos = self.model.listar_produtos()

        # Exibir os dados na tabela
        self.display_produtos(produtos)

    def display_produtos(self, produtos):
        # Limpar dados anteriores
        for row in self.tabela.get_children():
            self.tabela.delete(row)

        # Inserir novos dados na tabela
        for produto in produtos:
            self.tabela.insert("", "end", values=produto)