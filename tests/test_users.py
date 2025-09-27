from app import schemas 
from .database import client, session
    
def test_root(client):

    res = client.get("/")
    print(res.json().get("message"))
    assert res.json().get("message") == "welcome to my FastAPI"
    assert res.status_code == 200

def test_create_user(client):
    res = client.post(
        "/users/", json={"email": "test@example.com", "password": "password"}
    )
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "test@example.com"
    assert res.status_code == 201

def test_login_user(client):
    res = client.post("/login", data={"username": "test@example.com", "password": "password"})
    print(res.json())
    assert res.status_code == 200
    assert "access_token" in res.json()