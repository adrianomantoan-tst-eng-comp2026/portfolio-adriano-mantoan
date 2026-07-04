import sqlite3


def conectar():
    conexao = sqlite3.connect("banco.db")
    conexao.row_factory = sqlite3.Row
    return conexao


def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'A Fazer',
            prioridade TEXT NOT NULL DEFAULT 'Média'
        )
    """)

    cursor.execute("PRAGMA table_info(tarefas)")
    colunas = [coluna[1] for coluna in cursor.fetchall()]

    if "prioridade" not in colunas:
        cursor.execute("""
            ALTER TABLE tarefas
            ADD COLUMN prioridade TEXT NOT NULL DEFAULT 'Média'
        """)

    conexao.commit()
    conexao.close()


def salvar_tarefa(titulo, descricao, prioridade):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO tarefas (titulo, descricao, status, prioridade)
        VALUES (?, ?, ?, ?)
    """, (titulo, descricao, "A Fazer", prioridade))

    conexao.commit()
    conexao.close()


def listar_tarefas(pesquisa=None):
    conexao = conectar()
    cursor = conexao.cursor()

    if pesquisa:
        cursor.execute("""
            SELECT * FROM tarefas
            WHERE titulo LIKE ? OR descricao LIKE ?
            ORDER BY
                CASE prioridade
                    WHEN 'Alta' THEN 1
                    WHEN 'Média' THEN 2
                    WHEN 'Baixa' THEN 3
                    ELSE 4
                END,
                id DESC
        """, (f"%{pesquisa}%", f"%{pesquisa}%"))
    else:
        cursor.execute("""
            SELECT * FROM tarefas
            ORDER BY
                CASE prioridade
                    WHEN 'Alta' THEN 1
                    WHEN 'Média' THEN 2
                    WHEN 'Baixa' THEN 3
                    ELSE 4
                END,
                id DESC
        """)

    tarefas = cursor.fetchall()
    conexao.close()
    return tarefas


def buscar_tarefa(id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM tarefas WHERE id = ?", (id,))
    tarefa = cursor.fetchone()

    conexao.close()
    return tarefa


def atualizar_tarefa(id, titulo, descricao, prioridade):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE tarefas
        SET titulo = ?, descricao = ?, prioridade = ?
        WHERE id = ?
    """, (titulo, descricao, prioridade, id))

    conexao.commit()
    conexao.close()


def excluir_tarefa(id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM tarefas WHERE id = ?", (id,))

    conexao.commit()
    conexao.close()


def alterar_status(id, status):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE tarefas
        SET status = ?
        WHERE id = ?
    """, (status, id))

    conexao.commit()
    conexao.close()


def contar_tarefas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("SELECT COUNT(*) FROM tarefas")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM tarefas WHERE status = 'A Fazer'")
    a_fazer = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM tarefas WHERE status = 'Em Andamento'")
    em_andamento = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM tarefas WHERE status = 'Concluída'")
    concluidas = cursor.fetchone()[0]

    conexao.close()

    return {
        "total": total,
        "a_fazer": a_fazer,
        "em_andamento": em_andamento,
        "concluidas": concluidas
    }