from app import app

def test_login_generates_token():
    client = app.test_client()
    response = client.post("/login")
    data = response.get_json()
    
    assert response.status_code == 200
    assert "access_token" in data
    assert isinstance(data["access_token"], str)
