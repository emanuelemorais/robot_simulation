from flask import Flask, render_template, request, redirect, url_for, flash
import pydobot
import db as db
from models.coordenadas import Coordenadas

coordenadas = Coordenadas(x=1, y=3, z=42, j1=31, j2=312, j3=312, j4=3123)
db.session.add(coordenadas)
db.session.commit()
print('ok')
    
app = Flask(__name__, template_folder='../frontend/templates')

@app.route('/')
def index():
    db
    ultimo_dado = db.session.query(Coordenadas).order_by(Coordenadas.id.desc()).first()
    lista_dados = ultimo_dado.lista_dados()
    
    return render_template('index.html', x=lista_dados[0], y=lista_dados[1], z=lista_dados[2], j1=lista_dados[3], j2=lista_dados[4], j3=lista_dados[5], j4=lista_dados[6])    

@app.route('/move_robot', methods=['POST'])
def move_robot():
    x = request.form['x']
    y = request.form['y']
    z = request.form['z']
    j1 = request.form['j1']
    j2 = request.form['j2']
    j3 = request.form['j3']
    j4 = request.form['j4']
        
    db
    coordenadas = Coordenadas(x=int(x), y=int(y), z=int(z), j1=int(j1), j2=int(j2), j3=int(j3), j4=int(j4))
    db.session.add(coordenadas)
    db.session.commit()
    print('Dados inseridos com sucesso.')

    return redirect(url_for('index'))


@app.route('/inicia_simulacao')
def inicia_simulacao():
    return 'Simulação iniciada'
    
if __name__ == "__main__":
    app.run(debug=True)