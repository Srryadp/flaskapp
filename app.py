from flask import Flask, render_template, request, jsonify, redirect, url_for
import json
from books import scrape_books
from movies import obtener_url

app = Flask(__name__)

@app.route('/obtener_peliculas', methods=['GET', 'POST'])
def obtener_peliculas():
  
    if request.method == 'POST':
 
        page = request.form.get('page', 1)
        peliculas = obtener_url(page).get('results', [])
 
        return render_template('peliculas.html', peliculas=peliculas)
 
    return render_template('formulario_peliculas.html')

@app.route('/peliculas')
def peliculas():

    try:

        with open('peliculas.json', 'r') as json_file:

            peliculas = json.load(json_file)['results']

        return render_template('peliculas.html', peliculas=peliculas)

    except FileNotFoundError:

        return "No se encontraron datos de películas. Por favor, consulta primero las películas."

    except json.JSONDecodeError:

        return "Error al leer el archivo JSON. Asegúrate de que el archivo esté correctamente formateado."

@app.route('/obtener_libros', methods=['GET', 'POST'])
def obtener_libros():

    if request.method == 'POST':

        libros = scrape_books()

        with open('libros.json', 'w') as json_file:

            json.dump(libros, json_file)

        return redirect(url_for('libros')) 

    return render_template('formulario_libros.html')

@app.route('/libros')
def libros():

    try:

        with open('libros.json', 'r') as json_file:

            libros = json.load(json_file)

        return render_template('libros.html', libros=libros)

    except FileNotFoundError:

        return "No se encontraron datos de libros. Por favor, ejecuta primero el scraper."

    except json.JSONDecodeError:

        return "Error al leer el archivo JSON. Asegúrate de que el archivo esté correctamente formateado."

if __name__ == '__main__':

    app.run(debug=True)
