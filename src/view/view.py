from tkinter import * 
import tkinter as tk

from PIL import Image, ImageTk

#import customtkinter as ctk

from ttkbootstrap import *
import ttkbootstrap as ttkb
from ttkbootstrap.tableview import Tableview

# Criação da janela principal
janela = Tk()
janela.title("Sistema de Estoque Odontologia")
janela.geometry("700x500")  # Define o tamanho inicial da janela
janela.config(bg='white')
janela.minsize(width=900, height=700)

###################### SOFTWARE #######################


# Cabeçalho
cabecalho = ttkb.Frame(janela, height=100, bootstyle='secondary').pack(fill=tk.X,  expand=False)

# Barra de navegaçao com 4 botoes a esquerda, uma barra de pesquisa e um botao a direita

navegacao = Frame(janela)
navegacao.pack()

img_menu = Image.open("src/view/imagens/botao-de-menu.png")
icone_menu = ImageTk.PhotoImage(img_menu)
botao_menu = ttkb.Button(navegacao, text='Clique aqui', image=icone_menu, bootstyle='light').grid(column=0, row=0)

img_relatorio = Image.open("src/view/imagens/botao_relatorio.png")
icone_relatorio = ImageTk.PhotoImage(img_relatorio)
botao_relatorio = ttkb.Button(navegacao, text='Clique aqui', image=icone_relatorio, bootstyle='light').grid(column=1, row=0)

img_add = Image.open("src/view/imagens/lista-de-protudos.png")
icone_add = ImageTk.PhotoImage(img_add)
botao_adicionar = ttkb.Button(navegacao, text='Clique aqui', image=icone_add,bootstyle='light').grid(column=2, row=0)

img_alerta = Image.open("src/view/imagens/botao_alerta.png")
icone_alerta = ImageTk.PhotoImage(img_alerta)
botao_alerta = ttkb.Button(navegacao, text='Clique aqui', image=icone_alerta,bootstyle='light').grid(column=3, row=0)

busca = ttk.Entry(navegacao, text='busque aqui').grid(column=5, row=0)

img_notifc = Image.open("src/view/imagens/botao_notificacao.png")
icone_notific = ImageTk.PhotoImage(img_notifc)
botao_notificacao = ttkb.Button(navegacao, text='Clique aqui', image=icone_notific,bootstyle='light').grid(column=6, row=0)

# Tabela para listar os itens

tela_interna = tk.Frame(janela, bg="")
tela_interna.pack(pady=20, padx=20, fill='both', expand=True)  # Preenche a tela

    # Criação do Treeview para a tabela
tabela = ttk.Treeview(tela_interna, columns=("Coluna1", "Coluna2", "Coluna3", "Coluna4", "Coluna5", "Coluna6"), show='headings')

    # Definindo os cabeçalhos das colunas
for col in tabela["columns"]:
    tabela.heading(col, text=col)
    tabela.column(col, width=100, anchor="center")  # Ajustando a largura e o alinhamento das colunas

    # Inserindo dados na tabela
for i in range(10):  # 10 linhas
    tabela.insert("", "end", values=(f"Item {i+1}A", f"Item {i+1}B", f"Item {i+1}C", f"Item {i+1}D", f"Item {i+1}E", f"Item {i+1}F"))

    # Posiciona a tabela na tela interna
tabela.pack(expand=True, fill='both')


##################### Fechar janela ###################

# Iniciar o loop principal
janela.mainloop()