from app import app
from flask import render_template
from flask import request
from flask import flash
from flask import redirect

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


@app.route('/login')
def login():
      return render_template('login.html')

@app.route('/autenticar', methods=['POST'])
def autenticar():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')
    if usuario == 'admin' and senha== 'senha123':
        return "usuario: {} e senha: {}".format(usuario, senha)
    else:
        flash("Dados inválidos")
        flash("Login ou senha inválidos")
        return redirect('/login')