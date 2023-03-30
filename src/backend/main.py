from flask import Flask, render_template, request, redirect, url_for, flash
import pydobot
import db as db
from models.coordenadas import Coordenadas
import json


app = Flask(__name__, template_folder='../frontend/templates')

@app.route('/')
def index():
    db
    ultimo_dado = db.session.query(Coordenadas).order_by(Coordenadas.id.desc()).first()
    lista_dados = ultimo_dado.lista_dados()
    
    return render_template('index.html', x=lista_dados[0], y=lista_dados[1], z=lista_dados[2], r=lista_dados[3]) 

@app.route('/simulation')
def simulation():
    db
    ultimo_dado = db.session.query(Coordenadas).order_by(Coordenadas.id.desc()).first()
    lista_dados = ultimo_dado.lista_dados()
    jsons = {"x" : lista_dados[0], "y": lista_dados[1], "z": lista_dados[2], "r": lista_dados[3]}
    
    return json.dumps(jsons)

@app.route('/move_robot', methods=['POST'])
def move_robot():
    x = request.form['x']
    y = request.form['y']
    z = request.form['z']
    r = request.form['r']
    
        
    db
    coordenadas = Coordenadas(x=int(x), y=int(y), z=int(z), r=int(r))
    db.session.add(coordenadas)
    db.session.commit()
    print('Dados inseridos com sucesso.')

    return redirect(url_for('index'))

    
if __name__ == "__main__":
    app.run(debug=True)