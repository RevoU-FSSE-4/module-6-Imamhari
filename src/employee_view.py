from flask import Blueprint, jsonify, request
from flasgger import swag_from
from data import employees

employee_view = Blueprint("employee_view", __name__)

def validate_employee(data):
    if "name" not in data:
        raise Exception("Name is required")
    if "role" not in data:
        raise Exception("Role is required")
    if "email" not in data:
        raise Exception("Email is required")
    if "schedule" not in data:
        raise Exception("Schedule is required")

@employee_view.route("/employees", methods=["GET"])
@swag_from("docs/get_employees.yml")
def get_employees():
    try:
        if len(employees) == 0:
            return jsonify ({"message": "No employees found"}), 404
        else:
            return jsonify({"employees": employees}), 200
    except IndexError:
        return jsonify({"message": "No employees found"}), 404

@employee_view.route("/employees/<int:id>", methods=["GET"])
@swag_from("docs/get_employee_byId.yml")
def get_employee_byId(id):
    try:
        target_employee = next((employee for employee in employees if employee["id"] == id), None)
        if target_employee is None:
            raise Exception (f"Employee with id {id} not found")
        return jsonify({"employee": target_employee}), 200
    except IndexError:
        return jsonify({"message": "Employee not found"}), 404

@employee_view.route("/employees", methods=["POST"])
@swag_from("docs/create_employee.yml")
def create_employee():
    try:
        data = request.get_json()
        validate_employee(data)
        new_id = len(employees) + 1
        data["id"] = new_id
        employees.append(data)
        return jsonify({"message": "Employee created successfully"}), 201
    except IndexError:
        return jsonify({"message": "Employee not created"}), 400

@employee_view.route("/employees/<int:id>", methods=["PUT"])
@swag_from("docs/update_employee.yml")
def update_employee(id):
    try:
        target_employee = next((employee for employee in employees if employee["id"] == id), None)
        data = request.get_json()
        validate_employee(data)
        if target_employee is None:
            raise Exception (f"Employee with id {id} not found")
        target_employee.update(data)
        return jsonify({"message": "Employee updated successfully"}), 200
    except IndexError:
        return jsonify({"message": "Employee not updated"}), 400

@employee_view.route("/employees/<int:id>", methods=["DELETE"])
@swag_from("docs/delete_employee.yml")
def delete_employee(id):
    try:
        target_employee = next((employee for employee in employees if employee["id"] == id), None)
        if target_employee is None:
            raise Exception (f"Employee with id {id} not found")
        employees.remove(target_employee)
        return jsonify({"message": "Employee deleted successfully"}), 200
    except IndexError:
        return jsonify({"message": "Employee not deleted"}), 404


