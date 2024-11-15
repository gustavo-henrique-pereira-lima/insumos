from tkinter import *
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *

# Função para criar um campo de entrada com placeholder
def criar_placeholder(entry, texto_placeholder):
    def on_focus_in(event):
        if entry.get() == texto_placeholder:
            entry.delete(0, 'end')
            entry.config(foreground='black')

    def on_focus_out(event):
        if entry.get() == '':
            entry.insert(0, texto_placeholder)
            entry.config(foreground='gray')

    entry.insert(0, texto_placeholder)
    entry.config(foreground='gray')
    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)

# Função para a tela de login (Tela 1)
def tela_login():
    janela = ttkb.Window(themename="flatly")
    janela.title("Tela 1 - Login")
    janela.geometry("400x300")
    janela.resizable(False, False)

    Label(janela, text="Seja bem vindo", font=("Arial", 16, "bold")).pack(pady=10)
    Label(janela, text="🔵", font=("Arial", 20)).pack(pady=5)

    # Campos de entrada com placeholders
    entry_usuario = ttkb.Entry(janela, bootstyle="secondary")
    entry_usuario.pack(pady=5)
    criar_placeholder(entry_usuario, "Usuário")

    entry_senha = ttkb.Entry(janela, bootstyle="secondary", show="*")
    entry_senha.pack(pady=5)
    criar_placeholder(entry_senha, "Senha")

    # Botão de login
    ttkb.Button(
        janela, text="Entrar", bootstyle=PRIMARY, width=20, command=lambda: tela_principal(janela)
    ).pack(pady=20)

    janela.mainloop()

# Função para a tela principal (Tela 2)
def tela_principal(janela_antiga):
    janela_antiga.destroy()

    janela = ttkb.Window(themename="flatly")
    janela.title("Tela 2 - Principal")
    janela.geometry("800x600")
    janela.resizable(False, False)

    # Barra superior com ícones
    barra = Frame(janela, height=40, bg="gray")
    barra.pack(fill=X)

    ttkb.Button(barra, text="≡", bootstyle=SECONDARY, width=3, command=lambda: tela_menu(janela)).pack(side=LEFT, padx=5)
    ttkb.Button(barra, text="📊", bootstyle=SECONDARY, width=3, command=lambda: tela_relatorio(janela)).pack(side=LEFT, padx=5)
    ttkb.Button(barra, text="📃", bootstyle=SECONDARY, width=3, command=lambda: tela_insumos(janela)).pack(side=LEFT, padx=5)
    ttkb.Button(barra, text="➕", bootstyle=SECONDARY, width=3, command=lambda: tela_adicionar_material(janela)).pack(side=LEFT, padx=5)
    ttkb.Button(barra, text="❗", bootstyle=SECONDARY, width=3, command=lambda: tela_alertas(janela)).pack(side=LEFT, padx=5)

    # Tabela (corpo principal da tela 2)
    colunas = ["ID", "MATERIAL", "QUANTIDADE", "VENCIMENTO", "TIPO", "CRITICIDADE"]
    tabela = ttkb.Treeview(janela, columns=colunas, show="headings", height=15, bootstyle=INFO)
    tabela.pack(fill=BOTH, expand=True)

    for coluna in colunas:
        tabela.heading(coluna, text=coluna)
        tabela.column(coluna, width=120, anchor=CENTER)

    # Exemplo de dados na tabela
    dados = [
        (1, "Material A", 10, "2024-12-01", "Tipo X", "Alta"),
        (2, "Material B", 5, "2024-11-20", "Tipo Y", "Média"),
    ]
    for dado in dados:
        tabela.insert("", END, values=dado)

    ttkb.Button(janela, text="Voltar para Login", bootstyle=INFO, command=lambda: tela_login()).pack(pady=10)

    janela.mainloop()

# Funções para outras telas (alertas, relatório, insumos, menu, adicionar material)
def tela_alertas(janela_antiga):
    janela_antiga.destroy()
    janela = ttkb.Window(themename="flatly")
    janela.title("Alertas")
    janela.geometry("400x400")
    Label(janela, text="Tela de Alertas", font=("Arial", 16)).pack(pady=10)
    ttkb.Button(janela, text="Voltar", bootstyle=INFO, command=lambda: tela_principal(janela)).pack(pady=20)
    janela.mainloop()

def tela_relatorio(janela_antiga):
    janela_antiga.destroy()
    janela = ttkb.Window(themename="flatly")
    janela.title("Relatório")
    janela.geometry("400x400")
    Label(janela, text="Relatório de Atividades", font=("Arial", 16)).pack(pady=10)
    ttkb.Button(janela, text="Voltar", bootstyle=INFO, command=lambda: tela_principal(janela)).pack(pady=20)
    janela.mainloop()

def tela_insumos(janela_antiga):
    janela_antiga.destroy()
    janela = ttkb.Window(themename="flatly")
    janela.title("Insumos em Falta")
    janela.geometry("400x400")
    Label(janela, text="Insumos em Falta", font=("Arial", 16)).pack(pady=10)
    ttkb.Button(janela, text="Voltar", bootstyle=INFO, command=lambda: tela_principal(janela)).pack(pady=20)
    janela.mainloop()

def tela_menu(janela_antiga):
    janela_antiga.destroy()
    janela = ttkb.Window(themename="flatly")
    janela.title("Menu")
    janela.geometry("400x400")
    Label(janela, text="Menu Principal", font=("Arial", 16)).pack(pady=10)
    ttkb.Button(janela, text="Voltar", bootstyle=INFO, command=lambda: tela_principal(janela)).pack(pady=20)
    janela.mainloop()

def tela_adicionar_material(janela_antiga):
    janela_antiga.destroy()
    janela = ttkb.Window(themename="flatly")
    janela.title("Adicionar Material")
    janela.geometry("400x400")
    Label(janela, text="Adicionar Material", font=("Arial", 16)).pack(pady=10)
    ttkb.Button(janela, text="Voltar", bootstyle=INFO, command=lambda: tela_principal(janela)).pack(pady=20)
    janela.mainloop()

# Iniciar aplicação com a tela de login
tela_login()

