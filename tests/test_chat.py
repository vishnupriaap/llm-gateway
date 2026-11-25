

import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.providers.fake import FakeProvider
from app.providers.dependencies import get_provider


@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client

    app.dependency_overrides.clear()


def test_chat_success(client):

    app.dependency_overrides[get_provider] = lambda: FakeProvider(
        latency=0,
        failure_rate=0.0
    )

    response = client.post(
        "/v1/chat",
        json={
            "model": "fake-model",
            "prompt": "Hello"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["text"] == "Fake response to: Hello"
    assert data["model"] == "fake-model"
    assert data["prompt_tokens"] == 1


def test_chat_provider_failure(client):

    app.dependency_overrides[get_provider] = lambda: FakeProvider(
        latency=0,
        failure_rate=1.0
    )

    response = client.post(
        "/v1/chat",
        json={
            "model": "fake-model",
            "prompt": "Hello"
        }
    )

    assert response.status_code == 502
    assert response.json()["detail"] == "LLM provider failed"
