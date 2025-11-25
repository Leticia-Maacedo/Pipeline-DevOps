from app import app

def test_items_route():
    client = app.test_client()
    response = client.get("/items")

    assert response.status_code == 200
    
    data = response.get_json()
    assert "items" in data
    assert data["items"] == ["item1", "item2", "item3"]
