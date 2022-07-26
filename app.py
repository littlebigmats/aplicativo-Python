from flask import Flask, render_template
# importando de flask (biblioteca) la clas Flas (clases son con mayúscula)
app = Flask ('hello')
# hello es el nombre de la app
@app.route('/')
# método ou funçao para criar rota para o endpoint, precisa de @
def hello(): 
    return 'Hello World'
    # def hello é um recurso criado dentro da rota

@app.route('/meucontato')
def meucontato():
    return render_template('index.html')
    