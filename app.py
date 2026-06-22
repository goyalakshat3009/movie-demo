from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open("movie_genre_model.pkl", "rb"))
tfidf = pickle.load(open("tfidf_vectorizer.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    plot = request.form["plot"]

    vector = tfidf.transform([plot])

    prediction = model.predict(vector)[0]

    return render_template(
        "index.html",
        prediction=prediction,
        plot=plot
    )

if __name__ == "__main__":
    app.run(debug=True)