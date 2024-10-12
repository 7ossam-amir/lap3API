from flask import Flask,jsonify,request
app = Flask(__name__)
movies = [
    {"id": 1, "title": "Inception", "director": "Christopher Nolan", "genre": "Sci-Fi", "year": 2010},
    {"id": 2, "title": "The Matrix", "Openhimer": "Christopher Nolan", "genre": "History", "year": 2023}
]
@app.route('/')
def home():
    return "Welcome to my first api", 200

@app.route('/movies', methods=['GET'])
def get_movies():
    return jsonify(movies),200
@app.route('/find_movie/<int:movie_id>',methods = ['GET'])
def find_movie(movie_id):
    movie = next((movie for movie in movies if movie['id'] == movie_id),None)
    if movie:
        return jsonify(movie),200
    return jsonify({"error":"movie dose not exist"}),404
@app.route('/add_movie',methods = ['POST'])
def add_movie():
    new_movie = request.json
    new_movie['id'] = len(movies)+1
    movies.append(new_movie)
    return jsonify(new_movie),201
@app.route('/movie_update/<int:movie_id>', methods=['PUT'])

def movie_update(movie_id):
    movie = next((movie for movie in movies if movie['id'] == movie_id),None)
    if movie:
        u_movie = request.json
        movie.update(u_movie)
        return jsonify(movie),200
    return jsonify({"error":"movie not found"}),404
app.route('delete_movie/<int:movie_id>', methods=['DELETE'])
def delete_movie(movie_id):
    movie = next((movie for movie in movies if movie['id'] == movie_id),None)
    if movie:
        movies.remove(movie)
        return jsonify({"message":"movie deleted"})
    return jsonify({"error":"movie not found"})

if __name__ == '__main__':
    app.run(debug=True)
    