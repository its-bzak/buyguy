from unittest.mock import patch
import pytest
from app.services.paypal import get_paypal_access_token
import requests

PAYPAL_CLIENT_ID = "mock_client_id"
PAYPAL_CLIENT_SECRET = "mock_client_secret"
PAYPAL_API_BASE = "https://mock.api.sandbox.paypal.com"

@pytest.fixture(autouse=True)
def mock_env_vars(monkeypatch):
    # Instead of typing decorators for every test
    monkeypatch.setattr("app.services.paypal.PAYPAL_CLIENT_ID", "mock_client_id")
    monkeypatch.setattr("app.services.paypal.PAYPAL_CLIENT_SECRET", "mock_client_secret")
    monkeypatch.setattr("app.services.paypal.PAYPAL_API_BASE", "https://mock.api.sandbox.paypal.com")


@patch("app.services.paypal.requests.post")
def test_get_paypal_access_token(mock_post):
    # Return access token on success (200)

    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {
        "access_token":"mock_access_token",
        "token_type":"bearer",
        "expires_in":3600
    }

    token = get_paypal_access_token()

    assert token == "mock_access_token"

@patch("app.services.paypal.requests.post")
def test_get_paypal_access_token_auth_error(mock_post):
    # Return none with invalid credentials (401)

    mock_post.return_value.status_code = 401
    mock_post.return_value.json.return_value = {
        "error": "invalid_client",
        "error_description": "Client Authentication failed"
    }

    token = get_paypal_access_token()

    assert token is None

@patch("app.services.paypal.requests.post")
def test_get_paypal_access_token_server_error(mock_post):
    # Return none with server error (5xx)

    mock_post.return_value.status_code = 500
    mock_post.return_value.json.return_value = {
        "error": "server_error",
        "error_description": "Internal Server Error"
    }

    token = get_paypal_access_token()

    assert token is None

@patch("app.services.paypal.requests.post")
def test_get_paypal_access_token_network_timeout(mock_post):
    # Handle network timeout gracefully and return None

    mock_post.side_effect = requests.exceptions.Timeout("Connection timed out")
    token = get_paypal_access_token()

    assert token is None

@patch("app.services.paypal.requests.post")
def test_get_paypal_access_token_invalid_json(mock_post):
    # Handle malformed JSON response and return None

    mock_post.return_value.status_code = 200
    mock_post.return_value.json.side_effect = ValueError("Malformed JSON")

    token = get_paypal_access_token()
    assert token is None

@patch("app.services.paypal.requests.post")
def test_get_paypal_access_token_missing_key(mock_post):
    # Handle missing access_token key in response and return None

    mock_post.return_value.status_code = 200
    mock_post.return_value.json.return_value = {
        "token_type": "bearer",
        "expires_in": 3600
    }

    token = get_paypal_access_token()
    assert token is None