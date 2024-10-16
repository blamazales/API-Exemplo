from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
@app.route('/index', defaults={"nome": "usuário"})
@app.route('/index/<nome>/<idade>/<sexo>')

def index(nome, idade, sexo):
    dados = {"idade": idade, "sexo": sexo}
    return render_template('index.html', nome=nome, dados=dados)

@app.route('/contato')
def contato():
        return render_template('contato.html')