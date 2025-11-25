from app import app

def test_protected_route_requires_token():
    client = app.test_client()

    # sem token → erro
    response_no_token = client.get("/protected")
    assert response_no_token.status_code == 401

    # com token → OK
    login = client.post("/login")
    token = login.get_json()["access_token"]

    response = client.get(
        "/protected",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert response.get_json()["message"] == "Protected route"
