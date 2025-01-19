from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('torneo.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

# Ruta para la página de estadísticas
@app.route('/estadisticas')
def estadisticas():
    # Actualizar consulta para usar la tabla "equipos2"
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM equipos2 ORDER BY puntos DESC")
    equipos = cursor.fetchall()
    cursor.close()

    return render_template('estadisticas.html', equipos=equipos)

# Ruta para agregar un equipo
@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        # Obtener el nombre del equipo del formulario
        nombre_equipo = request.form['nombre']
        if nombre_equipo:
            # Insertar un nuevo equipo en la tabla "equipos2"
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO equipos2 (nombre, juegos_jugados, juegos_ganados, juegos_empatados, juegos_perdidos, goles_a_favor, goles_en_contra, diferencia_goles, puntos)
                VALUES (?, 0, 0, 0, 0, 0, 0, 0, 0)
            """, (nombre_equipo,))
            conn.commit()
            cursor.close()

    return render_template('admin.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render asignará dinámicamente el puerto
    app.run(host="0.0.0.0", port=port)