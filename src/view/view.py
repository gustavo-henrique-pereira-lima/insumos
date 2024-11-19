from tkinter import *
from ttkbootstrap import Style, ttk
from PIL import Image, ImageTk

# Inicializa o estilo para ttkbootstrap com um tema claro
style = Style(theme='flatly')

# Criação da janela principal
janela = style.master
janela.title("Sistema de Estoque Odontologia")
janela.geometry("900x700")
janela.config(bg='white')
janela.minsize(width=900, height=700)

###################### SOFTWARE #######################

# Cabeçalho
cabecalho = ttk.Frame(janela, height=100, bootstyle='secondary')
cabecalho.pack(fill=X, expand=False)

# Barra de navegação
navegacao = ttk.Frame(janela, bootstyle='light')
navegacao.pack(fill=X, pady=10)

# Configura cada coluna para ser responsiva
for i in range(6):
    navegacao.grid_columnconfigure(i, weight=1, uniform="group1")

# Botões e imagens para a barra de navegação (estilo light)
img_menu = Image.open("src/view/imagens/botao-de-menu.png")
icone_menu = ImageTk.PhotoImage(img_menu)
botao_menu = ttk.Button(navegacao, text='Menu', image=icone_menu, bootstyle='light', compound=TOP)
botao_menu.grid(column=0, row=0, padx=5, sticky="ew")

img_relatorio = Image.open("src/view/imagens/botao_relatorio.png")
icone_relatorio = ImageTk.PhotoImage(img_relatorio)
botao_relatorio = ttk.Button(navegacao, text='Relatório', image=icone_relatorio, bootstyle='light', compound=TOP)
botao_relatorio.grid(column=1, row=0, padx=5, sticky="ew")

img_add = Image.open("src/view/imagens/lista-de-protudos.png")
icone_add = ImageTk.PhotoImage(img_add)
botao_adicionar = ttk.Button(navegacao, text='Adicionar', image=icone_add, bootstyle='light', compound=TOP)
botao_adicionar.grid(column=2, row=0, padx=5, sticky="ew")

img_alerta = Image.open("src/view/imagens/botao_alerta.png")
icone_alerta = ImageTk.PhotoImage(img_alerta)
botao_alerta = ttk.Button(navegacao, text='Alerta', image=icone_alerta, bootstyle='light', compound=TOP)
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
img_notifc = Image.open("src/view/imagens/botao_notificacao.png")
icone_notific = ImageTk.PhotoImage(img_notifc)
botao_notificacao = ttk.Button(navegacao, text='Notificação', image=icone_notific, bootstyle='light', compound=TOP)
botao_notificacao.grid(column=5, row=0, padx=5, sticky="ew")

# Configura a coluna central para expandir conforme o redimensionamento da janela
navegacao.grid_columnconfigure(4, weight=2)  # Campo de busca terá mais espaço

# Tabela para listar os itens
tela_interna = ttk.Frame(janela, bootstyle='light')
tela_interna.pack(pady=20, padx=20, fill='both', expand=True)

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

# Iniciar o loop principal
janela.mainloop()
