import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine
from app.models import Author
from datetime import datetime

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def test_create_author(setup_database):
    response = client.post("/authors/", json={
        "name": "Author Test",
        "bio": "This is a test author.",
        "birth_date": "1980-01-01"
    })
    assert response.status_code == 201
    data = response.json()
    print(data)
    assert data["name"] == "Author Test"
    assert data["bio"] == "This is a test author."
    assert data["birth_date"] == "1980-01-01"
    assert "id" in data

def test_read_authors(setup_database):
    response = client.get("/authors/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_create_author_invalid(setup_database):
    response = client.post("/authors/", json={"name": "", "bio": "No name", "birth_date": "1980-01-01"})
    assert response.status_code == 400

def test_read_author_by_id(setup_database):
    response = client.post("/authors/", json={
        "name": "Author Test",
        "bio": "This is a test author.",
        "birth_date": "1980-01-01"
    })
    author_id = response.json()["id"]

    response = client.get(f"/authors/{author_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == author_id
    assert data["name"] == "Author Test"
    assert data["bio"] == "This is a test author."
    assert data["birth_date"] == "1980-01-01"

def test_read_author_not_found(setup_database):
    response = client.get("/authors/99999")
    assert response.status_code == 404

def test_delete_author(setup_database):
    response = client.post("/authors/", json={
        "name": "Author to Delete",
        "bio": "This author will be deleted.",
        "birth_date": "1990-01-01"
    })
    author_id = response.json()["id"]

    response = client.delete(f"/authors/{author_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert data["message"] == "Author deleted"

    response = client.get(f"/authors/{author_id}")
    assert response.status_code == 404