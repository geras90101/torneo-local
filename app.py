from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('torneo.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/estadisticas')
def estadisticas():
    conn = get_db_connection()
    equipos = conn.execute('SELECT * FROM equipos').fetchall()
    conn.close()
    return render_template('estadisticas.html', equipos=equipos)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        # Lógica para registrar equipos o partidos
        pass
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True)
