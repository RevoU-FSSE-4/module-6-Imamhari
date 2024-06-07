from flask import Blueprint, jsonify, request

employee_view = Blueprint("employee_view", __name__)

employee_data = {
    "employees": [],
    "roles": [],
    "schedules": []
}

def __init__(self, name, role_id, schedule_id):
    self.name = name
    self.role_id = role_id
    self.schedule_id = schedule_id


@employee_view.route("/employees", methods=["GET"])
def get_employees():
    return jsonify({"employees": employee_data}), 200


@employee_view.route("/employees/<int:employee_id>", methods=["GET"])
def get_employee(employee_id):
    try:
        employee = employee_data[employee_id]
        return jsonify({"employee": employee}), 200
    except IndexError:
        return jsonify({"message": "Employee not found"}), 404


@employee_view.route("/employees", methods=["POST"])
def create_employee():
    data = request.get_json()
    employee = data.get("employee")
    if employee:
        employee_data.append(employee)
        return jsonify({"message": "Employee created successfully"}), 201
    else:
        return jsonify({"message": "Employee not created"}), 400


@employee_view.route("/employees/<int:employee_id>", methods=["PUT"])
def update_employee(employee_id):
    data = request.get_json()
    employee = data.get("employee")
    if employee:
        employee_data[employee_id] = employee
        return jsonify({"message": "Employee updated successfully"}), 200
    else:
        return jsonify({"message": "Employee not updated"}), 400


@employee_view.route("/employees/<int:employee_id>", methods=["DELETE"])
def delete_employee(employee_id):
    try:
        employee_data.pop(employee_id)
        return jsonify({"message": "Employee deleted successfully"}), 200
    except IndexError:
        return jsonify({"message": "Employee not found"}), 404


