import customtkinter as ctk
from PIL import Image

#AQUI ESTOU CRIANDO CONSTANTES PARA DEFINIR QUANTAS FILEIRAS E COLUNAS TEREMOS
#É UMA BOA PRÁTICA SEMPRE QUE FORMOS CRIAR VARIÁVEIS QUE NÃO MUDAM, OU SEJA, CONSTANTES,
#criarmos o nome da variável com LETRA MAIÚSCULA
FILEIRAS = 5
COLUNAS = 10


# Funções de Navegação
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


def botao_pra_adicionar_algo():
    # Verifica se "algo_novo" está aparecendo na tela.
    if algo_novo.winfo_ismapped():
        # Se estiver aparecendo, remove.
        algo_novo.place_forget()
    else:
        # Se não estiver aparecendo, adiciona.
        algo_novo.place(x=370, y=200)


# --------------------------------------------------
# CONFIGURAÇÃO DO APP PRINCIPAL
# --------------------------------------------------

app = ctk.CTk()

app.title("Gerenciador de Salas de Cinema")
app.geometry("800x700")


# --------------------------------------------------
# 1. TELA INICIAL
# --------------------------------------------------

frame_inicial = ctk.CTkFrame(
    app,
    fg_color="#FFD587"
)


lbl_inicial = ctk.CTkLabel(
    frame_inicial,
    text="Cinema bem Ioco",
    font=("Arial", 16, "bold"),
    fg_color="transparent"
)

lbl_inicial.pack()


btn_ir_sala1 = ctk.CTkButton(
    frame_inicial,
    text="Ir para Sala 1",
    command=mostrar_sala1
)

btn_ir_sala1.place(x=330, y=70)


btn_ir_sala2 = ctk.CTkButton(
    frame_inicial,
    text="Ir para Sala 2",
    command=mostrar_sala2
)

btn_ir_sala2.place(x=330, y=120)


btn_adicionar = ctk.CTkButton(
    frame_inicial,
    text="Adicionar algo na tela",
    command=botao_pra_adicionar_algo
)

btn_adicionar.place(x=330, y=170)


algo_novo = ctk.CTkLabel(
    frame_inicial,
    text="Bagulho novo",
    font=("Arial", 16, "bold"),
    fg_color="#13d43a"
)


# --------------------------------------------------
# 2. TELA DA SALA 1
# --------------------------------------------------

frame_sala1 = ctk.CTkFrame(
    app,
    fg_color="#45b146"
)

lbl_sala1 = ctk.CTkLabel(
    frame_sala1,
    text="A bruxa de Blair",
    font=("Arial", 16, "bold"),
    fg_color="transparent",
    text_color="black"
)
lbl_sala1.pack(pady=10)

imagem = ctk.CTkImage(
     light_image=Image.open("bruxadblair.png"),
     dark_image=Image.open("bruxadblair.png"),
     size=(300, 350)
    )

label_imagem = ctk.CTkLabel(
         frame_sala1,
        text="",
        image=imagem
    )

label_imagem.pack(pady=50)



btn_voltar_sala1 = ctk.CTkButton(
    frame_sala1,
    text="Voltar para Início",
    command=mostrar_tela_inicial
)

btn_voltar_sala1.pack(pady=100)


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
    fg_color="#dd2c2c"
)


lbl_sala2 = ctk.CTkLabel(
    frame_sala2,
    text="Sala 2",
    font=("Arial", 16, "bold"),
    fg_color="#eef6e6",
    text_color="black"
)

lbl_sala2.pack(pady=20)


btn_voltar_sala2 = ctk.CTkButton(
    frame_sala2,
    text="Voltar para Início",
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