from app import app

def test_login():
    client = app.test_client()
    res = client.post('/login')
    assert res.status_code == 200
    assert "token" in res.get_json()
