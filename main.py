import os
import sqlite3

from contextlib import closing
from flask import Flask, request, jsonify, render_template, redirect
from flask_cors import CORS

# Definir explicitamente a pasta de templates
app = Flask(__name__, template_folder=os.path.join(os.getcwd(), 'templates'))
app.config['DATABASE'] = os.path.join(app.root_path, 'escola.db')
CORS(app)

def conectar_bd():
    return sqlite3.connect(app.config['DATABASE'])

def inicializar_bd():
    with closing(conectar_bd()) as bd:
        with app.open_resource('esquema.sql', mode='r') as f:
            bd.cursor().executescript(f.read())
        bd.commit()
    
@app.route('/')
def home():
    with closing(conectar_bd()) as bd:
        cursor = bd.cursor()
        cursos = cursor.execute('SELECT id, nome, descricao FROM cursos').fetchall()
    return render_template('inicio.html', cursos=cursos)

@app.route('/cursos', methods=['POST'])
def adicionar_curso():
    nome = request.form['nome']
    descricao = request.form['descricao']
    
    with closing(conectar_bd()) as bd:
        cursor = bd.cursor()
        cursor.execute('INSERT INTO cursos (nome, descricao) VALUES (?, ?)', (nome, descricao))
        bd.commit()
    return redirect('/')

@app.route('/alunos', methods=['GET', 'POST'])
def alunos():
    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        curso_id = request.form['curso_id']
        
        with closing(conectar_bd()) as bd:
            cursor = bd.cursor()
            cursor.execute('INSERT INTO alunos (nome, idade, curso_id) VALUES (?, ?, ?)', 
                          (nome, idade, curso_id))
            bd.commit()
        return redirect('/alunos')
    
    with closing(conectar_bd()) as bd:
        cursor = bd.cursor()
        alunos = cursor.execute('''
            SELECT alunos.id, alunos.nome, alunos.idade, cursos.nome 
            FROM alunos 
            JOIN cursos ON alunos.curso_id = cursos.id
        ''').fetchall()
        
        cursos = cursor.execute('SELECT id, nome FROM cursos').fetchall()
    
    return render_template('alunos.html', alunos=alunos, cursos=cursos)

@app.route('/deletar_curso/<int:id>', methods=['POST'])
def deletar_curso(id):
    with closing(conectar_bd()) as bd:
        cursor = bd.cursor()
        # Deleta alunos associados ao curso (opcional, dependendo das regras)
        cursor.execute('DELETE FROM alunos WHERE curso_id = ?', (id,))
        # Deleta o curso
        cursor.execute('DELETE FROM cursos WHERE id = ?', (id,))
        bd.commit()
    return redirect('/')

@app.route('/deletar_aluno/<int:id>', methods=['POST'])
def deletar_aluno(id):
    with closing(conectar_bd()) as bd:
        cursor = bd.cursor()
        cursor.execute('DELETE FROM alunos WHERE id = ?', (id,))
        bd.commit()
    return redirect('/alunos')

if __name__ == '__main__':
    app.run(debug=True)