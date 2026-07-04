import os
import sqlite3
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import database


def setup_function():
    if os.path.exists("banco.db"):
        os.remove("banco.db")
    database.criar_tabela()


def test_criar_tabela():
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT name FROM sqlite_master
        WHERE type='table' AND name='tarefas'
    """)

    tabela = cursor.fetchone()
    conexao.close()

    assert tabela is not None


def test_salvar_e_listar_tarefa():
    database.salvar_tarefa("Teste PyTest", "Descrição do teste")

    tarefas = database.listar_tarefas()

    assert len(tarefas) == 1
    assert tarefas[0]["titulo"] == "Teste PyTest"
    assert tarefas[0]["descricao"] == "Descrição do teste"
    assert tarefas[0]["status"] == "A Fazer"


def test_atualizar_tarefa():
    database.salvar_tarefa("Título antigo", "Descrição antiga")
    tarefa = database.listar_tarefas()[0]

    database.atualizar_tarefa(tarefa["id"], "Título novo", "Descrição nova")
    tarefa_atualizada = database.buscar_tarefa(tarefa["id"])

    assert tarefa_atualizada["titulo"] == "Título novo"
    assert tarefa_atualizada["descricao"] == "Descrição nova"


def test_alterar_status():
    database.salvar_tarefa("Tarefa status", "Teste de status")
    tarefa = database.listar_tarefas()[0]

    database.alterar_status(tarefa["id"], "Concluída")
    tarefa_atualizada = database.buscar_tarefa(tarefa["id"])

    assert tarefa_atualizada["status"] == "Concluída"


def test_excluir_tarefa():
    database.salvar_tarefa("Tarefa excluir", "Teste de exclusão")
    tarefa = database.listar_tarefas()[0]

    database.excluir_tarefa(tarefa["id"])

    tarefas = database.listar_tarefas()

    assert len(tarefas) == 0