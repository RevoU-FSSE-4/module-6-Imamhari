from flask import Flask, jsonify
from animal_view import animal_view



app = Flask(__name__)
app.register_blueprint(animal_view)

animals_data = {
    "animal_information": [],
    "enclosures": [],
    "feeding_schedules": []}

employee_data = {
    "employees": [],
    "roles": [],
    "schedules": []
}

@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"erorr": "Route not found"}), 404


 

#employee class
class Employee:
    def __init__(self, name, role_id, schedule_id):
        self.name = name
        self.role_id = role_id
        self.schedule_id = schedule_id

if __name__ == "__main__":
    app.run(debug=True)