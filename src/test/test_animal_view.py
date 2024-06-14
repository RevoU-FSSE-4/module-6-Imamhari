from flask import Flask
from animal_view import animal_view, validate_animal
import pytest, json
from unittest.mock import MagicMock

from app import app

@pytest.fixture

def client():
    with app.test_client() as client:
        yield client

def test_get_animals(client):
    response = client.get("/animals")
    assert response.status_code == 200

def test_get_animal_byId(client):
    response = client.get("/animals/1")
    assert response.status_code == 200

def test_create_animals(client):
    animal_view.service = MagicMock()
    data = {
        'species': 'Dog',
        'gender': 'Male',
        'age': '3',
        'type': 'Labrador'
    }

    response = client.data(
        "/animals",
        data = json.dumps(data),
        content_type = "appliction/json"
    )
    
    animal_view.service.create_data.assert_called_once_with(data)
    assert response.status_code == 200
    assert json.loads(response.get_data()) == data

def test_update_animal(client):
    data = {
        'species': 'Rabbit',
        'gender': 'Male',
        'age': '3',
        'type': 'Holland lop'
    }
    response = client.put("/animals/1", json=data)
    assert response.status_code == 200

def test_delete_animal(client):
    response = client.delete("/animals/1")
    assert response.status_code == 200

def test_validate_animal():
    valid_data = {
         'species': 'Rabbit',
        'gender': 'Male',
        'age': '3',
        'type': 'Holland lop'
    }
    invalid_data = {
         'species': 'Rabbit',
        'gender': 'Male',
        'age': '3',
    
    }
    assert validate_animal(valid_data) is None
    with pytest.raises(Exception):
        validate_animal(invalid_data)