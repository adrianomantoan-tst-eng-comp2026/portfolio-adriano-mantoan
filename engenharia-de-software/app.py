from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tarefas = []


@app.route("/")
def home():
    return render_template("index.html", tarefas=tarefas, tarefa_edicao=None)


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

    return render_template("index.html", tarefas=tarefas, tarefa_edicao=tarefa_edicao)


@app.route("/atualizar/<int:id>", methods=["POST"])
def atualizar(id):
    for tarefa in tarefas:
        if tarefa["id"] == id:
            tarefa["titulo"] = request.form.get("titulo")
            tarefa["descricao"] = request.form.get("descricao")
            break

@app.route("/excluir/<int:id>")
def excluir(id):
    global tarefas

    tarefas = [tarefa for tarefa in tarefas if tarefa["id"] != id]

    return redirect(url_for("home"))

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)