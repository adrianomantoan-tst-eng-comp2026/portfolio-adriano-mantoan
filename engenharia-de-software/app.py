from flask import Flask, render_template, request, redirect, url_for

from database import (
    criar_tabela,
    salvar_tarefa,
    listar_tarefas,
    buscar_tarefa,
    atualizar_tarefa,
    excluir_tarefa,
    alterar_status,
    contar_tarefas
)

app = Flask(__name__)

criar_tabela()


@app.route("/")
def home():
    pesquisa = request.args.get("pesquisa", "").strip()

    tarefas = listar_tarefas()

    if pesquisa:
        tarefas_filtradas = [
            tarefa for tarefa in tarefas
            if pesquisa.lower() in tarefa["titulo"].lower()
            or pesquisa.lower() in tarefa["descricao"].lower()
        ]
    else:
        tarefas_filtradas = tarefas

    contadores = contar_tarefas()

    return render_template(
        "index.html",
        tarefas=tarefas_filtradas,
        tarefa_edicao=None,
        pesquisa=pesquisa,
        contadores=contadores
    )


@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    titulo = request.form.get("titulo")
    descricao = request.form.get("descricao")

    if titulo:
        salvar_tarefa(titulo, descricao)

    return redirect(url_for("home"))


@app.route("/editar/<int:id>")
def editar(id):
    tarefa_edicao = buscar_tarefa(id)
    tarefas = listar_tarefas()
    contadores = contar_tarefas()

    return render_template(
        "index.html",
        tarefas=tarefas,
        tarefa_edicao=tarefa_edicao,
        pesquisa="",
        contadores=contadores
    )


@app.route("/atualizar/<int:id>", methods=["POST"])
def atualizar(id):
    titulo = request.form.get("titulo")
    descricao = request.form.get("descricao")

    atualizar_tarefa(id, titulo, descricao)

    return redirect(url_for("home"))


@app.route("/excluir/<int:id>")
def excluir(id):
    excluir_tarefa(id)

    return redirect(url_for("home"))


@app.route("/alterar_status/<int:id>", methods=["POST"])
def alterar_status_rota(id):
    novo_status = request.form.get("status")

    alterar_status(id, novo_status)

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)