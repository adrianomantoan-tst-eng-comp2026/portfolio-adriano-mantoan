from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tarefas = []


@app.route("/")
def home():
    pesquisa = request.args.get("pesquisa", "").strip()

    if pesquisa:
        tarefas_filtradas = [
            tarefa for tarefa in tarefas
            if pesquisa.lower() in tarefa["titulo"].lower()
            or pesquisa.lower() in tarefa["descricao"].lower()
        ]
    else:
        tarefas_filtradas = tarefas

    return render_template(
        "index.html",
        tarefas=tarefas_filtradas,
        tarefa_edicao=None,
        pesquisa=pesquisa
    )


@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    titulo = request.form.get("titulo")
    descricao = request.form.get("descricao")

    if titulo:
        tarefa = {
            "id": len(tarefas) + 1,
            "titulo": titulo,
            "descricao": descricao,
            "status": "A Fazer"
        }

        tarefas.append(tarefa)

    return redirect(url_for("home"))


@app.route("/editar/<int:id>")
def editar(id):
    tarefa_edicao = None

    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefa_edicao = tarefa
            break

    return render_template(
        "index.html",
        tarefas=tarefas,
        tarefa_edicao=tarefa_edicao,
        pesquisa=""
    )


@app.route("/atualizar/<int:id>", methods=["POST"])
def atualizar(id):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefa["titulo"] = request.form.get("titulo")
            tarefa["descricao"] = request.form.get("descricao")
            break

    return redirect(url_for("home"))


@app.route("/excluir/<int:id>")
def excluir(id):
    global tarefas

    tarefas = [tarefa for tarefa in tarefas if tarefa["id"] != id]

    return redirect(url_for("home"))


@app.route("/alterar_status/<int:id>", methods=["POST"])
def alterar_status(id):
    novo_status = request.form.get("status")

    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefa["status"] = novo_status
            break

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)