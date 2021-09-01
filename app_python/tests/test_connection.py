from server import app

app.testing = True
client = app.test_client()


def connect():
    return client.get("http://127.0.0.1:5000/")


def test_answer():
    assert connect()
