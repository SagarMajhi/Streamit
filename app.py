from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import requests
import os

app = Flask(__name__, static_folder='Streamit/dist', static_url_path='/')
CORS(app)

def get_movie_recommendations(api_key, media_type, media_id):
    url = f"https://api.themoviedb.org/3/{media_type}/{media_id}/recommendations"
    params = {"api_key": api_key}

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        return data.get("results", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching recommendations: {e}")
        return []

@app.route("/recommendations", methods=["GET"])
def get_recommendations():
    api_key = "539be994be3a883c3eecccb1c252f107"
    media_type = request.args.get("mediaType")
    media_id = request.args.get("id")

    recommendations = get_movie_recommendations(api_key, media_type, media_id)
    return jsonify({"results": recommendations})

@app.route("/")
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == "__main__":
    app.run(port=5500)
