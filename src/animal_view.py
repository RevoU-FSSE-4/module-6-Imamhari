from flask import Blueprint, jsonify, request
from flasgger import swag_from
from data import animals

animal_view = Blueprint("animal_view", __name__)

def validate_animal(data):
    if "species" not in data:
        raise Exception("Species is required")
    if "gender" not in data:
        raise Exception("Gender is required")
    if "age" not in data:
        raise Exception("Age is required")
    if "type" not in data:
        raise Exception("Type is required")
    

@animal_view.route("/animals", methods=["GET"])
@swag_from("docs/get_animals.yml")
def get_animals():
    try: 
        if len(animals) == 0:
            return jsonify({"message": "No animals found"}), 404
        else:
            return jsonify({"animals": animals}), 200
    except IndexError:
        return jsonify({"message": "No animals found"}), 404
    
@animal_view.route("/animals/<int:id>", methods=["GET"])
@swag_from("docs/get_animal_byId.yml")
def get_animal_byId(id):
    try:
        target_animal = next((animal for animal in animals if animal["id"] == id), None)
        if target_animal is None:
            raise Exception (f"Animal with id {id} not found")
        return jsonify({"animal": target_animal}), 200
        
    except IndexError:
        return jsonify({"message": "Animal not found"}), 404
    
@animal_view.route("/animals", methods=["POST"])
@swag_from("docs/create_animal.yml")
def create_animal():
    try:
        data = request.get_json()
        validate_animal(data)
        new_id = len(animals) + 1
        data["id"] = new_id
        animals.append(data)
        return jsonify({"message": "Animal created successfully"}), 201
    except IndexError:
        return jsonify({"message": "Animal not created"}), 400

@animal_view.route("/animals/<int:id>", methods=["PUT"])
@swag_from("docs/update_animal.yml")
def update_animal(id):
    try:
        target_animal = next((animal for animal in animals if animal["id"] == id), None)
        data = request.get_json()
        validate_animal(data)
        if target_animal is None:
            raise Exception (f"Animal with id {id} not found")
        target_animal.update(data)
        return jsonify({"message": "Animal updated successfully"}), 200
    except IndexError:
        return jsonify({"message": "Animal not updated"}), 400
    
@animal_view.route("/animals/<int:id>", methods=["DELETE"])
@swag_from("docs/delete_animal.yml")
def delete_animal(id):
    try:
        target_animal = next((animal for animal in animals if animal["id"] == id), None)
        if target_animal is None:
            raise Exception (f"Animal with id {id} not found")
        animals.remove(target_animal)
        return jsonify({"message": "Animal deleted successfully"}), 200
    except IndexError:
        return jsonify({"message": "Animal not deleted"}), 404