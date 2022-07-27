from flask import Flask, render_template
# importando de flask (biblioteca) la clas Flas (clases son con mayúscula)
from datetime import datetime
# importando datetime para dados do tipo tempo
app = Flask ('hello')
# hello es el nombre de la app
posts=[
    {
        'title': 'O meu primeiro post',
        'body' : 'Aqui é o texto do post',
        'author': 'Feulo',
        'created' : datetime(2022,7,25)
    },
    {
        'title': 'O meu segundo post',
        'body' : 'Aqui é o texto do post',
        'author': 'Danilo',
        'created' : datetime(2022,7,26)
    }
]
#post é uma lista [] com diccionario {}
@app.route('/')
# método ou funçao para criar rota para o endpoint, precisa de @
def index(): 
    return render_template('index.html', posts = posts)
    # def hello é um recurso criado dentro da rota    
@app.route('/login')
def login():
    return render_template("login.html")