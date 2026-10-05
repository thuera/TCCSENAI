import customtkinter as ctk
import psycopg as pg
from PIL import Image


# ==========================================================
# CONSTANTES
# ==========================================================

# Como esses valores não mudam durante o programa,
# usamos nomes em letras maiúsculas.

FILEIRAS = 5
COLUNAS = 10


# ==========================================================
# FUNÇÕES DE NAVEGAÇÃO
# ==========================================================

def esconder_todas_as_telas():
    """
    Remove todas as telas da visualização atual.
    """

    frame_inicial.pack_forget()
    frame_sala1.pack_forget()
    frame_sala2.pack_forget()
    frame_assentos_sala1.pack_forget()


def mostrar_tela_inicial():
    esconder_todas_as_telas()

    frame_inicial.pack(
        fill="both",
        expand=True
    )


def mostrar_sala1():
    esconder_todas_as_telas()

    frame_sala1.pack(
        fill="both",
        expand=True
    )


def mostrar_sala2():
    esconder_todas_as_telas()

    frame_sala2.pack(
        fill="both",
        expand=True
    )


def mostrar_mapa_de_assentos1():
    esconder_todas_as_telas()

    frame_assentos_sala1.pack(
        fill="both",
        expand=True
    )


# ==========================================================
# FUNÇÃO PARA SELECIONAR CADEIRA
# ==========================================================

def selecionar_cadeira(codigo):
    """
    Função executada quando o usuário
    clica em uma cadeira.
    """

    print(f"Cadeira selecionada: {codigo}")


# ==========================================================
# FUNÇÃO PARA CRIAR AS CADEIRAS
# ==========================================================

def CriarMapaDeCadeiras():

    # Tamanho dos botões
    largura_btn = 45
    altura_btn = 40

    # Espaçamento entre as cadeiras
    espaco_x = 8
    espaco_y = 8

    # Percorre as fileiras
    for x in range(FILEIRAS):

        # chr(65) = A
        # chr(66) = B
        # chr(67) = C
        # etc.

        letra = chr(65 + x)

        # Calcula a posição vertical
        pos_y = 150 + x * (altura_btn + espaco_y)

        # Percorre as colunas
        for y in range(1, COLUNAS + 1):

            codigo = f"{letra}{y}"

            # Calcula a posição horizontal
            pos_x = 430 + (y - 1) * (largura_btn + espaco_x)

            botao_cadeira = ctk.CTkButton(
                frame_assentos_sala1,
                text=codigo,
                width=largura_btn,
                height=altura_btn,
                fg_color="#2FA572",
                hover_color="#1E6B4A",

                # Cada botão envia seu próprio código
                command=lambda c=codigo: selecionar_cadeira(c)
            )

            botao_cadeira.place(
                x=pos_x,
                y=pos_y
            )


# ==========================================================
# CONFIGURAÇÃO DO APP PRINCIPAL
# ==========================================================

app = ctk.CTk()

app.title("Gerenciador de Salas de Cinema")
app.geometry("1440x900")


# ==========================================================
# FONTE PERSONALIZADA
# ==========================================================

ctk.FontManager.load_font(
    "C:/Users/Aluno/Downloads/TCCSENAI-main/TCCSENAI/Runzoe-Regular.otf"
)

fc = ctk.CTkFont(
    family="Runzoe-Regular",
    size=70
)


# ==========================================================
# 1. TELA INICIAL
# ==========================================================

frame_inicial = ctk.CTkFrame(
    app,
    fg_color="#424242"
)


lbl_inicial = ctk.CTkLabel(
    frame_inicial,
    text="Cineminha fioty",
    font=fc,
    fg_color="transparent",
    text_color="white"
)

lbl_inicial.pack(pady=40)


btn_ir_sala1 = ctk.CTkButton(
    frame_inicial,
    text="Salas e Sessões",
    command=mostrar_sala1,
    font=("Arial", 15, "bold"),
    width=160,
    height=120
)

btn_ir_sala1.place(
    x=200,
    y=350
)


btn_ir_sala2 = ctk.CTkButton(
    frame_inicial,
    text="Gerenciador de caixa",
    command=mostrar_sala2,
    font=("Arial", 15, "bold"),
    width=160,
    height=120
)

btn_ir_sala2.place(
    x=1100,
    y=350
)


# ==========================================================
# 2. TELA DE SALAS E SESSÕES
# ==========================================================

frame_sala1 = ctk.CTkFrame(
    app,
    fg_color="#424242"
)


lblsala1 = ctk.CTkLabel(
    frame_sala1,
    text="Sala de sessões",
    font=("Arial", 30, "bold"),
    fg_color="transparent",
    text_color="white"
)

lblsala1.pack(pady=30)


# ==========================================================
# FILME 1 - A BRUXA DE BLAIR
# ==========================================================

titulo_filme1 = ctk.CTkLabel(
    frame_sala1,
    text="A Bruxa de Blair",
    font=("Arial", 16, "bold"),
    fg_color="transparent",
    text_color="white"
)

titulo_filme1.place(
    x=180,
    y=180
)


imagem_filme1 = ctk.CTkImage(
    light_image=Image.open(
        "C:/Users/Aluno/Downloads/TCCSENAI-main/TCCSENAI/bruxadblair.png"
    ),

    dark_image=Image.open(
        "C:/Users/Aluno/Downloads/TCCSENAI-main/TCCSENAI/bruxadblair.png"
    ),

    size=(250, 325)
)


label_filme1 = ctk.CTkLabel(
    frame_sala1,
    text="",
    image=imagem_filme1
)

label_filme1.place(
    x=125,
    y=250
)


btn_ir_para_sessao1 = ctk.CTkButton(
    frame_sala1,
    text="Mapa de assentos",

    # NÃO usamos ()
    command=mostrar_mapa_de_assentos1
)

btn_ir_para_sessao1.place(
    x=185,
    y=600
)


# ==========================================================
# FILME 2 - TRANSFORMERS
# ==========================================================

titulo_filme2 = ctk.CTkLabel(
    frame_sala1,
    text="Transformers: A era da extinção",
    font=("Arial", 16, "bold"),
    fg_color="transparent",
    text_color="white"
)

titulo_filme2.place(
    x=610,
    y=180
)


imagem_filme2 = ctk.CTkImage(
    light_image=Image.open(
        "C:/Users/Aluno/Downloads/TCCSENAI-main/TCCSENAI/transformers.png"
    ),

    dark_image=Image.open(
        "C:/Users/Aluno/Downloads/TCCSENAI-main/TCCSENAI/transformers.png"
    ),

    size=(250, 325)
)


label_filme2 = ctk.CTkLabel(
    frame_sala1,
    text="",
    image=imagem_filme2
)

label_filme2.place(
    x=605,
    y=250
)


btn_ir_para_sessao2 = ctk.CTkButton(
    frame_sala1,
    text="Mapa de assentos",
    command=mostrar_mapa_de_assentos1
)

btn_ir_para_sessao2.place(
    x=665,
    y=600
)


# ==========================================================
# FILME 3 - CORAÇÕES DE FERRO
# ==========================================================

titulo_filme3 = ctk.CTkLabel(
    frame_sala1,
    text="Corações de ferro",
    font=("Arial", 16, "bold"),
    fg_color="transparent",
    text_color="white"
)

titulo_filme3.place(
    x=1155,
    y=180
)


imagem_filme3 = ctk.CTkImage(
    light_image=Image.open(
        "C:/Users/Aluno/Downloads/TCCSENAI-main/TCCSENAI/fury.png"
    ),

    dark_image=Image.open(
        "C:/Users/Aluno/Downloads/TCCSENAI-main/TCCSENAI/fury.png"
    ),

    size=(250, 325)
)


label_filme3 = ctk.CTkLabel(
    frame_sala1,
    text="",
    image=imagem_filme3
)

label_filme3.place(
    x=1100,
    y=250
)


btn_ir_para_sessao3 = ctk.CTkButton(
    frame_sala1,
    text="Mapa de assentos",
    command=mostrar_mapa_de_assentos1
)

btn_ir_para_sessao3.place(
    x=1160,
    y=600
)


# ==========================================================
# BOTÃO VOLTAR
# ==========================================================

btn_voltar_sala1 = ctk.CTkButton(
    frame_sala1,
    text="Voltar para Início",
    command=mostrar_tela_inicial
)

btn_voltar_sala1.place(
    x=650,
    y=750
)


# ==========================================================
# MAPA DE ASSENTOS
# ==========================================================

frame_assentos_sala1 = ctk.CTkFrame(
    app,
    fg_color="#000000"
)


titulo_assentos = ctk.CTkLabel(
    frame_assentos_sala1,
    text="Selecione seu assento",
    font=("Arial", 30, "bold"),
    text_color="white"
)

titulo_assentos.pack(
    pady=30
)


# Uma representação simples da tela do cinema
lbl_tela_cinema = ctk.CTkLabel(
    frame_assentos_sala1,
    text="TELA",
    width=550,
    height=30,
    fg_color="#CCCCCC",
    text_color="black"
)

lbl_tela_cinema.place(
    x=440,
    y=90
)


# Criação das cadeiras
CriarMapaDeCadeiras()


btn_voltar_assentos = ctk.CTkButton(
    frame_assentos_sala1,
    text="Voltar para sessões",
    command=mostrar_sala1
)

btn_voltar_assentos.place(
    x=650,
    y=600
)


# ==========================================================
# 3. GERENCIADOR DE CAIXA
# ==========================================================

frame_sala2 = ctk.CTkFrame(
    app,
    fg_color="#424242"
)


lbl_sala2 = ctk.CTkLabel(
    frame_sala2,
    text="Gerenciador de caixa",
    font=("Arial", 25, "bold"),
    fg_color="transparent",
    text_color="white"
)

lbl_sala2.pack(
    pady=20
)


btn_voltar_sala2 = ctk.CTkButton(
    frame_sala2,
    text="Voltar para Início",
    fg_color="#333333",
    command=mostrar_tela_inicial
)

btn_voltar_sala2.pack(
    pady=10
)


# ==========================================================
# DEFINE QUAL TELA ABRE PRIMEIRO
# ==========================================================

mostrar_tela_inicial()


# ==========================================================
# INICIA O LOOP DO APLICATIVO
# ==========================================================

app.mainloop()