import tkinter as tk
from tkinter.font import Font
from tkinter import messagebox
from random import choice

numeros_usados = []
numeros = [n for n in range(101)]

# Função que ira gerar os números e atualizar a label onde ficara o numero
def gerar_numero(label):
    global numeros
    global numeros_usados

    try:
        numero_sortido = choice(numeros)
        numeros_usados.append(numero_sortido)
        numeros.remove(numero_sortido)

        # Atualiza o texto da Label para exibir o número sorteado
        atualizar_label(label,numero_sortido)
    
    except IndexError:
        messagebox.showerror('Erro','Todos os números já foram sortidos!')

def atualizar_label(label, numero):
    label.config(text=numero)


# Função para ajustar a largura e altura da janela automaticamente
def ajustar_tamanho_janela():
    janela.update_idletasks()
    largura = janela.winfo_reqwidth()
    altura = janela.winfo_reqheight()    
    janela.geometry(f"{largura+80}x{altura+20}")

# Função para centralizar a janela na tela do computador
def centralizar_tela():
    largura = 250
    altura = 160

    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight() - 100

    x = (largura_tela - largura) // 2
    y = (altura_tela - altura) // 2

    janela.geometry(f"{largura}x{altura}+{x}+{y}")


janela = tk.Tk()
janela.title('Sorteador')

fonte = Font(family="Helvetica", size=12, weight="bold")
fonte_numero = Font(family="Helvetica", size=20, weight="bold")

# Label do título
tk.Label(janela, text='Números de 0 a 100',font=fonte).pack(pady=10)

# Label onde irá aparecer o numero
label_numero_sortido = tk.Label(janela, text='', font=fonte_numero)
label_numero_sortido.pack(pady=10)

# Botão que irá gerar um número aleatório
gerar_numero_aleatorio = tk.Button(janela, text='GERAR NÚMERO', font=fonte, command=lambda: gerar_numero(label_numero_sortido))
gerar_numero_aleatorio.pack(pady=10)

ajustar_tamanho_janela()
centralizar_tela()

janela.mainloop()