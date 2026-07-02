from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tarefas = []


@app.route("/")
def home():
    return render_template("index.html", tarefas=tarefas)


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


if __name__ == "__main__":
    app.run(debug=True)