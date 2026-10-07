import psycopg


# Criação da conexão informando os dados para acesso
DB_CONFIG = {
    "dbname": "cinema",
    "user": "postgres",
    "password": "root",
    "host": "localhost",
    "port": "5432"
}


# Definição do intervalo de filas (A até M) e cadeiras (1 até 16)
filas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
cadeiras = range(1, 17)  # 1 a 16


try:
    # Conecta ao PostgreSQL
    conn = psycopg.connect(**DB_CONFIG)
    cursor = conn.cursor()

    # Criação da tabela (caso ela ainda não exista)
    # O tipo SERIAL gera o ID único automaticamente, indicando um AUTO INCREMENT,
    # subindo sozinho a cada nova entrada
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS assentos (
            id SERIAL PRIMARY KEY,
            fila CHAR(1) NOT NULL,
            numero_cadeira INT NOT NULL,
            ocupado BOOLEAN DEFAULT FALSE NOT NULL
        );
    """)

    # Query de inserção
    query_insert = "INSERT INTO assentos (fila, numero_cadeira, ocupado) VALUES (%s, %s, %s);"

    # Lista para armazenar os dados que serão inseridos
    dados_assentos = []

    for fila in filas:
        for cadeira in cadeiras:
            # Todos os assentos começam como Livres (False)
            dados_assentos.append((fila, cadeira, False))

    # Executa a inserção em lote (com um comando eu adiciono MUITAS execuções,
    # sendo que cada execução vai usar a mesma query insert,
    # variando apenas os dados por cada comando)
    cursor.executemany(query_insert, dados_assentos)

    # Salva as alterações
    conn.commit()
    print(f"Sucesso! {len(dados_assentos)} assentos foram cadastrados.")

except Exception as error:
    # SINTAXE PADRÃO DO EXCEPT
    print(f"Erro ao conectar ou operar no banco: {error}")
    conn.rollback()

finally:
    # Ao usar o FINALLY, ele executa se tiver entrado no TRY ou no EXCEPT,
    # ao final de um dos dois blocos.
    # Garante o fechamento das conexões. ISSO é importante para não ficar consumindo dados na rede
    cursor.close()
    conn.close()