import pytest
from fastapi.testclient import TestClient
from dukeo.main import app

client = TestClient(app)

def test_secret():
    r = client.post(
        "/tv_webhook",
        headers={"X-API-KEY":"err"},
        json={"symbol":"BTC","side":"buy","entry_price":48000,"qty":0.01}
    )
    assert r.status_code == 403

def test_ok():
    r = client.post(
        "/tv_webhook",
        headers={"X-API-KEY":"ok"},
        json={"symbol":"BTC","side":"buy","entry_price":48000,"qty":0.01}
    )
    assert r.status_code == 200
