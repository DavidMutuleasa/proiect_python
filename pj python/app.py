from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

OMDB_API_KEY = 'c9134552'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search_movies():
    query = request.form.get('query')
    year = request.form.get('year')
    api_url = f'http://www.omdbapi.com/?s={query}&y={year}&apikey={OMDB_API_KEY}'
    response = requests.get(api_url)
    data = response.json()

    if data.get('Response') == 'True':
        return render_template('search_results.html', movies=data['Search'])
    else:
        return render_template('search_results.html', movies=None)

@app.route('/movie/<movie_id>', methods=['GET'])
def movie_details(movie_id):
    api_url = f'http://www.omdbapi.com/?i={movie_id}&apikey={OMDB_API_KEY}'
    response = requests.get(api_url)
    movie = response.json()

    if movie.get('Response') == 'True':
        return render_template('movie_details.html', movie=movie)
    else:
        return render_template('error.html', message="Movie not found")

if __name__ == '__main__':
    app.run(debug=True)
