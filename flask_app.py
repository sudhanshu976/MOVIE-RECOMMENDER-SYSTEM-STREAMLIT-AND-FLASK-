import pickle
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=575822df7f5955a81b6bd090f40f4849".format(movie_id)
    data = requests.get(url).json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names, recommended_movie_posters

@app.route('/')
def home():
    return render_template('index.html', movie_list=movies['title'].values)

@app.route('/recommendations', methods=['POST'])
def recommendations():
    selected_movie = request.form.get('selected_movie')
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    return render_template('recommendations.html', selected_movie=selected_movie, recommended_movies=zip(recommended_movie_names, recommended_movie_posters))

if __name__ == '__main__':
    # Load data
    movies = pickle.load(open('models/movie_list.pkl', 'rb'))
    similarity = pickle.load(open('models/similarity.pkl', 'rb'))

    app.run(debug=True)
