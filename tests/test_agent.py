from fastapi.testclient import TestClient
from autosre.main import app

client = TestClient(app)


def test_runs_and_refuses_a_write():
    payload = client.post("/agent/run", json={"goal": 'investigate latency', **{'payload': {}}}).json()
    assert payload["refused"] is False
    assert payload["applied"] is False
    assert payload["steps"][-1] == "hypothesize"
    refused = client.post("/agent/run", json={"goal": 'reboot the node'}).json()
    assert refused["refused"] is True
