from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load data
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie):

    movie_index = movies[movies['title'] == movie].index[0]

    distances = sorted(
        list(enumerate(similarity[movie_index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_movies = []

    for i in distances[1:6]:
        recommended_movies.append(
            movies.iloc[i[0]].title
        )

    return recommended_movies


@app.route('/')
def home():
    return render_template(
        'index.html',
        movie_list=movies['title'].values,
        recommendations=None
    )

@app.route('/recommend', methods=['POST'])
def get_recommendation():

    selected_movie = request.form['movie']

    recommendations = recommend(selected_movie)

    return render_template(
        'index.html',
        movie_list=movies['title'].values,
        recommendations=recommendations
    )


if __name__ == "__main__":
    app.run(debug=True)
