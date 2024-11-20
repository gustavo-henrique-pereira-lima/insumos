from tkinter import *
from ttkbootstrap import Style, ttk
from model import ProdutoModel
from view import ProdutoView
from controller import ProdutoController

if __name__ == "__main__":
    # Criar a janela principal
    style = Style(theme='flatly')
    janela = style.master

    # Criar instâncias do Model, View e Controller
    model = ProdutoModel()
    view = ProdutoView()
    controller = ProdutoController()

    # Conectar o Controller ao Model e View
    controller.conectar(model, view)

    # Configurar a interface e exibir
    view.setup(janela)

    # Iniciar o loop principal do Tkinter
    janela.mainloop()
