

"""
# Função para criar a tabela
def criar_tabela():

    # Verifica se a tabela já existe para evitar duplicações
    if hasattr(janela, "tabela"):
        return

    # Criação do Treeview para a tabela
    tabela = ttk.Treeview(janela, columns=("Coluna1", "Coluna2", "Coluna3", "Coluna4", "Coluna5", "Coluna6"), show='headings')

    # Definindo as cabeçalhos das colunas
    for col in tabela["columns"]:
        tabela.heading(col, text=col)
        tabela.column(col, width=100, anchor="center")  # Ajustando a largura e o alinhamento das colunas

    # Inserindo dados na tabela
    for i in range(10):  # 10 linhas
        tabela.insert("", "end", values=(f"Item {i+1}A", f"Item {i+1}B", f"Item {i+1}C", f"Item {i+1}D", f"Item {i+1}E", f"Item {i+1}F"))

    # Posiciona a tabela na janela
    tabela.pack(expand=True, fill='both')

    # Atribui a tabela ao frame para evitar duplicações
    janela.tabela = tabela

def abrir_popup():
    tk.messagebox.showinfo("Popup", "Este é um popup simples!")

# Chama a função para criar a tabela
criar_tabela()

"""



# Função para criar a tabela
def criar_tabela():
    # Verifica se a tabela já existe para evitar duplicações
    if hasattr(tela_interna, "tabela"):
        return

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

    # Atribui a tabela ao frame para evitar duplicações
    tela_interna.tabela = tabela

# Função para abrir um popup
def abrir_popup():
    tk.messagebox.showinfo("Popup", "Este é um popup simples!")


# Criação de uma tela interna (frame)
tela_interna = tk.Frame(janela, bg="lightgray")
tela_interna.pack(pady=20, padx=20, fill='both', expand=True)  # Preenche a tela

# Adiciona um rótulo à tela interna
rotulo = tk.Label(tela_interna, text="Bem-vindo à Tela Interna!", bg="lightgray", font=("Arial", 20))
rotulo.pack(pady=10)

# Adiciona um botão para abrir o popup
botao_popup = tk.Button(tela_interna, text="Abrir Popup", command=abrir_popup)
botao_popup.pack(pady=10)

# Adiciona um botão para criar a tabela
botao_criar_tabela = tk.Button(tela_interna, text="Criar Tabela", command=criar_tabela)
botao_criar_tabela.pack(pady=10)

# Adiciona um botão para sair da aplicação
botao_sair = tk.Button(tela_interna, text="Sair", command=janela.quit)
botao_sair.pack(pady=10)



""" 

# Função para mostrar ou esconder o Frame
def alternar_frame():
    if tela_interna.winfo_ismapped():  # Verifica se o frame está atualmente visível
        tela_interna.pack_forget()      # Esconde o frame
    else:
        tela_interna.pack(pady=20, padx=20, fill='both', expand=True)  # Mostra o frame


# Criação de um Frame que será mostrado e escondido
tela_interna = tk.Frame(janela, bg="lightblue")
tela_interna.pack(pady=20, padx=20, fill='both', expand=True)  # Preenche a tela (inicialmente mostrado)

# Adiciona um rótulo ao Frame
rotulo = tk.Label(tela_interna, text="Este é um Frame que aparece e desaparece!", bg="lightblue")
rotulo.pack(pady=10)

# Adiciona um botão para alternar a visibilidade do Frame
botao_alternar = tk.Button(janela, text="Mostrar/Ocultar Frame", command=alternar_frame)
botao_alternar.pack(pady=20)
"""