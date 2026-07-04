import os
import sqlite3
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import database


def setup_function():
    database.criar_tabela()

    conexao = database.conectar()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM tarefas")
    conexao.commit()
    conexao.close()


def test_criar_tabela():
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()

    cursor.execute("PRAGMA table_info(tarefas)")
    colunas = [coluna[1] for coluna in cursor.fetchall()]

    conexao.close()

    assert "prioridade" in colunas


def test_salvar_e_listar_tarefa():
    database.salvar_tarefa("Teste PyTest", "Descrição do teste", "Alta")

    tarefas = database.listar_tarefas()

    assert len(tarefas) == 1
    assert tarefas[0]["titulo"] == "Teste PyTest"
    assert tarefas[0]["descricao"] == "Descrição do teste"
    assert tarefas[0]["status"] == "A Fazer"
    assert tarefas[0]["prioridade"] == "Alta"


def test_atualizar_tarefa():
    database.salvar_tarefa("Título antigo", "Descrição antiga", "Baixa")
    tarefa = database.listar_tarefas()[0]

    database.atualizar_tarefa(tarefa["id"], "Título novo", "Descrição nova", "Média")
    tarefa_atualizada = database.buscar_tarefa(tarefa["id"])

    assert tarefa_atualizada["titulo"] == "Título novo"
    assert tarefa_atualizada["descricao"] == "Descrição nova"
    assert tarefa_atualizada["prioridade"] == "Média"


def test_alterar_status():
    database.salvar_tarefa("Tarefa status", "Teste de status", "Média")
    tarefa = database.listar_tarefas()[0]

    database.alterar_status(tarefa["id"], "Concluída")
    tarefa_atualizada = database.buscar_tarefa(tarefa["id"])

    assert tarefa_atualizada["status"] == "Concluída"


def test_excluir_tarefa():
    database.salvar_tarefa("Tarefa excluir", "Teste de exclusão", "Baixa")
    tarefa = database.listar_tarefas()[0]

    database.excluir_tarefa(tarefa["id"])

    tarefas = database.listar_tarefas()

    assert len(tarefas) == 0


def test_ordenacao_por_prioridade():
    database.salvar_tarefa("Tarefa baixa", "Prioridade baixa", "Baixa")
    database.salvar_tarefa("Tarefa alta", "Prioridade alta", "Alta")
    database.salvar_tarefa("Tarefa média", "Prioridade média", "Média")

    tarefas = database.listar_tarefas()

    assert tarefas[0]["prioridade"] == "Alta"
    assert tarefas[1]["prioridade"] == "Média"
    assert tarefas[2]["prioridade"] == "Baixa"