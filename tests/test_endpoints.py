import pytest
from fastapi.testclient import TestClient
from datetime import datetime

def test_read_user(client):
    response = client.get("/api/v1/users/1")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "name" in data
    assert "email" in data
    assert "timestamp" in data

def test_read_posts_with_last_user(client):
    client.get("/api/v1/users/1")
    response = client.get("/api/v1/posts")
    assert response.status_code == 200
    data = response.json()
    assert "User Posts" in data
    assert "timestamp" in data
    assert isinstance(data["User Posts"], list)

def test_read_posts_with_specific_user(client):
    response = client.get("/api/v1/posts?user_id=1")
    assert response.status_code == 200
    data = response.json()
    assert "User Posts" in data
    assert "timestamp" in data
    assert isinstance(data["User Posts"], list)

def test_read_posts_without_user(client):
    response = client.get("/api/v1/posts")
    assert response.status_code == 400
    assert "No user has been fetched or is not provided" in response.json()["detail"]

def test_user_not_found(client):
    response = client.get("/api/v1/users/999")
    assert response.status_code == 404

def test_posts_with_invalid_user(client):
    response = client.get("/api/v1/posts?user_id=999")
    assert response.status_code == 400