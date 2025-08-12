import sys
import os
from src.main import app

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))


def test_hello():
    client = app.test_client()
    response = client.get("/")
    assert response.data == b"Hello, World!"
    assert response.status_code == 200
