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
            status TEXT NOT NULL
        )
    """)

    conexao.commit()
    conexao.close()


def salvar_tarefa(titulo, descricao):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO tarefas
        (titulo, descricao, status)
        VALUES (?, ?, ?)
    """, (titulo, descricao, "A Fazer"))

    conexao.commit()
    conexao.close()


def listar_tarefas():
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT *
        FROM tarefas
        ORDER BY id
    """)

    tarefas = cursor.fetchall()

    conexao.close()

    return tarefas


def buscar_tarefa(id):

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        SELECT *
        FROM tarefas
        WHERE id=?
    """, (id,))

    tarefa = cursor.fetchone()

    conexao.close()

    return tarefa


def atualizar_tarefa(id, titulo, descricao):

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE tarefas
        SET titulo=?,
            descricao=?
        WHERE id=?
    """, (titulo, descricao, id))

    conexao.commit()

    conexao.close()


def excluir_tarefa(id):

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        DELETE FROM tarefas
        WHERE id=?
    """, (id,))

    conexao.commit()

    conexao.close()


def alterar_status(id, status):

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        UPDATE tarefas
        SET status=?
        WHERE id=?
    """, (status, id))

    conexao.commit()

    conexao.close()