#Começo importando a biblioteca que vou usar, e dizendo que quando eu for me referir a ela,
#vou chamar de ctk
import customtkinter as ctk

#AQUI ESTOU CRIANDO CONSTANTES PARA DEFINIR QUANTAS FILEIRAS E COLUNAS TEREMOS
#É UMA BOA PRÁTICA SEMPRE QUE FORMOS CRIAR VARIÁVEIS QUE NÃO MUDAM, OU SEJA, CONSTANTES,
#criarmos o nome da variável com LETRA MAIÚSCULA
FILEIRAS = 5
COLUNAS = 10

app = ctk.CTk()  #AQUI INICIANDO A CRIACAO DA JANELA COM O NOME DE app
app.title("Gerenciamento de Cinema")  #AQUI O TITULO DA JANELA
app.geometry("800x450")  #AQUI É O TAMANHO DA JANELA

# Cria uma label, que é um espaço pra texto, e serve para indicar o Titulo do Filme
filme = ctk.CTkLabel(app, text="Filme: Vampeta, meu tesouro")
filme.pack(pady=(20, 5))  #O comando PACK manda colocar na tela. Depois vamos aprender a usar o place, que acho melhor.

# QUADRADINHO QUE VAI MOSTRAR ONDE É A TELA DO CINEMA
tela = ctk.CTkLabel(
    app,
    text="T E L A",
    fg_color="#333333",  #AQUI É O EFEITINHO NO FUNDO DE FICAR CINZA MAIS CLARINHO
)                       #Esse 333333 é o código da cor do cinzinha.

tela.pack(fill="x", padx=60, pady=20)  #AQUI O FILL X manda ele alargar o espaço todo pelo eixo X

# Container para os Assentos
frame_assentos = ctk.CTkFrame(app, fg_color="transparent")  #AQUI EU DIGO PRA CRIAR UM FRAME com fundo
                                                            #transparente, por isso o fg_color
frame_assentos.pack()  #Aqui eu mando inserir o frame na tela.

# AQUI O FILHO CHORA E A MÃE NÃO VÊ. Essa é a lógica de criação do mapa de cadeiras
for x in range(FILEIRAS):
    letra = chr(65 + x)  # Cada letra possui um numero correspondente em uma codificação que
                         # chamamos de ASCII. O numero 65 corresponde a letra A,
                         # então quando eu faço 65 mais 1, vai dar a letra B,
                         # 65 mais 2, vira letra C e assim por diante.
                         # Dessa forma, se eu tiver 10 filas, eu vou fazer o loop e definir uma letra
                         # do 65 + x, que é o numero da fila, indo até 65 mais 10
                         # e cada fila vai ganhar uma letra até a última fila, em ordem

    for y in range(1, COLUNAS + 1):
        codigo = f"{letra}{y}"  #Aqui eu monto o código de cada cadeira. A lógica é a mesma, pois tenho
                                # um for dentro do outro, eu vou executar esse segundo for por completo
                                # e a letra vai ser a mesma, pois a letra é definida na fila.
                                # Mas cada fila vai ter y colunas, mas dessa vez a coluna é numero mesmo.
                                # Para o primeiro assento vou começar em 0, eu fiz o range ir do numero de colunas
                                # mais um

        btn = ctk.CTkButton(  #Aqui eu crio um botão a cada assento criado.
            frame_assentos,
            text=codigo,
            width=45,
            height=40,
            fg_color="#2FA572",  # Verde
            hover_color="#1E6B4A",  #Hover significa quando passo o mouse em cima. Aí fica um verde escuro, entendeu, zé?
        )
        btn.grid(row=x, column=y - 1, padx=4, pady=4)  #Esse comando cria uma grade(GRID), e distribui cada elemento
                                                       #na posição x e y, que vão fazer o loop

# Execução da Janela. SEMPRE vamos ter que ter isso no final do nosso código, senão a janela não exibe
app.mainloop()