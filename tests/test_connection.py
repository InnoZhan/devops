import requests


def connect():
    return requests.get("http://127.0.0.1:5000")


def test_answer():
    assert connect()