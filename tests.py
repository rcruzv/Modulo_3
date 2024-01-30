import pytest
import requests

BASE_URL = 'http://127.0.0.1:5000'
tasks = []

def test_create():
    new = {
        "id": 1,
        "title": "Teste 01",
        "description": "Esse é um teste!"
    }
    
    response = requests.post(f"{BASE_URL}/task", json=new)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json

def test_getAll():
    response = requests.get(f"{BASE_URL}/tasks")
    assert response.status_code == 200
    response_json = response.json()
    assert "tasks" in response_json
    assert "total_tasks" in response_json

def test_get():
    response = requests.get(f"{BASE_URL}/task/1")
    assert response.status_code == 200
    response_json = response.json()
    assert "completed" in response_json
    assert "id" in response_json
    assert "description" in response_json
    assert "title" in response_json

def test_update():
    upt = {
        "completed": True,
        "title": "Teste 02",
        "description": "Esse é um teste de atualização!"
    }

    response = requests.put(f"{BASE_URL}/task/1", json=upt)
    assert response.status_code == 200
    response_json = response.json()
    assert "completed" in response_json
    assert "id" in response_json
    assert "description" in response_json
    assert "title" in response_json

def test_delete():
    response = requests.delete(f"{BASE_URL}/task/1")
    assert response.status_code == 200