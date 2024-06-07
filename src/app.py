from flask import Flask, jsonify
from animal_view import animal_view



app = Flask(__name__)
app.register_blueprint(animal_view)




@app.route("/")
def index():
    return "Welcome to the zoo!"


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"erorr": "Route not found"}), 404



if __name__ == "__main__":
    app.run(debug=True)