from flask import Flask, jsonify, request
from datetime import datetime
from flasgger import Swagger
from animal_view import animal_view
from employee_view import employee_view


app = Flask(__name__)
swagger = Swagger(app)

app.register_blueprint(animal_view)
app.register_blueprint(employee_view)


@app.before_request
def start_timer():
    request.start_timer = datetime.now()

@app.after_request
def log_timer(response):
    end_time = datetime.now()
    request_time = (end_time - request.start_timer).total_seconds() 
    print (f"Request time: {request_time}s")
    return response


@app.route("/")
def index():
    return "Welcome to the zoo!"


@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"erorr": "Route not found"}), 404



if __name__ == "__main__":
    app.run(debug=True)