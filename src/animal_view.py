from flask import Blueprint, jsonify, request


animal_view = Blueprint("animal_view", __name__)

animals_data = {
    "animal_information": [],
    "enclosures": [],
    "feeding_schedules": []}


def __init__(self, species, type, age, enclosure_id):
    self.species = species
    self.type = type
    self.age = age
    self.enclosure_id = enclosure_id
    
@animal_view.route("/animals", methods=["GET"])
def get_animals():
    return jsonify({"animals", animals_data}), 200

@animal_view.route("/animals", methods=["POST"])
def create_animal():
    data = request.get_json()
    animal = data.get("animal")
    if animal:
        animals_data.append(animal)
        return jsonify({"message": "Animal created successfully"}), 201
    else:
        return jsonify({"message": "Animal not created"}), 400
    
@animal_view.route("/animals/<int:animal_id>", methods=["GET"])
def get_animal(animal_id):
    try:
        animal = animals_data[animal_id]
        return jsonify({"animal": animal}), 200
    except IndexError:
        return jsonify({"message": "Animal not found"}), 404

@animal_view.route("/animals/<int:animal_id>", methods=["PUT"])
def update_animal(animal_id):
    data = request.get_json()
    animal = data.get("animal")
    if animal:
        animals_data[animal_id] = animal
        return jsonify({"message": "Animal updated successfully"}), 200
    else:
        return jsonify({"message": "Animal not updated"}), 400
    
@animal_view.route("/animals/<int:animal_id>", methods=["DELETE"])  
def delete_animal(animal_id):
    try:
        animals_data.pop(animal_id)
        return jsonify({"message": "Animal deleted successfully"}), 200
    except IndexError:
        return jsonify({"message": "Animal not found"}), 404