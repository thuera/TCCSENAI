"""
git clone 

cd TCCSENAI

git add .

git commit -m ""

git push

"""

#Atualizado dia 22/09
import customtkinter as ctk
from PIL import Image



#AQUI ESTOU CRIANDO CONSTANTES PARA DEFINIR QUANTAS FILEIRAS E COLUNAS TEREMOS
#É UMA BOA PRÁTICA SEMPRE QUE FORMOS CRIAR VARIÁVEIS QUE NÃO MUDAM, OU SEJA, CONSTANTES,
#criarmos o nome da variável com LETRA MAIÚSCULA
FILEIRAS = 5
COLUNAS = 10


# Funções de Navegação
def mostrar_mapa_de_cadeiras2():
     esconder_todas_as_telas()
     frame_cadeiras2.pack(fill="both", expand=1)

def mostrar_tela_inicial():
    esconder_todas_as_telas()
    frame_inicial.pack(fill="both", expand=True)


def mostrar_sala1():
    esconder_todas_as_telas()
    frame_sala1.pack(fill="both", expand=True)


def mostrar_sala2():
    esconder_todas_as_telas()
    frame_sala2.pack(fill="both", expand=True)


def esconder_todas_as_telas():
    """
    Remove todas as telas
    da visualização atual.
    """

    frame_inicial.pack_forget()
    frame_sala1.pack_forget()
    frame_sala2.pack_forget()


# --------------------------------------------------
# CONFIGURAÇÃO DO APP PRINCIPAL
# --------------------------------------------------

app = ctk.CTk()

app.title("Gerenciador de Salas de Cinema")
app.geometry("1440x900")

ctk.FontManager.load_font("C:/UsersAluno/Downloads/TCCSENAI-main/TCCSENAI/Runzoe-Regular")
fc=ctk.CTkFont(family="Runzoe-Regular", size=70)

# --------------------------------------------------
# 1. TELA INICIAL
# --------------------------------------------------

frame_inicial = ctk.CTkFrame(
    app,
    fg_color="#424242"
)


lbl_inicial = ctk.CTkLabel(
    frame_inicial,
    text="Cineminha fioty",
    font=fc,
    fg_color="transparent",
    text_color="white",
)

lbl_inicial.pack(pady=40)


btn_ir_sala1 = ctk.CTkButton(
    frame_inicial,
    text="Salas e Sessões",
    command=mostrar_sala1,
    width=160,
    height=120
)

btn_ir_sala1.place(x=200, y=350)


btn_ir_sala2 = ctk.CTkButton(
    frame_inicial,
    text="Gerenciador de caixa",
    command=mostrar_sala2,
    width=160,
    height=120
)

btn_ir_sala2.place(x=1100, y=350)


# --------------------------------------------------
# 2. TELA DA SALA 1
# --------------------------------------------------

frame_sala1 = ctk.CTkFrame(
    app,
    fg_color="#424242"
)

lbl_sala1 = ctk.CTkLabel(
    frame_sala1,
    text="A Bruxa de Blair",
    font=("Arial", 16, "bold"),
    fg_color="transparent",
    text_color="white"
)
lbl_sala1.pack(pady=20)

imagem = ctk.CTkImage(
     light_image=Image.open("C:/Users/Aluno/Downloads/TCCSENAI-main/TCCSENAI/bruxadblair.png"),
     dark_image=Image.open("C:/Users/Aluno/Downloads/TCCSENAI-main/TCCSENAI/bruxadblair.png"),
     size=(125, 175)
    )

label_imagem = ctk.CTkLabel(
         frame_sala1,
        text="",
        image=imagem
    )

label_imagem.place(x=0, y=0)



btn_voltar_sala1 = ctk.CTkButton(
    frame_sala1,
    text="Voltar para Início",
    command=mostrar_tela_inicial
)

btn_voltar_sala1.pack(pady=50)


# --------------------------------------------------
# IMAGEM DA SALA 1
# --------------------------------------------------

# Para utilizar imagens no CustomTkinter, podemos usar
# CTkImage junto com a biblioteca Pillow.

# Exemplo:
#
# from PIL import Image
#
# imagem = ctk.CTkImage(
#     light_image=Image.open("borat.png"),
#     dark_image=Image.open("borat.png"),
#     size=(300, 200)
# )
#
# label_imagem = ctk.CTkLabel(
#     frame_sala1,
#     text="",
#     image=imagem
# )
#
# label_imagem.pack(pady=20)


# --------------------------------------------------
# 3. TELA DA SALA 2
# --------------------------------------------------

frame_sala2 = ctk.CTkFrame(
    app,
    fg_color="#424242"
)


lbl_sala2 = ctk.CTkLabel(
    frame_sala2,
    text="Sala 2",
    font=("Arial", 16, "bold"),
    fg_color="transparent",
    text_color="black"
)

lbl_sala2.pack(pady=20)


btn_voltar_sala2 = ctk.CTkButton(
    frame_sala2,
    text="Voltar para Início",
    fg_color="#333333",
    command=mostrar_tela_inicial
)

btn_voltar_sala2.pack(pady=10)


# --------------------------------------------------
# DEFINE QUAL TELA ABRE PRIMEIRO
# --------------------------------------------------

mostrar_tela_inicial()

# --------------------------------------------------
# INICIA O LOOP DO APLICATIVO
# --------------------------------------------------

app.mainloop()