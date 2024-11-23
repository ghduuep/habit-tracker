import tkinter as tk
from database import inserir_habito, listar_habitos

janela = tk.Tk()

def salvar_habito():
	nome = entrada_nome.get()
	frequencia = entrada_frequencia.get()
	meta = entrada_meta.get()

	inserir_habito(nome, frequencia, meta)
	listar_habitos()

janela.title("Habit Tracker")
tk.Label(janela, text="Nome do hábito").pack()
entrada_nome = tk.Entry(janela)
entrada_nome.pack()

tk.Label(janela, text="Frequência:").pack()
entrada_frequencia = tk.Entry(janela)
entrada_frequencia.pack()

tk.Label(janela, text="Meta Diária:").pack()
entrada_meta = tk.Entry(janela)
entrada_meta.pack()

tk.Button(janela, text="Salvar Hábito", command=salvar_habito).pack()

label_status = tk.Label(janela, text="")
label_status.pack()

janela.mainloop()