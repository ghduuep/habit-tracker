import sqlite3

# Criando ou conectando ao banco de dados
conexao = sqlite3.connect("habitos.db")
cursor = conexao.cursor()

# Criando a tabela de hábitos
cursor.execute("""
CREATE TABLE IF NOT EXISTS habitos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    frequencia TEXT NOT NULL,
    meta_diaria INTEGER NOT NULL
)
""")

# Criando a tabela de registros
cursor.execute("""
CREATE TABLE IF NOT EXISTS registros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data TEXT NOT NULL,
    habito_id INTEGER NOT NULL,
    status INTEGER NOT NULL,
    FOREIGN KEY(habito_id) REFERENCES habitos(id)
)
""")

# Salvando as alterações e fechando a conexão inicial
conexao.commit()
conexao.close()

def inserir_habito(nome, frequencia, meta_diaria):
    conexao = sqlite3.connect("habitos.db")
    cursor = conexao.cursor()
    cursor.execute("""
    INSERT INTO habitos (nome, frequencia, meta_diaria) VALUES (?, ?, ?)
    """, (nome, frequencia, meta_diaria))
    conexao.commit()
    conexao.close()

def inserir_registro(data, habito_id, status):
    conexao = sqlite3.connect("habitos.db")
    cursor = conexao.cursor()
    cursor.execute("""
    INSERT INTO registros (data, habito_id, status) VALUES (?, ?, ?)
    """, (data, habito_id, status))
    conexao.commit()
    conexao.close()

def listar_habitos():
    conexao = sqlite3.connect("habitos.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM habitos")
    habitos = cursor.fetchall()
    conexao.close()
    return habitos

def listar_registros():
    conexao = sqlite3.connect("habitos.db")
    cursor = conexao.cursor()
    cursor.execute("""
    SELECT registros.data, habitos.nome, registros.status
    FROM registros
    JOIN habitos ON registros.habito_id = habitos.id
    """)
    registros = cursor.fetchall()
    conexao.close()
    return registros