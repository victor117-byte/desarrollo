#Programa Index
#Creador Victor Hernandez Berrios
#Iniciado el 02/08/20
# Programa que ejecutia un index exportando maquetado
#Se agrega la biblioteca flask, instalada desde pip en terminal
from flask import Flask, render_template

app = Flask(__name__)
#Se crea el directorio raiz de el sitio
@app.route('/')     #app.route agrega una ruta
def home():
    return render_template('home.html')     #se agrega el archivo html a la raiz

#Se crea una ruta about del sitio
@app.route('/about')
def about():
    return render_template('About.html')

if __name__ == '__main__':
    app.run(debug = True) #debug es el modo de prueba