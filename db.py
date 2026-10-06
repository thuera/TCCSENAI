import tkinter as tk
from tkinter import messagebox
import psycopg

def clique_botao():
    try:
        # Uso do bloco 'with' para fechar conexão e cursor automaticamente
        with psycopg.connect(
            host='localhost',
            dbname='cinema',
            port=5432,
            user='postgres',
            password='root'
        ) as conexao:
            with conexao.cursor() as cursor:
                # IF NOT EXISTS evita erro se o botão for clicado mais de uma vez
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS usuarios (
                        id INT PRIMARY KEY,
                        nome VARCHAR(100) NOT NULL,
                        email VARCHAR(100)  
                    );
                """)
            # Confirma (persist) as alterações no banco de dados
            conexao.commit()
            
        messagebox.showinfo("Sucesso", "Tabela 'usuarios' verificada/criada com sucesso!")

    except Exception as e:
        messagebox.showerror("Erro de Conexão/SQL", f"Ocorreu um erro:\n{e}")

# Criando a janela principal
janela = tk.Tk()
janela.title("Cinema")
janela.geometry("600x400")
janela.configure(bg="green")

# Criando o botão
botao = tk.Button(janela, 
                  text="Criar Tabela", 
                  command=clique_botao
                  )
botao.place(x=250, y=190)

# Mantendo a janela aberta
janela.mainloop()